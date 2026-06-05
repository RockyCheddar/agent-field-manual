# Promotion Workflow

Raw imports are not automatically endorsed. Use this workflow to turn external material into a clean Agent Field Manual artifact.

1. **Identify the pattern** — what job does the source item actually perform?
2. **Check fit** — is it useful for agent architecture, client ops, engineering quality, research, content, or business execution?
3. **Preserve provenance** — keep source repo, author, license, commit, and upstream URL.
4. **Rewrite for this library** — clarify `use_when`, `avoid_when`, setup assumptions, outputs, and failure modes.
5. **Test in real work** — run the skill/playbook on an actual task before marking it `tested`.
6. **Promote deliberately** — put durable adaptations under `skills/seedvision/`, `frameworks/`, or `playbooks/`.

Do not mutate `skills/external/*` as if it were original work. Create adaptations instead.
