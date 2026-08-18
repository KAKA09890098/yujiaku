# Yujia V2.2 visual standard

## Approved benchmark roles

- `../assets/benchmark-outdoor.png`: reference its full-body scale, long-lens compression, directional outdoor light, controlled exposure, hair-edge detail, pavement shadows, and depth.
- `../assets/benchmark-indoor.png`: reference its full-body scale, window-side light, controlled pale clothing, floor reflection, bright-but-not-washed background, and indoor depth.
- Never copy the exact identity, hairstyle, outfit cut, scene, objects, or pose from a benchmark unless the user explicitly requests that exact element.
- Across a batch, benchmarks define the photographic system, **not a recurring model/person**.

## Fixed image system

### Output and composition

- Produce one independent 3:4 vertical image, preferably around 1080×1440.
- **Absolute single-canvas rule:** one file contains exactly one photograph. Never generate a collage, grid, contact sheet, diptych, split screen, storyboard, tiled layout, or multiple panels in one canvas. This cannot be overridden by batch size.
- **Absolute single-human rule:** the whole visible photograph contains exactly one human being: the intended adult Chinese woman aged 20–30. No background people, crowds, passers-by, reflected people, people on posters/screens, silhouettes, drivers, cyclists, shop staff, or partial human limbs/bodies.
- Show that one woman from hair to shoe soles.
- Let the person occupy about 85–92% of image height.
- Put the person's visual center on the left or right vertical third:
  - LEFT target x = 33%, acceptable 28–38%.
  - RIGHT target x = 67%, acceptable 62–72%.
- Center exclusion zone: x = 42–58% is always a hard failure.
- Direct face, body, or movement toward the wider two-thirds negative space when natural.
- Keep the open side visually usable for optional editorial/title placement, but do not leave the whole environment textless: at least one readable Chinese environmental sign/label must exist naturally inside the photographed scene.
- Never default back to centered portrait composition.

### Camera

- Use an 85–135mm telephoto look with shallow depth of field.
- Shoot from behind or a three-quarter-rear angle.
- Keep camera height near the waist or hips.
- For clear natural body volume, prefer a 100–135mm look and a subtle 5–10-degree side offset from a straight rear view.
- Preserve natural perspective; forbid wide-angle stretching, extreme low angles, and top-down views.

### Lighting system — consistent quality, varied setup

Use real directional environmental light rather than uniform global illumination. Maintain the same quality standard, but do **not** reuse the same lighting setup throughout a batch.

Approved lighting preset families include:

1. morning side/back daylight from camera-left;
2. morning side/back daylight from camera-right;
3. tree-filtered directional daylight;
4. architecture-cut side light and open shade;
5. bright neutral open shade with directional bounce;
6. large-window light from left indoors;
7. large-window light from right indoors;
8. skylight + side-window mixed indoor light;
9. transit-hall window side light;
10. late-afternoon neutral side light without a strong golden filter.

For batches of 10 or fewer, use a different lighting preset for each image. For larger batches, never repeat a lighting preset consecutively and keep any one preset at or below 20% unless the user explicitly fixes lighting.

For outdoor scenes:

- Use directional side/back daylight, sometimes filtered by trees or architecture.
- Keep refined highlights on hair and clothing edges without a hard artificial rim.
- Let the background sit slightly darker than the subject when appropriate.
- Preserve real pavement, tree, or building shadows and restrained light patches.
- Avoid yellow filters, strong golden-hour stylization, gray overcast flatness, and blown highlights.

For indoor public spaces:

- Use large-window side light or side/back light with neutral ambient fill.
- Keep the space bright and transparent but recover window, floor, stone, and pale-fabric highlights.
- Preserve subtle shadow modeling on the subject and fabric.
- Avoid white haze, flat exposure, dramatic studio lighting, and excessive floor glare.

### Person identity and pose

- Every batch image must depict a **different adult woman identity** unless the user explicitly requests the same person.
- Do not use the benchmark face as a recurring identity.
- Plan identity variation with at least four changing descriptors: face shape, brow/eye character, nose profile, lip shape, skin tone, height impression, shoulder frame, or overall build.
- Do not merely change hair color or clothing on an otherwise identical face and count it as a new person.
- Use a natural young-adult presence aged 20–30 and documentary behavior.
- Keep realistic 7.5–8-head proportions, harmonious shoulders, waist, hips, and legs, and plausible anatomy.
- Use a naturally athletic hourglass or pear-shaped build with a defined but realistic waist-to-hip transition.
- Render clothing-covered lower-body form as smooth and anatomically connected, not exaggerated or segmented.
- Allow varied heights, builds, skin tones, and facial structures within the approved range.
- Keep hair at least shoulder length or longer.
- Hairstyle pool: loose straight hair, loose waves, low ponytail, high ponytail, braided ponytail, single long braid, half-up style, low bun with visible trailing length, high bun with visible trailing length, side braid, clipped half-up hair, long hair tucked behind one ear.
- For batches of 10 or fewer, do not repeat the exact hairstyle.
- Use natural actions such as walking, waiting, carrying flowers, tote, book, drink, documents, small shopping bag, luggage, umbrella, phone, or jacket.
- Prefer natural asymmetry and gait; no rigid mannequin stance.
- Show no more than half a side profile and forbid direct eye contact.
- Avoid theatrical posing, forced twisting, plastic skin, extreme retouching, and exaggerated proportions.

### Wardrobe — fixed category, varied silhouettes

The category stays fitted athletic wear, but top designs must vary across a batch.

Allowed opaque fitted top silhouettes include:

1. fitted long-sleeve crew-neck athletic top;
2. fitted long-sleeve half-zip athletic top;
3. fitted short-sleeve crew-neck athletic top;
4. fitted cap-sleeve athletic top;
5. wide-strap racerback athletic tank;
6. high-neck sleeveless athletic tank;
7. scoop-neck wide-strap athletic tank;
8. fitted mock-neck sleeveless athletic top;
9. fitted cropped long-sleeve athletic top with normal opaque back;
10. fitted cropped short-sleeve athletic top.

- For batches of 10 or fewer, do not repeat the exact top silhouette.
- Use high-waisted, full-length fitted yoga leggings.
- Use opaque, supportive, medium-thick matte performance fabric with realistic folds, tension, and tonal depth.
- Use a high-rise contoured waistband and subtle curved back yoke or shaping seam.
- Prefer light or bright leggings: warm ivory, cream, sand, light beige, blush pink, peach, coral, lavender, powder blue, mint, sage, butter yellow, light lilac, soft stone, pale teal.
- Use simple neutral sneakers.
- Forbid text/logos **on the clothing itself**, transparent fabric, wet-look fabric, scrunch seams, extreme compression, visible intimate anatomy, and anatomically impossible tailoring. Environmental Chinese signage in the scene is required separately.

### Waist-to-hip lighting and form

- Treat silhouette plausibility as a quality target equal to face, hands, and feet.
- Use broad soft side light or side/back light across the pelvis.
- Preserve highlight detail and subtle fabric shading in pale leggings; keep them opaque, matte, and dimensional rather than overexposed.
- Keep natural fabric tension at waistband, outer hip, and upper thigh so the garment reads as fabric, not painted skin.
- Reject flat rear illumination, symmetrical mannequin posture, lumpy segmentation, abrupt dents, or an oversized lower body disconnected from the torso.

### Background and scene diversity

Use real-life scenes such as:

- commercial street;
- airport concourse;
- train station passage;
- office colonnade;
- flower market;
- museum exterior or lobby;
- residential park;
- hotel arcade;
- café arcade;
- metro hall;
- botanical garden;
- riverside path;
- pedestrian bridge;
- community plaza;
- parking-building walkway;
- residential lane / urban village alley;
- convenience-store exterior with a readable Chinese shop-type sign;
- apartment lobby;
- covered walkway;
- waterfront promenade.

- For batches of 10 or fewer, do not repeat the same scene type.
- Keep background recognizable but secondary and softly blurred, while preserving one or more small areas of sufficient focus for environmental text to be genuinely readable.
- **Readable Chinese environmental text is mandatory in every generated photograph.** It must appear physically in the scene: storefront sign, awning, door plaque, metro/exit sign, wall notice, station board, parking sign, property-office plaque, etc.
- Prefer short, plausible real-life Chinese text. Examples: `便利店`, `早餐店`, `水果店`, `手机维修`, `快递驿站`, `社区服务中心`, `物业服务中心`, `地铁站入口`, `A出口`, `停车场`, `生活超市`, `鲜果`, `五金店`.
- When a real exact sign is not known or not needed, invent a plausible generic Chinese phrase that fits the scene. Do **not** invent fake claims about a real institution or use gibberish/pseudo-Chinese.
- Text must be environmental, perspective-correct, attached to a real physical surface, and lit consistently with the scene. Never place it as a floating caption, posterized headline, subtitle, border, or graphic overlay.
- If the generated Chinese text is malformed, nonsensical, duplicated unnaturally, or unreadable, the image fails and must be regenerated with a shorter/simpler phrase.
- Avoid prominent third-party brand marks and watermarks. Absolutely no other people anywhere in the frame.
- Render candid editorial/documentary photography rather than glamour, studio, fantasy, or pure-desire imagery.

## Batch diversity matrix requirements

Before generation, each planned row must specify:

- unique subject identity descriptor;
- unique hairstyle (N ≤ 10);
- unique top silhouette (N ≤ 10);
- unique scene type (N ≤ 10);
- unique action/prop (N ≤ 10);
- unique full palette (N ≤ 10);
- unique lighting preset (N ≤ 10);
- unique readable environmental Chinese sign text (N ≤ 10);
- the physical surface carrying that text (shop sign / metro sign / plaque / awning / wall notice etc.);
- alternating LEFT/RIGHT side unless user fixes it.

Do not accept cosmetic token changes as diversity. Example: “same face + same ponytail + same racerback + same alley + same sunlight, but leggings color changed” is a batch-diversity failure.

## Shared generation prompt

Use this block in every generation, then append the image-specific plan row:

```text
Use case: photorealistic-natural
Asset type: one independent 3:4 vertical WeChat image-post photograph
Input images: Image 1 and Image 2 are photographic-system references only. Match their natural adult proportions, full-body scale, 85–135mm telephoto compression, shallow depth of field, controlled directional environmental light, realistic opaque fitted sportswear, and strict rule-of-thirds composition. Do not copy their exact identities, hairstyles, clothing cuts, scenes, poses, or objects.

ABSOLUTE output rule: generate exactly one finished photograph in one file, with exactly one human visible anywhere in the entire frame: the intended adult woman. Do not create a collage, grid, diptych, split screen, contact sheet, tiled layout, storyboard, or multiple panels. Do not include background people, reflections of people, people on screens/posters, silhouettes, crowds, passers-by, drivers, cyclists, staff, or partial human body parts. If any second human or any multi-panel layout appears, discard the image and regenerate from scratch.

MANDATORY readable-environment-text rule: include at least one short, coherent, genuinely readable Chinese phrase physically integrated into the real scene. Put it on a plausible storefront sign, awning, metro/exit sign, door plaque, wall notice, parking sign, property-office plaque, or similar real surface. Prefer short realistic phrases such as “便利店”“早餐店”“水果店”“手机维修”“快递驿站”“社区服务中心”“地铁站入口”“A出口”“停车场”“生活超市”. If the exact real wording is unknown, invent a plausible generic Chinese sign. The text must be perspective-correct and lit as part of the environment, never added as a caption/title/subtitle/graphic overlay. If the Chinese characters are garbled, fake-looking, or unreadable, regenerate using a shorter phrase.

Shared standard: one clearly adult Chinese woman aged 20–30; realistic 7.5–8-head proportions; complete full body from hair to shoe soles and about 85–92% of frame height. Rear or three-quarter-rear candid viewpoint at waist/hip camera height. Place the subject on the specified vertical third: LEFT target x≈33% (28–38%) or RIGHT target x≈67% (62–72%). The subject visual center must not enter the 42–58% center exclusion zone. Orient face/movement toward the broad negative-space side where natural. At most half a side profile and no direct eye contact.

Identity diversity: this woman must be a different identity from every previously accepted subject in this batch. Vary facial structure and overall build, not merely clothing or hairstyle. Do not clone the benchmark face and do not reuse a prior accepted face.

Body and gait: naturally athletic adult build with realistic waist-to-hip transition and anatomically plausible clothing-covered form. Use natural documentary action and subtle asymmetry. No extreme proportions or provocative pose.

Wardrobe: use the plan row's specified fitted athletic top silhouette plus high-waisted full-length light/bright yoga leggings. Opaque, supportive, medium-thick matte performance fabric; natural folds and tonal depth; no logos, transparency, wet-look material, scrunch seam, or visible intimate anatomy.

Lighting: use the plan row's specified directional environmental-light preset. Keep controlled highlights, dimensional shadows, natural hair/fabric texture, and moderate exposure. The batch must not repeat the same lighting template.

Style: candid documentary/editorial lifestyle photography, tasteful, realistic, and anatomically natural.

Avoid: centered composition, repeated identity, repeated hairstyle, repeated top silhouette, repeated scene template, repeated lighting template, wide-angle distortion, cropped head or feet, direct eye contact, plastic skin, excessive retouching, impossible proportions, provocative pose, sheer fabric, visible intimate anatomy, blown highlights, flat light, **missing/unreadable/gibberish environmental Chinese text**, floating captions/titles/subtitles, watermark, decorative border, prominent unintended third-party brand marks, extra people, or any multi-panel layout.
```

Append these fields for each image:

```text
Image number: <NN>
Subject identity: <unique identity descriptor, clearly different from previous accepted subjects>
Scene/backdrop: <unique real-life scene with a natural physical surface for readable Chinese environmental text>
Hairstyle: <unique hairstyle for N<=10>
Top silhouette: <unique approved top silhouette for N<=10>
Action/prop: <unique natural action or object>
Composition: <LEFT or RIGHT vertical third; state target x and open-space side>
Color palette: <top, leggings, shoes; unique full combination for N<=10>
Lighting/mood: <unique lighting preset and direction for N<=10>
Environmental Chinese text: <short readable phrase; unique for N<=10>
Text surface: <shop sign / metro sign / door plaque / awning / wall notice / other physical surface>
Difference reminder: <name at least three obvious visual differences from the previous accepted image>
```

## Review

Every image and every batch must be reviewed using `acceptance-review.md`. The review is mandatory, not optional guidance.
