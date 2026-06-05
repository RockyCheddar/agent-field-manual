---
title: handoff
type: skill
source: external-original
origin_url: https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md
repo: mattpocock/skills
source_commit: aaf2453fbdfe7a15c07f11d861224f34ab4b53cb
author: Matt Pocock
license: MIT
status: raw
tags:
  - external
  - mattpocock-skills
use_when: You want the original upstream skill behavior from Matt Pocock Skills.
avoid_when: You need Seedvision-specific operating guidance; adapt and promote it first.
---

---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS - not the current workspace.

Include a "suggested skills" section in the document, which suggests skills that the agent should invoke.

Do not duplicate content already captured in other artifacts (PRDs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
