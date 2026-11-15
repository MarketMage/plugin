#!/usr/bin/env bash
# Run the eval suite against the shipped plugin folder.
#
#   scripts/eval.sh [claude plugin eval options...]
#   e.g. scripts/eval.sh --ablation none --case 'validate-*' -j 4
#
# The evals live in evals/ at the repository root, outside the plugin folder, so they never ship to
# users. `claude plugin eval` only reads an eval dir inside the plugin folder (--eval-dir and the
# manifest's experimental.evals both refuse "..", and it refuses a symlinked evals/). So this script
# copies the plugin folder (marketplace.json's plugins[0].source) and evals/ (without results/) into
# a temporary folder, runs the eval there, and copies the results back to evals/results/, also when
# the run fails or is interrupted. Relative --json, --report and --output-dir paths are taken from the
# directory you run it in. --trust-plugin is passed: this is our own plugin and suite.
set -euo pipefail
repo="$(cd "$(dirname "$0")/.." && pwd)"
caller="$(pwd)"
plugin="$(python3 "$repo/scripts/plugin_dir.py")"

# Make relative output paths absolute against the caller's directory, before the cd below.
abs() { case "$1" in /*) printf '%s' "$1" ;; *) printf '%s' "$caller/$1" ;; esac; }
args=()
while [ $# -gt 0 ]; do
  case "$1" in
    --json|--report|--output-dir)
      # --json takes an optional path: only a following non-option argument is one.
      if [ $# -gt 1 ] && [ "${2#-}" = "$2" ]; then args+=("$1" "$(abs "$2")"); shift 2; else args+=("$1"); shift; fi ;;
    --json=*|--report=*|--output-dir=*)
      args+=("${1%%=*}=$(abs "${1#*=}")"); shift ;;
    --eval-dir|--eval-dir=*)
      echo "eval.sh: --eval-dir isn't supported: the suite is always evals/ (copied next to the plugin)" >&2; exit 2 ;;
    *) args+=("$1"); shift ;;
  esac
done

tmp="$(mktemp -d "${TMPDIR:-/tmp}/marketmage-eval.XXXXXX")"
copy_back() {
  set +e  # always clean up, even if a copy fails
  if [ -d "$tmp/evals/results" ]; then
    mkdir -p "$repo/evals/results"
    cp -R "$tmp/evals/results/." "$repo/evals/results/" || echo "eval.sh: could not copy every result back" >&2
    # Mock-recording notes (ADOPT.txt) name files in the temporary folder: point them at the repo.
    find "$repo/evals/results" -name ADOPT.txt -newer "$tmp" -exec sed -i.bak "s#$tmp/evals#$repo/evals#g" {} \; -exec rm -f {}.bak \;
  fi
  rm -rf "$tmp"
}
trap copy_back EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

cp -R "$plugin/." "$tmp/"
mkdir "$tmp/evals"
(cd "$repo/evals" && find . -mindepth 1 -maxdepth 1 ! -name results -exec cp -R {} "$tmp/evals/" \;)
cd "$tmp"
claude plugin eval . --trust-plugin ${args[@]+"${args[@]}"}
