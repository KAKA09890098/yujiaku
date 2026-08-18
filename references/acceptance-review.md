# Yujia V2.3 mandatory acceptance and review protocol

This protocol is a required execution stage. Generation is not finished until Gate 0 and all three acceptance gates pass.

## Gate 0 — Runtime eligibility

Before any batch generation:

- [ ] The active runtime can isolate a per-image prompt from the user's full batch request, **or** the user is issuing exactly one image request in the current turn.
- [ ] The current generation call semantically requests exactly one photograph.
- [ ] The call does not mention the total batch count, multiple variants, grid, collage, contact sheet, series, or multi-panel output.

If any item fails, strict batch status = `BLOCKED — DO NOT GENERATE AS A BATCH IN THIS TURN`. Explain the runtime limitation and switch to separate single-image turns or an explicit-prompt Work/Codex runtime.



## Gate 1 — Per-image hard acceptance

For every newly generated image, inspect it against the plan row and mark each item PASS or FAIL.

### A. File/output

- [ ] **Exactly one finished photograph in the file — no exceptions.**
- [ ] **No collage, grid, diptych, split-screen, contact sheet, tiled layout, storyboard, or multi-panel layout — no exceptions.**
- [ ] 3:4 portrait orientation.
- [ ] **At least one short Chinese environmental phrase is genuinely readable.**
- [ ] The readable text is physically part of the scene (sign/plaque/awning/metro sign/wall notice), perspective-correct, and naturally lit — not a caption or graphic overlay.
- [ ] The phrase is coherent Chinese, not malformed pseudo-Chinese or nonsense glyphs.
- [ ] No watermark, decorative border, floating headline, subtitle, or unintended brand logo.

### B. Subject count and adulthood

- [ ] **Exactly one human is visible anywhere in the entire frame — no exceptions.**
- [ ] That sole human is the intended clearly adult Chinese woman aged 20–30.
- [ ] No second human in foreground, midground, or background.
- [ ] No human in reflections, mirrors, glass, screens, posters, silhouettes, vehicles, or shop interiors.
- [ ] No partial extra human body/limb at any frame edge.

### C. Composition — hard geometry

- [ ] Full body visible from hair to shoe soles.
- [ ] Subject occupies about 85–92% of image height.
- [ ] LEFT image: subject visual center approximately x=28–38%.
- [ ] RIGHT image: subject visual center approximately x=62–72%.
- [ ] Subject visual center does **not** fall in x=42–58% center exclusion zone.
- [ ] Broad negative-space side remains usable and visually cleaner than subject side.
- [ ] Movement/gaze direction is compatible with open space where natural.

Any center-exclusion failure is automatic FAIL. Any multi-panel output or second-human presence is also automatic FAIL and must be discarded, not cropped into compliance.

### D. Camera and pose

- [ ] Rear or three-quarter-rear view.
- [ ] Waist/hip-height camera impression.
- [ ] 85–135mm telephoto compression; no obvious wide-angle stretching.
- [ ] At most half a side profile.
- [ ] No direct eye contact.
- [ ] Natural documentary action or gait; not theatrical/provocative.

### E. Identity and anatomy

- [ ] Facial identity is not the same or near-same as any previously accepted subject.
- [ ] Identity difference is structural, not merely changed hair/clothes.
- [ ] Natural adult proportions and plausible anatomy.
- [ ] Hands, feet, legs, joints, and torso look coherent.
- [ ] Clothing-covered silhouette is natural, smooth, and not exaggerated.

If reviewer thinks “this looks like the same woman again,” mark FAIL unless the user explicitly requested one recurring person.

### F. Hair and wardrobe

- [ ] Hair is at least shoulder length.
- [ ] Hairstyle matches the plan row.
- [ ] For N≤10, exact hairstyle has not appeared in any accepted image.
- [ ] Top silhouette matches the plan row.
- [ ] For N≤10, exact top silhouette has not appeared in any accepted image.
- [ ] Leggings and top are opaque, matte, supportive, and free of logos/scrunch seams.
- [ ] No visible intimate anatomy or impossible tailoring.

### G. Scene, action, palette, lighting

- [ ] Scene matches plan row and is not a repeated scene type for N≤10.
- [ ] Action/prop matches plan row and is not repeated for N≤10.
- [ ] Full palette matches plan row and is not repeated for N≤10.
- [ ] Lighting matches plan row and is not repeated for N≤10.
- [ ] Light is genuinely directional and dimensional, not the same default sun template repeated.
- [ ] Highlights are controlled; shadows preserve form; no washed-out or flat exposure.
- [ ] Background is secondary and softly blurred overall, but the planned environmental text region retains enough local clarity to be read.
- [ ] Environmental Chinese text matches the plan row and is not an exact repeat for N≤10.

### Gate 1 decision

If **any hard item** above is FAIL, image status = `FAIL — REGENERATE`.

Do not repair multiple unrelated failures with vague instructions. Regenerate with targeted corrections naming the failed dimensions, for example:

> Regenerate image 04 only. Keep the planned museum arcade scene and RIGHT-third composition. Replace the repeated high ponytail with the planned long single braid, replace the repeated racerback with the planned fitted short-sleeve crew-neck top, use window-right directional light, and ensure subject center x≈67%, outside the 42–58% center zone. Use a clearly different facial identity from images 01–03.

## Gate 2 — Cross-image diversity review

Perform after every two accepted images and again at the end.

Compare each new accepted candidate to all earlier accepted images across these dimensions:

| Dimension | N≤10 acceptance rule |
|---|---|
| Facial identity | zero repeats / near-repeats |
| Hairstyle | zero exact repeats |
| Top silhouette | zero exact repeats |
| Scene type | zero repeats |
| Action/prop | zero repeats |
| Full palette | zero repeats |
| Lighting preset | zero repeats |
| Environmental Chinese text | zero exact repeats |
| Composition side | alternate L/R unless user fixes side |

### Near-duplicate visual-template rule

Even when metadata names differ, FAIL the newer image if at least four of the following are substantially similar to an earlier accepted image:

- face/identity impression;
- hairstyle silhouette;
- top silhouette;
- body stance/gait;
- backdrop type/layout;
- lighting direction/quality;
- palette family;
- camera framing;
- environmental sign wording/surface.

The purpose is to stop “same model, same shoot, recolored leggings” outputs.

## Gate 3 — Final whole-batch audit

Before delivery:

1. Lay out the batch mentally or via a temporary contact sheet made **outside the image generator, for review only**. The contact sheet can never replace individual generated files and is not an accepted generation output.
2. Scan for a repeated face, hair silhouette, top cut, alley/street template, sun direction, body pose, framing template, or repeated environmental sign wording.
3. Confirm LEFT/RIGHT pattern from the plan.
4. Confirm every filename side matches actual placement.
5. Run the programmatic validator with strict mode.
6. Create `acceptance-report.md`.

### Required acceptance-report.md format

```markdown
# Yujia V2.2 Acceptance Report

Batch: <name>
Expected: <N>
Accepted: <N>
Programmatic validation: PASS/FAIL
Batch diversity: PASS/FAIL

| # | file | composition | identity | hair | top | scene | action | palette | lighting | readable scene text | anatomy/opacity | result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | ... | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |

## Cross-image duplicate audit
- Identity repeats: none / details
- Hairstyle repeats: none / details
- Top repeats: none / details
- Scene repeats: none / details
- Action repeats: none / details
- Palette repeats: none / details
- Lighting repeats: none / details
- Environmental text repeats/unreadable text: none / details
- Near-duplicate visual templates: none / details

## Final decision
PASS — deliver
```

If the final decision is not PASS, do not deliver the batch as complete. Regenerate only the failed files and rerun all three gates.
