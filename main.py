#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes the single v2.4.7 changelog line for this entry into the
directory MAKEFUN points at. The file holds exactly one line of
text with no trailing newline.
"""

import os
import sys


def build_entry():
    fragments = (
        'v2.4.7: Fixed a bug where the brain',
        'replayed your most embarrassing moment',
        'from 2009 every night, at the exact',
        'moment you tried to fall asleep.',
    )
    return ' '.join(fragments)


def main():
    entry = build_entry()
    size = len(entry)
    if size < 1 or size > 160:
        print("entry length out of range", file=sys.stderr)
        return 1
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    entry_path = os.path.join(target_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as out:
        out.write(entry)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
