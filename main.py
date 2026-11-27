#!/usr/bin/env python3
"""news-image-20261127 entry: copy the poster to /output/entry.png.

The poster is a newspaper front page summing up Friday 27 November 2026:
the Thanksgiving nor'easter postpones the 100th Macy's parade for the first
time ever by weather (moved to Saturday; 800,000 lose power), with Bangkok
refinery fire, Cairo tanker fire, Trump's new tariffs and Kyiv missile
strikes in the strip below. The image is pre-rendered and shipped in this
repository as entry.png; this program only copies it to the output path,
so both runs write byte-identical files. Standard library only.
"""
import hashlib
import os
import shutil

# The poster shipped with this entry, next to this file.
SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

# The grader sets MAKEFUN_OUTPUT_DIR; otherwise the harness writes to /output.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    """Copy the shipped poster to the harness output directory."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    target = os.path.join(OUTPUT_DIR, "entry.png")
    shutil.copyfile(SOURCE, target)
    # Verify the copy is byte-identical before reporting success.
    with open(SOURCE, "rb") as f:
        source_hash = hashlib.sha256(f.read()).hexdigest()
    with open(target, "rb") as f:
        target_hash = hashlib.sha256(f.read()).hexdigest()
    if source_hash != target_hash:
        raise SystemExit(f"integrity check failed: {target} != {SOURCE}")
    print("wrote", target)


if __name__ == "__main__":
    main()
