---
title: Whiteboard Gremlin Illustrations
type: skill
source: seedvision-original
origin_url:
repo: RockyCheddar/agent-field-manual
author: Seedvision
license: MIT
status: draft
use_when: You need clean, strange, memorable English article illustrations for AI, product, workflow, strategy, or operating-system content.
avoid_when: You need polished commercial brand art, a dense infographic, a faithful technical architecture diagram, or copied character/IP from another creator.
---

# Whiteboard Gremlin Illustrations

## Contract

This skill turns an article, memo, concept, or workflow into original 16:9 editorial illustrations with a clean whiteboard-sketch style.

It guarantees:

- English-first visuals with short, readable handwritten labels.
- Original character language; no copying named characters, example compositions, or creator-specific IP.
- One cognitive move per image: a judgment, transition, loop, bottleneck, handoff, contrast, or metaphor.
- Sparse, weird, useful illustrations — not PPT slides, not mascot stickers, not generic AI art.
- A shot list before generation unless the user explicitly asks for one single image.

## Visual DNA

The default style is **deadpan whiteboard weirdness**:

- 16:9 horizontal canvas.
- Pure white background.
- Black hand-drawn line art with slight wobble.
- Lots of empty space; subject usually occupies 35%-60% of the frame.
- Small accent marks in red, orange, and blue.
- English handwritten labels only; keep labels short, usually 1-4 words.
- A tiny recurring operator character, called the **Gremlin**, performs the core action.
- Product-sketch energy: clear, rough, clever, not polished.

The Gremlin is not a cute mascot. It is a small odd worker inside the system: serious, blank, slightly overcommitted, and doing the awkward job that makes the metaphor work.

## Do Not Copy

This skill is a clean-room Seedvision original. Do not copy another creator's recurring character, language, examples, compositions, labels, or visual identity.

Avoid:

- Named external characters or IP.
- Chinese labels unless the user specifically asks.
- Reusing another repo's exact metaphor set, sample image layouts, or character description.
- Treating style references as templates.
- Copying any upstream example images.

## Workflow

### 1. Read for cognitive anchors

Extract the parts of the input worth visualizing:

- The core claim.
- A before/after shift.
- A process loop.
- A bottleneck or failure mode.
- A handoff between people/tools/agents.
- A compounding mechanism.
- A trust-building or evidence-building sequence.
- A hidden system underneath a simple surface.

Do not illustrate every section. Pick the few moments where a drawing would make the reader understand faster or remember longer.

### 2. Build a shot list

Unless the user asks for a single image, propose 3-7 shots.

For each shot include:

- Placement: where it belongs in the article or thread.
- Title: internal title only; do not put this title on the image.
- Cognitive anchor: what the reader should understand.
- Structure type.
- Physical metaphor.
- Gremlin action.
- Suggested labels.
- Why this image earns its place.

Short article: 1-3 shots. Long article: 4-7 shots. Do not exceed 8 unless the user asks.

### 3. Choose one structure type

Use one primary structure per image:

- **Input → machine → output:** raw material becomes something useful.
- **Before / after:** chaos becomes leverage, manual becomes automated, vague becomes testable.
- **Loop:** capture, process, ship, learn, repeat.
- **Handoff path:** idea moves from human to agent to artifact to user.
- **Bottleneck:** one stuck point blocks a whole system.
- **Filter or sorter:** many inputs become a few useful decisions.
- **Layer stack:** foundations support tools, workflows, and outcomes.
- **Map route:** a journey with 3-5 landmarks.
- **Small comic:** 2-4 panels showing a state change.
- **Evidence bridge:** trust is built piece by piece.

### 4. Invent a fresh physical metaphor

Translate the abstract idea into a physical scene.

Useful metaphor ingredients:

- Leaky pipes, mail slots, trap doors, pulleys, ladders, drawers, odd machines, conveyor belts, clamps, switches, funnels, shelves, magnets, bridges, pressure gauges, buckets, stamps, field notes, tiny cranes, repair tape, signal towers, split roads, nesting boxes.

Use only 1-3 main objects. The weirdness should clarify the idea, not clutter the image.

### 5. Make the Gremlin necessary

The Gremlin must do the conceptual work:

- Pulling a stuck lever.
- Sorting inputs into bins.
- Holding a bridge together.
- Catching falling context.
- Feeding raw notes into a machine.
- Tightening a feedback loop.
- Carrying evidence blocks.
- Redirecting a pipe.
- Labeling a dangerous shortcut.
- Measuring whether output improved.

If the image still works perfectly after removing the Gremlin, rewrite it.

### 6. Generate one image at a time

Use one prompt per image. Never combine the whole shot list into a grid unless the user asks for a contact sheet.

Default generation constraints:

- 16:9 horizontal.
- White background.
- Black sketch lines.
- Sparse red/orange/blue accent notes.
- Short English handwritten labels.
- No title text in the top-left.
- No dense flowchart.
- No glossy vector art.
- No app screenshots.
- No fake UI.
- No cute mascot poster.

### 7. QA before delivery

Pass/fail checklist:

- One core idea only.
- Gremlin performs the main action.
- Labels are short and readable.
- Plenty of empty space.
- Looks hand-drawn, not corporate.
- Feels strange but legible.
- Does not resemble an external sample composition.
- No Chinese text unless requested.
- No title in the image.
- No dense lecture-slide energy.

If it fails, regenerate with fewer elements and a clearer Gremlin action.

## Prompt Template

```text
Create one standalone 16:9 horizontal editorial illustration for an English article.

Style:
Pure white background. Minimal black hand-drawn line art with slight wobble. Sparse red, orange, and blue handwritten accent notes. Lots of negative space. Rough whiteboard/product-sketch energy. Clever, deadpan, slightly absurd, but clean and readable.

Recurring original character:
Include one tiny black-and-white "Gremlin" operator: a small irregular ink-like worker with tiny dot eyes and thin limbs, blank serious expression, not cute, not a mascot, not a known character. The Gremlin must perform the core conceptual action.

Theme:
{theme}

Core idea:
{one sentence describing what the reader should understand}

Structure type:
{input-machine-output | before-after | loop | handoff path | bottleneck | filter | layer stack | map route | small comic | evidence bridge}

Composition:
{describe the physical scene, where the Gremlin is, what it is doing, how the idea moves through the scene}

Suggested elements:
{3-5 concrete objects}

Handwritten English labels:
{label 1} / {label 2} / {label 3} / {optional label 4} / {optional label 5}

Color rules:
Black for main sketch and character. Orange for path/flow/motion. Red for risk/problem/result. Blue for system feedback or side notes.

Constraints:
One image explains one idea. Keep subject around 35%-60% of the canvas. Use at most 3-6 short labels. Do not include a big title. Do not write the structure type. Do not create a PPT infographic, dense flowchart, corporate vector illustration, cute mascot poster, children’s book style, realistic UI, or complex technical architecture. Invent a fresh metaphor for this specific content.
```

## Output Format

For shot-list mode:

```markdown
## Illustration Plan

1. **{internal title}**
   - Placement: {where it goes}
   - Cognitive anchor: {what it explains}
   - Structure: {structure type}
   - Metaphor: {physical metaphor}
   - Gremlin action: {what it does}
   - Labels: `{label}`, `{label}`, `{label}`
   - Why it earns space: {reason}
```

For generation mode:

```markdown
Generated {n} illustrations.

- `01-{slug}.png` — {purpose / placement}
- `02-{slug}.png` — {purpose / placement}

Strongest image: {which one and why}
Optional/regenerate candidate: {which one and why, if any}
```

## Anti-Patterns

- Making a generic AI/network/robot illustration.
- Creating a formal chart with too many arrows.
- Turning the Gremlin into a cute brand mascot.
- Using long labels or full sentence explanations in the image.
- Copying another creator's sample compositions or named IP.
- Making every shot use the same machine/funnel/bridge metaphor.
- Letting aesthetic weirdness outrun conceptual clarity.
