#!/usr/bin/env python3
"""Ingest external AI-agent skill repositories into Agent Field Manual.

This script is intentionally stdlib-only. It copies MIT-licensed source repos into
`sources/<id>/raw`, writes attribution/index files, and promotes discovered
SKILL.md files into `skills/external/<id>/...` with provenance frontmatter.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = Path.home() / ".cache" / "agent-field-manual-sources"


@dataclass(frozen=True)
class Source:
    id: str
    name: str
    owner: str
    repo: str
    url: str
    description: str
    raw_skill_globs: tuple[str, ...]


SOURCES = [
    Source(
        id="garrytan-gstack",
        name="gstack",
        owner="Garry Tan",
        repo="garrytan/gstack",
        url="https://github.com/garrytan/gstack",
        description="Garry Tan's Claude Code / OpenClaw skill pack and agent setup.",
        raw_skill_globs=("*/SKILL.md", "browser-skills/*/SKILL.md"),
    ),
    Source(
        id="mattpocock-skills",
        name="Matt Pocock Skills",
        owner="Matt Pocock",
        repo="mattpocock/skills",
        url="https://github.com/mattpocock/skills",
        description="Engineering, planning, debugging, and productivity skills for real software work with agents.",
        raw_skill_globs=("skills/*/*/SKILL.md",),
    ),
    Source(
        id="every-compound-engineering",
        name="Every Compound Engineering Plugin",
        owner="Every Inc.",
        repo="everyinc/compound-engineering-plugin",
        url="https://github.com/everyinc/compound-engineering-plugin",
        description="Compound engineering Claude Code plugin: skills and agents that make each engineering unit easier than the last.",
        raw_skill_globs=("plugins/*/skills/*/SKILL.md", "tests/skills/*/SKILL.md"),
    ),
    Source(
        id="addyosmani-agent-skills",
        name="Addy Osmani Agent Skills",
        owner="Addy Osmani",
        repo="addyosmani/agent-skills",
        url="https://github.com/addyosmani/agent-skills",
        description="A practical agent skills library covering specs, testing, code quality, context engineering, browser testing, launch readiness, and software delivery workflows.",
        raw_skill_globs=("skills/*/SKILL.md",),
    ),
]


def run(cmd: list[str], cwd: Path | None = None) -> str:
    return subprocess.check_output(cmd, cwd=cwd, text=True).strip()


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9._-]+", "-", text.lower()).strip("-") or "item"


def copytree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)

    def ignore(dirpath: str, names: list[str]) -> set[str]:
        # Keep the public repo focused and avoid shipping upstream test fixtures
        # that can contain fake keys/private keys which trigger scanners.
        ignored = {
            ".git",
            "node_modules",
            ".next",
            "dist",
            "build",
            "coverage",
            ".DS_Store",
            "test",
            "tests",
            "fixtures",
            "__fixtures__",
        }
        return {n for n in names if n in ignored}

    shutil.copytree(src, dst, ignore=ignore)


def detect_license(repo_dir: Path) -> tuple[str, str]:
    files = sorted([p for p in repo_dir.iterdir() if p.name.upper().startswith("LICENSE")])
    if not files:
        return "UNKNOWN", ""
    text = files[0].read_text(errors="ignore")
    kind = "MIT" if "MIT License" in text[:500] else "SEE LICENSE"
    return kind, files[0].name


def discover_skill_files(repo_dir: Path, patterns: tuple[str, ...]) -> list[Path]:
    seen: dict[str, Path] = {}
    for pattern in patterns:
        for path in repo_dir.glob(pattern):
            if path.is_file() and ".git" not in path.parts:
                seen[str(path.relative_to(repo_dir))] = path
    return [seen[k] for k in sorted(seen)]


def title_from_skill(path: Path) -> str:
    text = path.read_text(errors="ignore")
    for line in text.splitlines()[:40]:
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip().strip('"\'')
        if line.startswith("# "):
            return line[2:].strip()
    return path.parent.name


def frontmatter(src: Source, rel: Path, commit: str, license_kind: str, title: str) -> str:
    return f"""---
title: {title}
type: skill
source: external-original
origin_url: {src.url}/blob/main/{rel.as_posix()}
repo: {src.repo}
source_commit: {commit}
author: {src.owner}
license: {license_kind}
status: raw
tags:
  - external
  - {src.id}
use_when: You want the original upstream skill behavior from {src.name}.
avoid_when: You need Seedvision-specific operating guidance; adapt and promote it first.
---

"""


def write_source_doc(src: Source, commit: str, license_kind: str, license_file: str, skills: list[Path], repo_dir: Path) -> None:
    out = ROOT / "sources" / src.id / "SOURCE.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {src.name}",
        "",
        f"- Source repo: [{src.repo}]({src.url})",
        f"- Owner/author: {src.owner}",
        f"- Imported commit: `{commit}`",
        f"- License: {license_kind}" + (f" (`raw/{license_file}`)" if license_file else ""),
        f"- Local raw snapshot: `sources/{src.id}/raw/`",
        f"- Promoted raw skills: `skills/external/{src.id}/`",
        "",
        f"> {src.description}",
        "",
        "## Import policy",
        "",
        "This source is imported as an attributed external dependency. Files promoted into the library preserve upstream attribution and commit metadata. Seedvision-specific adaptations should be created separately with `source: external-adapted`, not silently edited in place.",
        "",
        "## Discovered skills",
        "",
    ]
    for p in skills:
        rel = p.relative_to(repo_dir)
        lines.append(f"- `{rel.as_posix()}` — {title_from_skill(p)}")
    out.write_text("\n".join(lines) + "\n")


def write_external_skills(src: Source, commit: str, license_kind: str, skills: list[Path], repo_dir: Path) -> None:
    base = ROOT / "skills" / "external" / src.id
    if base.exists():
        shutil.rmtree(base)
    base.mkdir(parents=True, exist_ok=True)
    for p in skills:
        rel = p.relative_to(repo_dir)
        title = title_from_skill(p)
        out_dir = base / slug(str(rel.parent))
        out_dir.mkdir(parents=True, exist_ok=True)
        body = p.read_text(errors="ignore")
        # Avoid nested frontmatter confusion in the compiled library.
        out = frontmatter(src, rel, commit, license_kind, title) + body
        (out_dir / "SKILL.md").write_text(out)
        (out_dir / "UPSTREAM.md").write_text(
            f"# Upstream\n\n- Source: {src.url}/blob/main/{rel.as_posix()}\n- Repo: {src.repo}\n- Commit: `{commit}`\n- License: {license_kind}\n"
        )


def write_main_docs(all_rows: list[dict[str, str | int]]) -> None:
    readme = ROOT / "README.md"
    readme.write_text("""# Agent Field Manual

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
""" + "".join(
        f"| {r['name']} | [{r['repo']}]({r['url']}) | {r['license']} | `{str(r['commit'])[:12]}` | {r['count']} |\n"
        for r in all_rows
    ) + """

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
""")

    attr = ROOT / "ATTRIBUTION.md"
    attr.write_text("# Attribution\n\n" + "\n".join(
        f"## {r['name']}\n\n- Repo: [{r['repo']}]({r['url']})\n- Author/owner: {r['owner']}\n- License: {r['license']}\n- Imported commit: `{r['commit']}`\n- Local source notes: `sources/{r['id']}/SOURCE.md`\n"
        for r in all_rows
    ) + "\n")

    (ROOT / "docs" / "promotion-workflow.md").write_text("""# Promotion Workflow

Raw imports are not automatically endorsed. Use this workflow to turn external material into a clean Agent Field Manual artifact.

1. **Identify the pattern** — what job does the source item actually perform?
2. **Check fit** — is it useful for agent architecture, client ops, engineering quality, research, content, or business execution?
3. **Preserve provenance** — keep source repo, author, license, commit, and upstream URL.
4. **Rewrite for this library** — clarify `use_when`, `avoid_when`, setup assumptions, outputs, and failure modes.
5. **Test in real work** — run the skill/playbook on an actual task before marking it `tested`.
6. **Promote deliberately** — put durable adaptations under `skills/seedvision/`, `frameworks/`, or `playbooks/`.

Do not mutate `skills/external/*` as if it were original work. Create adaptations instead.
""")


def main() -> None:
    rows: list[dict[str, str | int]] = []
    for src in SOURCES:
        repo_dir = CACHE / src.id
        if not repo_dir.exists():
            run(["git", "clone", "--depth", "1", src.url + ".git", str(repo_dir)])
        commit = run(["git", "rev-parse", "HEAD"], cwd=repo_dir)
        license_kind, license_file = detect_license(repo_dir)
        raw_dst = ROOT / "sources" / src.id / "raw"
        copytree(repo_dir, raw_dst)
        skills = discover_skill_files(repo_dir, src.raw_skill_globs)
        write_source_doc(src, commit, license_kind, license_file, skills, repo_dir)
        write_external_skills(src, commit, license_kind, skills, repo_dir)
        rows.append({
            "id": src.id,
            "name": src.name,
            "owner": src.owner,
            "repo": src.repo,
            "url": src.url,
            "license": license_kind,
            "commit": commit,
            "count": len(skills),
        })
    write_main_docs(rows)
    print("Imported sources:")
    for r in rows:
        print(f"- {r['id']}: {r['count']} skills @ {str(r['commit'])[:12]} ({r['license']})")


if __name__ == "__main__":
    main()
