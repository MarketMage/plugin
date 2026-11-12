# Release: going public

**State (12 Nov 2026, 0.4.15):** the repository is public (since 9 Nov), with branch protection, secret scanning, push protection and private vulnerability reporting on; the plugin is pinned on the organization; marketmage.io is indexable and shows the GitHub install. Left: the reviewer test account, then the directory submission (below). This file keeps what is ready and the commands that were used, for reference.

**Which account runs the commands.** Every command runs as **marketmage-dev**, the MarketMage organization's own account (its `gh` login is labelled `MarketMage`). Commits and pushes always come from it, so the history shows MarketMage only. Check the active account first; other sessions switch accounts too:

```bash
gh auth switch --user MarketMage
gh auth status        # the active account must be marketmage-dev
```

## What is ready

- The plugin users install is `marketmage/`. It holds 505 files; the directory's limit is 512. The largest file is the icon, `.claude-plugin/icon.png` (123 KB, an image, so the directory's 256 KiB limit for non-image files doesn't apply to it). The largest text file is `skills/find-products/SKILL.md` (51 KB). `scripts/check.py` keeps it within the limits in CI.
- `/plugin marketplace add MarketMage/plugin` then `/plugin install marketmage@marketmage` installs `marketmage/`, because the marketplace's `source` is `./marketmage`. The scripts read the plugin folder from that field.
- License: PolyForm Shield 1.0.0, the official text verbatim, with `Required Notice: Copyright (c) 2026 Extoris LLC (https://marketmage.io)`, in `LICENSE` and `marketmage/LICENSE`; `plugin.json` says `PolyForm-Shield-1.0.0`.
- `SECURITY.md`, `CONTRIBUTING.md`, issue templates (bug report, feature idea, support link) with their `bug` and `idea` labels, and `.gitignore`.
- Listing icon: `marketmage/.claude-plugin/icon.png` (the site's 512 px icon). The directory's docs (checked 12 Nov) read a plugin listing from the files of the live version, so a new icon ships like any other change, as a new version.
- **History:** this repository started from one fresh commit, so no earlier snapshot (with its old MIT license) is ever public. The development history, PRs #1–#36, is kept in the private, archived repository `MarketMage/plugin-history`. Never push from an old clone to this repository.

## Release zips

Every version is also published as a zip, for people who install with **Upload plugin**.

- **How it runs:** `.github/workflows/release.yml` runs on every push to `main` (and by hand: **Actions → release → Run workflow**). It reads `version` from `marketmage/.claude-plugin/plugin.json`; if the tag `v<version>` doesn't exist yet, it zips the **contents** of `marketmage/` (so `.claude-plugin/plugin.json` is at the zip's top level, as Upload plugin needs; `.DS_Store` and other system files left out), creates the tag and a release named `MarketMage <version>`, and attaches `marketmage.zip`. If the tag exists, it does nothing.
- **To release:** bump `version` in `plugin.json` in the PR as usual and merge it. Nothing else.
- **The stable link:** the asset is always named `marketmage.zip`, so https://github.com/MarketMage/plugin/releases/latest/download/marketmage.zip serves the newest version. marketmage.io/download/marketmage.zip redirects there, and the site's download page reads the version and size from the latest release when the site is built, so rebuild and deploy the site after a release.
- **Permissions:** the workflow asks for `contents: write` (the organization's default token is read-only) and uses only `actions/checkout` and the `gh` CLI, as the organization allows only GitHub's own actions. Branch protection covers `main` only, so creating tags isn't blocked.
- **Redo a release:** delete the release and its tag (`gh release delete v<version> --cleanup-tag --yes`), then run the workflow by hand.

## The organization (done 2026-11-05)

GitHub no longer converts a personal account into an organization, so the account was renamed and a new organization took the name:

- **MarketMage** is an organization owned by Extoris LLC, on the Free plan. Its owners' memberships are private, so the profile page lists no one.
- **Profile:** name, description, website https://marketmage.io, email support@marketmage.io, the site's icon as the avatar, and a profile page in [`MarketMage/.github`](https://github.com/MarketMage/.github) (`profile/README.md`, with an organization-wide `SECURITY.md`).
- **marketmage.io is verified** (DNS TXT record `_gh-MarketMage-o`, in Vercel's DNS for the domain).
- **Two-factor authentication is required** for every member, with secure methods only (no SMS).
- **Actions:** only GitHub's own actions and the organization's may run; the default `GITHUB_TOKEN` is read-only and can't approve pull requests; workflows from outside contributors need approval.
- **New repositories** get Dependabot alerts, the dependency graph, and secret scanning with push protection.
- **This repository:** description, homepage, topics, wiki and projects off, issues on, Dependabot alerts on, squash merges only (title and body from the PR), branches deleted on merge.

## Left to do, in order

1. ✓ **Make the repository public** (done 9 Nov), then the go-live settings below (done 9 Nov).
2. ✓ **Pin the plugin** on the organization's profile (done 9 Nov).
3. **Reviewer test account** (before submitting; `plans/claude-plugin/submission-checklist.md`, 3.D): a separate Apify account with its own mailbox (for example review@marketmage.io) and about USD 10 of credit. Sign in to it once from Claude, then ask Claude to create the sample watchlist `cw-price-sample` (no recipients) and run it twice. Its sign-in details go only in the submission form.
4. **Submit to the directory** at https://claude.ai/directory/manage: **Submit new → Plugin bundle**, repository `MarketMage/plugin`, plugin path `marketmage`, branch `main`. Install the Claude GitHub App on the repository if the portal asks. If the form asks for a privacy policy, it is https://marketmage.io/privacy/ (the manifest has no privacy key: claude.ai strips it).

## Make it public

```bash
gh auth switch --user MarketMage
gh repo edit MarketMage/plugin --visibility public --accept-visibility-change-consequences
```

## Go-live settings (need a public repository or a paid plan)

GitHub refuses these on a private repository on the Free plan ("Upgrade to GitHub Pro or make this repository public"). Run them after the repository is public.

**Branch protection on `main`:** changes through pull requests, the `check` workflow must pass, no force-pushes, no deletion. Owners can still push directly (`enforce_admins` is off).

```bash
gh api -X PUT repos/MarketMage/plugin/branches/main/protection --input - <<'EOF'
{
  "required_status_checks": { "strict": true, "contexts": ["check"] },
  "enforce_admins": false,
  "required_pull_request_reviews": { "required_approving_review_count": 0 },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "required_linear_history": false,
  "required_conversation_resolution": true
}
EOF
```

**Secret scanning and push protection:**

```bash
gh api -X PATCH repos/MarketMage/plugin --input - <<'EOF'
{ "security_and_analysis": {
    "secret_scanning": { "status": "enabled" },
    "secret_scanning_push_protection": { "status": "enabled" } } }
EOF
```

**Private vulnerability reporting** (so people can report privately on GitHub as well as by email):

```bash
gh api -X PUT repos/MarketMage/plugin/private-vulnerability-reporting
```

**Check:**

```bash
gh api repos/MarketMage/plugin -q '{visibility, security_and_analysis}'
gh api repos/MarketMage/plugin/branches/main/protection -q '{checks: .required_status_checks.contexts, force: .allow_force_pushes.enabled}'
gh api repos/MarketMage/plugin/private-vulnerability-reporting
```

## After go-live

- ✓ **Update marketmage.io the same day** (done 9 Nov): site branch `go-live` had `"repo_public": true` and `"preview": false` on top of the PolyForm Shield Terms and the corrected license in the structured data. Deploy it to production, so the docs show the GitHub link and install commands and search engines may index the site.
- Test the public install in a clean config:

  ```bash
  export CLAUDE_CONFIG_DIR=$(mktemp -d)
  claude plugin marketplace add MarketMage/plugin
  claude plugin install marketmage@marketmage
  claude plugin list
  unset CLAUDE_CONFIG_DIR
  ```

