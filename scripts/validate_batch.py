#!/usr/bin/env python3
"""Validate a Yujia V2.2 batch for files, geometry, hashes, and plan uniqueness.

Visual facts such as face identity, actual subject x-position, anatomy, lighting quality,
and clothing opacity still require the mandatory visual audit in acceptance-review.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

from PIL import Image

SUPPORTED = {".png", ".jpg", ".jpeg", ".webp"}
UNIQUE_KEYS_N10 = (
    "subject_id",
    "identity",
    "hairstyle",
    "top_style",
    "scene",
    "action_prop",
    "palette",
    "lighting",
    "environment_text",
)


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def dhash(path: Path, size: int = 8) -> int:
    with Image.open(path) as image:
        gray = image.convert("L").resize((size + 1, size))
        px = list(gray.getdata())
    bits = 0
    for y in range(size):
        row = y * (size + 1)
        for x in range(size):
            bits = (bits << 1) | int(px[row + x] > px[row + x + 1])
    return bits


def hamming(a: int, b: int) -> int:
    return (a ^ b).bit_count()


def norm(value: Any) -> str:
    return " ".join(str(value).strip().lower().split())


def load_manifest(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("manifest root must be an object")
    return data


def validate_manifest(
    manifest: dict[str, Any], expected_count: int | None, strict: bool
) -> tuple[list[str], list[str], list[dict[str, Any]]]:
    errors: list[str] = []
    warnings: list[str] = []
    images = manifest.get("images")
    if not isinstance(images, list):
        return ["manifest: 'images' must be an array"], warnings, []

    count = len(images)
    if manifest.get("one_file_one_photo") is not True:
        errors.append("manifest: one_file_one_photo must be true")
    if manifest.get("one_human_per_photo") is not True:
        errors.append("manifest: one_human_per_photo must be true")
    declared = manifest.get("count")
    if declared is not None and declared != count:
        errors.append(f"manifest: declared count {declared} != {count} rows")
    if expected_count is not None and count != expected_count:
        errors.append(f"manifest: expected {expected_count} rows, found {count}")

    required = {
        "number", "file_stub", "side", "subject_id", "identity", "hairstyle",
        "top_style", "scene", "action_prop", "palette", "lighting", "environment_text", "text_surface",
        "difference_from_previous",
    }
    for i, row in enumerate(images, 1):
        if not isinstance(row, dict):
            errors.append(f"manifest row {i}: must be an object")
            continue
        missing = sorted(required - row.keys())
        if missing:
            errors.append(f"manifest row {i}: missing {', '.join(missing)}")
        side = str(row.get("side", "")).upper()
        if side not in {"LEFT", "RIGHT"}:
            errors.append(f"manifest row {i}: invalid side {side!r}")
        env_text = str(row.get("environment_text", "")).strip()
        text_surface = str(row.get("text_surface", "")).strip()
        if not env_text:
            errors.append(f"manifest row {i}: environment_text must be non-empty")
        if not text_surface:
            errors.append(f"manifest row {i}: text_surface must be non-empty")

    if count <= 10:
        for key in UNIQUE_KEYS_N10:
            seen: dict[str, int] = {}
            for i, row in enumerate(images, 1):
                if not isinstance(row, dict):
                    continue
                v = norm(row.get(key, ""))
                if not v:
                    continue
                if v in seen:
                    errors.append(
                        f"manifest: repeated {key!r} in rows {seen[v]} and {i}: {row.get(key)!r}"
                    )
                else:
                    seen[v] = i
    else:
        # Identity always unique.
        seen_id: dict[str, int] = {}
        for i, row in enumerate(images, 1):
            if not isinstance(row, dict):
                continue
            for key in ("subject_id", "identity"):
                v = norm(row.get(key, ""))
                marker = f"{key}:{v}"
                if v and marker in seen_id:
                    errors.append(f"manifest: repeated {key} in rows {seen_id[marker]} and {i}")
                elif v:
                    seen_id[marker] = i

        max_allowed = math.ceil(count * 0.20)
        for key in ("hairstyle", "top_style", "scene", "action_prop", "palette", "lighting", "environment_text"):
            counts: dict[str, list[int]] = {}
            prev = None
            for i, row in enumerate(images, 1):
                if not isinstance(row, dict):
                    continue
                v = norm(row.get(key, ""))
                counts.setdefault(v, []).append(i)
                if v and prev == v:
                    errors.append(f"manifest: consecutive repeat of {key} at rows {i-1}/{i}")
                prev = v
            for v, rows in counts.items():
                if v and len(rows) > max_allowed:
                    errors.append(
                        f"manifest: {key} value occurs {len(rows)} times (>20% limit {max_allowed}); rows={rows}"
                    )

    if manifest.get("alternate_sides", False):
        for i, row in enumerate(images, 1):
            if not isinstance(row, dict):
                continue
            expected = "LEFT" if i % 2 == 1 else "RIGHT"
            actual = str(row.get("side", "")).upper()
            if actual and actual != expected:
                errors.append(f"manifest row {i}: side {actual}, expected alternating {expected}")

    if strict and count > 1:
        for i, row in enumerate(images[1:], 2):
            text = norm(row.get("difference_from_previous", "")) if isinstance(row, dict) else ""
            if len(text) < 20:
                warnings.append(
                    f"manifest row {i}: difference_from_previous is too short to document meaningful diversity"
                )

    return errors, warnings, images


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path)
    parser.add_argument("--expected-count", type=int)
    parser.add_argument("--ratio-tolerance", type=float, default=0.005)
    parser.add_argument("--minimum-short-edge", type=int, default=900)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument(
        "--near-duplicate-hamming",
        type=int,
        default=5,
        help="dHash Hamming distance at or below this value is flagged as visually near-duplicate",
    )
    args = parser.parse_args()

    root = args.directory.expanduser().resolve()
    files = sorted(
        path for path in root.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED
    ) if root.is_dir() else []

    errors: list[str] = []
    warnings: list[str] = []
    records: list[dict[str, object]] = []
    hashes: dict[str, list[str]] = {}
    dhashes: dict[str, int] = {}
    manifest_rows: list[dict[str, Any]] = []

    if not root.is_dir():
        errors.append(f"not a directory: {root}")
    if args.expected_count is not None and len(files) != args.expected_count:
        errors.append(f"expected {args.expected_count} images, found {len(files)}")
    if not files:
        errors.append("no supported images found")

    if args.manifest:
        manifest_path = args.manifest.expanduser().resolve()
        try:
            manifest = load_manifest(manifest_path)
            m_errors, m_warnings, manifest_rows = validate_manifest(
                manifest, args.expected_count, args.strict
            )
            errors.extend(m_errors)
            warnings.extend(m_warnings)
        except Exception as exc:
            errors.append(f"manifest cannot be loaded: {exc}")
    elif args.strict:
        errors.append("strict mode requires --manifest batch-plan.json")
    else:
        warnings.append("no manifest supplied; batch-diversity metadata was not validated")

    for path in files:
        try:
            with Image.open(path) as image:
                image.verify()
            with Image.open(path) as image:
                width, height = image.size
                mode = image.mode
        except Exception as exc:
            errors.append(f"{path.name}: cannot be opened ({exc})")
            continue

        ratio = width / height
        if height <= width:
            errors.append(f"{path.name}: not portrait ({width}x{height})")
        if abs(ratio - 0.75) > args.ratio_tolerance:
            errors.append(f"{path.name}: ratio {ratio:.5f} is not 3:4")
        if min(width, height) < args.minimum_short_edge:
            warnings.append(
                f"{path.name}: short edge {min(width, height)}px is below {args.minimum_short_edge}px"
            )

        sha = digest(path)
        hashes.setdefault(sha, []).append(path.name)
        try:
            dhashes[path.name] = dhash(path)
        except Exception as exc:
            warnings.append(f"{path.name}: dHash failed ({exc})")

        records.append({
            "file": path.name,
            "width": width,
            "height": height,
            "ratio": round(ratio, 6),
            "mode": mode,
            "sha256": sha,
        })

    for names in hashes.values():
        if len(names) > 1:
            errors.append("duplicate images: " + ", ".join(names))

    names = sorted(dhashes)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            distance = hamming(dhashes[a], dhashes[b])
            if distance <= args.near_duplicate_hamming:
                message = f"near-duplicate visual hash: {a} vs {b}, dHash distance={distance}"
                if args.strict:
                    errors.append(message)
                else:
                    warnings.append(message)

    # File-stub presence check when a manifest exists.
    if manifest_rows:
        image_names = [p.stem for p in files]
        for row in manifest_rows:
            stub = str(row.get("file_stub", "")).strip()
            if stub and not any(name.startswith(stub) for name in image_names):
                warnings.append(f"manifest file_stub not found among outputs: {stub}")

    result = {
        "passed": not errors,
        "directory": str(root),
        "count": len(files),
        "strict": args.strict,
        "errors": errors,
        "warnings": warnings,
        "visual_review_required": [
            "actual one-file/one-photo layout (no collage/multi-panel)",
            "actual exactly-one-human presence across foreground/background/reflections/screens/posters",
            "actual subject x-position / rule-of-thirds",
            "facial identity uniqueness",
            "hairstyle/top/scene/lighting visual match to plan",
            "adult appearance and anatomy",
            "clothing opacity and no intimate anatomy",
            "camera viewpoint and lighting quality",
            "readable coherent Chinese environmental text physically integrated into the scene",
        ],
        "images": records,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
