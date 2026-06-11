# Agent Field Manual

Curated frameworks, skills, and playbooks for building real AI agent systems.

This repo is designed as an operator-grade library, not a prompt dump. It keeps raw upstream material clearly attributed, then promotes only useful patterns into clean frameworks, skills, playbooks, and templates.

## Operating principles

1. **Attribution first** — external work stays linked to its source, author, license, and commit.
2. **Raw is not refined** — imported skills are useful references, but Seedvision adaptations live separately.
3. **Field-tested beats clever** — promote patterns only when they survive actual use.
4. **Frameworks over fragments** — organize around when/how to use a pattern, not where it was found.
5. **Public repo as showroom** — keep messy private experiments out unless they teach a reusable lesson.

## Library map

- `sources/` — attributed upstream snapshots, source notes, and import indexes.
- `skills/external/` — raw imported skill files with provenance frontmatter.
- `skills/seedvision/` — original or adapted Seedvision skills. Empty until deliberately promoted.
- `frameworks/` — reusable conceptual models for agent systems.
- `playbooks/` — step-by-step operating guides.
- `templates/` — reusable prompts, specs, PRDs, eval rubrics, and client docs.
- `case-studies/` — public-safe implementation notes and anonymized examples.
- `tools/` — ingestion and normalization utilities.

## Imported sources

| Source | Repo | License | Commit | Imported skills |
| --- | --- | --- | --- | ---: |
| gstack | [garrytan/gstack](https://github.com/garrytan/gstack) | MIT | `cab774cced06` | 54 |
| Matt Pocock Skills | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT | `aaf2453fbdfe` | 29 |
| Every Compound Engineering Plugin | [everyinc/compound-engineering-plugin](https://github.com/everyinc/compound-engineering-plugin) | MIT | `bb0c9ab4ee59` | 40 |
| Addy Osmani Agent Skills | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT | `d187883b7d76` | 24 |


## Skill metadata standard

Every promoted file should include:

```yaml
title:
type: skill | framework | playbook | prompt | template
source: seedvision-original | seedvision-refined | external-original | external-adapted
origin_url:
repo:
source_commit:
author:
license:
status: raw | tested | refined | deprecated
use_when:
avoid_when:
```

## Promotion workflow

1. Add or update raw source under `sources/<source-id>/raw`.
2. Generate/update `SOURCE.md` and `skills/external/<source-id>/`.
3. Read the raw item.
4. Create a refined adaptation under `skills/seedvision/`, `frameworks/`, or `playbooks/`.
5. Preserve attribution and explain what changed.
6. Mark adaptations as `tested` only after real use.

## License

This repository is MIT licensed. Imported external materials retain their original licenses and attribution; see `ATTRIBUTION.md` and each `sources/*/SOURCE.md`.
