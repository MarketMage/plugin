---
type: agent
expect:
  actorId: /^cleanpull[~\/][a-z-]+$/
  name: /^cw-[a-z0-9-]+$/
---

You are the Apify `create-actor-task` tool. The task was created. Reply with only a JSON object: `taskId` "tsk" followed by 6 letters, `actorId`, `name`, `title` and `description` as given (null if not given), `publishedAt` null, `publicConfig` null, and `input` exactly as given in the call.
