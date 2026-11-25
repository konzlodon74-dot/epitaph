#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — entry writer.

Gate: /output/entry.txt must be UTF-8, 1-150 characters, single line,
with no trailing newline. This script is deterministic and stdlib-only.
"""
import os


EPITAPH = "Hold my beer and watch this."


def validate(text):
    assert 1 <= len(text) <= 150, "length must be 1-150 characters"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    text.encode("utf-8")  # must be UTF-8 encodable
    return text


def main():
    line = validate(EPITAPH.strip())
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write as UTF-8, single line, no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
