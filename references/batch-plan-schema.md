# Yujia V2.2 batch plan schema

Create `batch-plan.json` before generation.

## Required JSON structure

```json
{
  "skill": "yujia-v2-2",
  "count": 10,
  "alternate_sides": true,
  "one_file_one_photo": true,
  "one_human_per_photo": true,
  "images": [
    {
      "number": 1,
      "file_stub": "01_住宅公园_左侧三分之一",
      "side": "LEFT",
      "subject_id": "S01",
      "identity": "oval face; straight brows; narrow nose bridge; medium-light skin; tall/slender athletic frame",
      "hairstyle": "long loose waves",
      "top_style": "fitted short-sleeve crew-neck athletic top",
      "scene": "residential park path",
      "action_prop": "walking with folded light jacket",
      "palette": "warm ivory top + sage leggings + white shoes",
      "lighting": "tree-filtered directional daylight from camera-right",
      "environment_text": "社区服务中心",
      "text_surface": "small wall-mounted community office plaque in the background",
      "difference_from_previous": "first image"
    }
  ]
}
```

## Absolute batch-output invariants

- `one_file_one_photo` must be `true`.
- `one_human_per_photo` must be `true`.
- `count: N` means N independent generated image files, never N panels in one file.
- Every plan row assumes a scene with no other visible humans anywhere, including reflections/screens/posters/backgrounds.
- Every plan row must include non-empty `environment_text` and `text_surface`.
- `environment_text` must be a short, coherent, readable Chinese phrase that can plausibly exist in that scene. It may be generic/invented when exact real-world text is unknown.

## Planning rules

For N≤10, every value below must be unique across rows:

- `subject_id` (always unique at any N)
- `identity` (must describe a genuinely different person)
- `hairstyle`
- `top_style`
- `scene`
- `action_prop`
- `palette`
- `lighting`
- `environment_text`

`side` alternates LEFT/RIGHT unless the user explicitly specifies a side pattern. `text_surface` should vary naturally with scene type and must describe a physical object/surface, never a digital overlay.

Each `difference_from_previous` entry after image 01 must name at least three obvious differences from the immediately previous image, including at least one of identity/hairstyle/top and at least one of scene/lighting.

## Anti-token-variation rule

Do not pretend two rows are diverse by changing only adjectives. These pairs count as repeats:

- `sunny alley` vs `bright sunny alley`;
- `high ponytail` vs `high ponytail with loose strands`;
- `racerback tank` vs `racerback sport tank`;
- `left side sunlight` vs `warm left side sunlight`.

Use materially different visual categories.


## Environmental text examples

Use short phrases the image model has a realistic chance of rendering correctly. Prefer 2–6 Chinese characters when possible. Examples:

- 便利店
- 早餐店
- 水果店
- 鲜果
- 手机维修
- 五金店
- 快递驿站
- 社区服务中心
- 物业服务中心
- 地铁站入口
- A出口
- 停车场
- 生活超市

If a generated phrase is garbled, regenerate with a shorter phrase rather than accepting pseudo-Chinese.
