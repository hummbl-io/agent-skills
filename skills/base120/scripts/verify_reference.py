"""Verify this offline Base120 reference bundle using the standard library."""

import hashlib
import json
import sys
from pathlib import Path


def verify(root):
    metadata = json.loads((root / "references/source.json").read_text(encoding="utf-8"))
    for item in metadata["files"]:
        path = root / item["bundle_path"]
        # Git text exports normalize line endings; hash the pinned LF text bytes.
        raw = path.read_bytes().replace(b"\r\n", b"\n")
        if hashlib.sha256(raw).hexdigest() != item["sha256"]:
            raise ValueError("Reference hash mismatch: " + item["bundle_path"])
    operators = json.loads((root / "references/operators.json").read_text(encoding="utf-8"))
    families = ("P", "IN", "CO", "DE", "RE", "SY")
    expected = {family + str(i): family for family in families for i in range(1, 21)}
    if len(operators) != 120:
        raise ValueError("Reference must contain exactly 120 operators")
    seen = set()
    for op in operators:
        code = op["code"]
        if code in seen or expected.get(code) != op["transformation"]:
            raise ValueError("Invalid or duplicate operator: " + code)
        if not all(isinstance(op[k], str) and op[k].strip() for k in ("name", "definition")):
            raise ValueError("Empty operator name or definition: " + code)
        seen.add(code)
    if seen != set(expected):
        raise ValueError("Reference is missing canonical operator codes")
    return metadata


if __name__ == "__main__":
    try:
        source = verify(Path(__file__).resolve().parents[1])
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
    print("Verified 120 operators in six families at " + source["revision"])
