---
name: yujia-v2-3
description: Strictly generate, reframe, and audit consistent 3:4 photorealistic lifestyle images of clearly adult Chinese women aged 20–30 in opaque fitted athletic tops and high-waisted yoga leggings. Enforces exact left/right rule-of-thirds composition, one-image-per-file output, deliberately different identities, hairstyles, top silhouettes, scenes, actions, palettes, and lighting across a batch, plus mandatory readable environmental Chinese signage/text, per-image review, and whole-batch PASS/FAIL audit before delivery.
---

# Yujia V2.3 — strict generation + runtime safety guard + acceptance audit + readable environmental Chinese text

Produce repeatable lifestyle photographs from two approved benchmark images while preventing the common failure mode of turning a batch into near-duplicates of the same woman, hairstyle, top, street, lighting, or centered composition.


## ABSOLUTE OUTPUT RULE — ZERO EXCEPTIONS

This rule overrides every other generation convenience or batching behavior:

1. **ONE FILE = ONE PHOTOGRAPH ONLY.** Never place two or more generated images inside one file/canvas. No collage, grid, diptych, split screen, storyboard, contact sheet, tiled layout, before/after pair, or multi-panel composition.
2. **ONE PHOTOGRAPH = ONE HUMAN ONLY.** The entire visible frame may contain exactly one human figure: the intended adult woman. No second person in foreground, midground, background, reflections, mirrors, screens, posters, glass, silhouettes, crowds, passers-by, drivers, shop staff, cyclists, or partial human body parts.
3. A request for `N` images means **exactly N independent image-generation calls and N separate image files**. Never satisfy `N` by asking the image model to create N panels on one canvas.
4. If the output contains more than one panel or more than one human, status is **AUTOMATIC FAIL — DISCARD AND REGENERATE**. Cropping a collage into pieces does not count as a valid fix; regenerate the failed image as a fresh single photograph.
5. Temporary contact sheets may be created only by a non-generative review tool after all individual files already exist, solely for internal/final audit. They are never accepted as generated outputs and never replace the independent files.
6. **Batch execution lock:** even if the user asks for 5, 10, or 100 images in one message, invoke the image generator for image 01 only; review it; then invoke image 02; and so on. Never phrase a single generation call as a request for multiple variants/images/panels.
7. **Readable-scene-text lock:** every accepted image must contain at least one short, coherent, readable Chinese environmental phrase physically present in the photographed world. Missing text, pseudo-Chinese, unreadable characters, or floating graphic text is a hard failure.


## RUNTIME SAFETY GUARD — STRICT BATCH MODE

This guard exists because some chat image-generation runtimes infer the image prompt from the full conversation and may reinterpret a batch request such as “generate 10 images” as a collage even when the Skill intends sequential calls. **Never claim strict compliance when the runtime cannot isolate each image call.**

### ChatGPT conversational image generator

When the active image tool infers generation intent from the full conversation and does not expose a fully isolated per-image prompt:

1. `N > 1` is **not a valid strict-batch execution mode inside one assistant turn**. Do not attempt repeated calls while the latest user request still semantically asks for multiple images; the tool may repeatedly create collages.
2. Strict mode requires **one user-visible generation turn per image**. The current turn must semantically request exactly one photograph (for example, “generate image 01 only” or “next single image”).
3. Never tell the user a multi-image batch is compliant if the runtime returned a collage or if independent files cannot be guaranteed.
4. If the user asks for 5/10/100 images in this runtime, explain the runtime limitation and use one of these safe paths:
   - ask them to proceed image-by-image in separate turns while retaining the batch plan; or
   - move the batch to a Work/Codex-style runtime that supports explicit isolated per-image generation calls and file saving.
5. A collage is not salvageable by cropping and never counts toward the requested total.

### Work/Codex or explicit-prompt runtime

If the runtime can pass an isolated explicit prompt for each generation call and save each result separately, execute the full batch automatically:

`plan row 01 → one explicit prompt → n=1 → save 01 → Gate 1 → accept/regenerate → row 02 → ... → final audit`.

The per-image prompt must never mention the total batch count, variants, grid, collection, series, contact sheet, or multiple images. It describes **only that one photograph**.

### Truthfulness requirement

Tool/runtime capability overrides aspiration. If strict one-file-one-photo output cannot be guaranteed in the active runtime, say so before generation rather than pretending the Skill can force behavior the tool does not expose.

## Load the standard

Before generating or editing anything, read these files completely:

1. [references/visual-standard.md](references/visual-standard.md)
2. [references/acceptance-review.md](references/acceptance-review.md)
3. [references/batch-plan-schema.md](references/batch-plan-schema.md)

Treat these assets as photographic-system references only:

- `assets/benchmark-outdoor.png`: outdoor directional-light reference.
- `assets/benchmark-indoor.png`: indoor window-light reference.

Never copy the benchmark identity. Never let repeated use of a benchmark collapse a batch into the same face, hairstyle, clothing cut, pose, or light.

## Mode A — Generate new images

### 1. Parse the request

Extract count, theme, scene constraints, wardrobe constraints, and requested left/right placement. Environmental Chinese text is a fixed requirement of this Skill and is not treated as optional overlay copy. If the request is otherwise complete, choose varied real-life scenes without asking questions.

### 2. Build and save a batch plan before generation

Create `batch-plan.json` using `references/batch-plan-schema.md`.

Every row must be deliberately unique in all of these dimensions:

- `subject_id` and facial identity descriptor
- face shape / feature cluster
- body-build descriptor within the approved natural range
- hairstyle
- top silhouette/style
- scene/backdrop
- action/prop
- top + leggings palette
- lighting preset/direction
- readable environmental Chinese text + physical sign/surface
- left/right third

For batches of 10 or fewer, do not repeat the exact hairstyle, top silhouette, scene, action/prop, full palette, lighting preset, or environmental sign text. Faces must always be different identities, regardless of batch size. Every plan row must include at least one short, coherent, readable Chinese phrase that naturally belongs to the scene.

When the user does not specify a side, alternate exactly: LEFT, RIGHT, LEFT, RIGHT…

### 3. Generate exactly one image per call and per file — ABSOLUTE

Use the built-in image generation tool. Pass both benchmark assets as photographic-standard references when the tool supports references.

**Never request a collage, contact sheet, diptych, grid, split screen, multi-panel layout, or multiple finished images inside one canvas. Never allow any additional human anywhere in the frame, including background figures, reflections, posters, screens, silhouettes, or partial bodies.** A request for 10 images means 10 independent generation calls and 10 independent image files.

Generate **sequentially, one call at a time**. Do not issue a single model request whose semantic instruction is “make 5 images”, “show 5 variations”, or anything that encourages a multi-panel canvas. Complete image 01 → inspect → accept/regenerate → save; only then move to image 02. Review cadence may summarize every two accepted images, but generation itself remains strictly one call → one file → one photograph.

### 4. Use the shared prompt + one plan row

Apply the shared prompt in `references/visual-standard.md`, then append the row-specific fields from `batch-plan.json`. Explicitly state that the subject identity must not resemble previously accepted subjects in the same batch.

### 5. Mandatory immediate acceptance review

After every generated image, perform the per-image audit in `references/acceptance-review.md`.

An image is **FAIL** and must be regenerated if any hard item fails. Do not count a failed image toward the requested total.

Important hard failures include:

- centered or near-centered subject
- more than one human anywhere in the visible frame, even tiny/background/reflected/partial
- same/near-same facial identity as an accepted batch image
- hairstyle repeated when the batch size is 10 or fewer
- top silhouette repeated when the batch size is 10 or fewer
- scene/action/palette/lighting preset repeated when the batch size is 10 or fewer
- cropped head or feet
- wrong viewpoint or obvious wide-angle look
- direct eye contact
- unreadably flat or blown lighting
- anatomy or clothing-opacity failures
- missing environmental Chinese text, unreadable/gibberish Chinese text, or text that looks like a digital overlay instead of a physical part of the scene
- watermark or unwanted branding failures

### 6. Mandatory cross-image review after each pair

After every two accepted images, compare the new pair against **all previously accepted images**, not only against each other. Check identity, hairstyle, top style, scene, action, palette, lighting, and composition side. If a repeated visual template is emerging, fail the newer image and regenerate it with a targeted correction.

### 7. Save accepted images

Use stable filenames:

`NN_场景_左侧三分之一.png` or `NN_场景_右侧三分之一.png`

The filename side must match the actual visual placement.

### 8. Run programmatic validation

Run:

```bash
python scripts/validate_batch.py OUTPUT_DIR --expected-count N --manifest batch-plan.json --strict
```

Fix every error before delivery. Programmatic checks supplement visual review; they do not replace it.

### 9. Mandatory final batch audit

Perform the complete whole-batch audit in `references/acceptance-review.md` and save `acceptance-report.md` beside the images.

Delivery is allowed only when:

- every image is individually PASS;
- the batch diversity audit is PASS;
- the programmatic validator is PASS.

If any image fails, regenerate only failed images and rerun both visual and programmatic audits.

### 10. Deliver

Deliver individual image files/links by default. Create a ZIP only when requested. Never replace independent files with a collage. A review-only contact sheet, if created outside the image generator, is secondary and never a deliverable substitute.

## Hard visual checks

Reject or redo an output when any condition fails:

- 3:4 vertical frame; prefer approximately 1080×1440.
- Exactly one human in the entire visible frame; that human is the intended adult subject.
- Subject visual center on LEFT x≈33% or RIGHT x≈67%, tolerance ±5 percentage points.
- **Center exclusion zone:** if the subject visual center falls anywhere from x=42% through x=58%, reject as centered.
- Keep the broader two-thirds side usable as negative space; movement/gaze should generally point into it.
- Complete body from hair to shoe soles; subject about 85–92% of frame height.
- Rear or three-quarter-rear candid view at waist/hip camera height with an 85–135mm telephoto look and shallow depth of field.
- At most half a side profile; no direct eye contact.
- Clearly adult Chinese woman aged 20–30 with realistic 7.5–8-head proportions and plausible anatomy.
- Hair at least shoulder length; use varied long-hair configurations across a batch.
- Natural athletic hourglass or pear-shaped silhouette; smooth, anatomically plausible clothing-covered form without exaggeration.
- Natural gait or documentary action; no theatrical/provocative pose.
- Directional environmental light with controlled highlights and dimensional shadows.
- Opaque, supportive, medium-thick matte fitted sportswear; no transparency, wet-look fabric, scrunch seams, logos, visible intimate anatomy, or impossible tailoring.
- Background secondary and softly blurred while retaining **at least one naturally placed, genuinely readable Chinese environmental phrase** on a physical scene element (shop sign, metro sign, door plaque, awning, wall notice, station sign, etc.).
- The environmental phrase should be short and realistic. Prefer plausible generic text such as `便利店`, `早餐店`, `水果店`, `手机维修`, `快递驿站`, `社区服务中心`, `物业服务中心`, `地铁站入口`, `A出口`, `停车场`, `生活超市`. If an exact real-world sign is not known, invent a plausible generic Chinese sign rather than producing nonsense glyphs.
- Environmental text is part of the photographed scene, never a caption/title/graphic overlay. No watermarks; avoid prominent third-party brand logos unless the user explicitly requests a real brand.

## Batch diversity hard rules

Faces are identities, not a style parameter. **Never reuse or intentionally clone the same face across a batch.**

For N ≤ 10:

- 10 images → 10 distinct subject identities.
- Exact hairstyle: no repeats.
- Exact top silhouette: no repeats.
- Scene/backdrop: no repeats.
- Action/prop: no repeats.
- Full color palette: no repeats.
- Lighting preset: no repeats.
- Environmental Chinese sign text: no exact repeats for N≤10.
- Composition side alternates unless user specifies otherwise.

For N > 10:

- Subject identity still never repeats.
- No exact hairstyle/top/scene/action/lighting preset/environmental sign text may appear in consecutive images.
- No exact non-identity attribute, including environmental sign text, should occupy more than 20% of the batch unless the user explicitly fixes that attribute.

Similarity rule: if two accepted images would reasonably be mistaken for the same photo shoot because face + hair + top + lighting + backdrop are substantially similar, the newer one fails even if individual metadata labels differ.

## Mode B — Reframe an approved existing image

When the image is already correct and the user only asks to move it to a left/right third:

1. Do not generatively redraw the person.
2. Extend only clean background on the destination's opposite side and crop the other side by the same width.
3. Preserve subject, clothing, pose, lighting, exposure, color, and original main-image pixels.
4. Choose the third that best follows gaze/movement direction and provides clean title space unless the user specifies a side.
5. Compare the unchanged overlap region pixel-for-pixel. Require zero changed pixels before delivery.

## Quality-control principle

The Skill is not complete when images merely “look similar to the benchmark.” It is complete only when the **photographic system is consistent while the batch content is deliberately varied**, and every output passes both per-image and whole-batch audits.
