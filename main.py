#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — make.fun entry (pure stdlib).

Writes the one sentence a house cat would say in its own defence in the
five seconds after sweeping a glass off the table.
"""

import os

ENTRY = (
    "As the household's chief glass inspector, I can confirm it failed "
    "its drop test \u2014 the table is now certified free of unreliable "
    "glassware."
)


def main():
    line = ENTRY.strip()
    if not 1 <= len(line) <= 200:
        raise SystemExit("entry must be 1-200 characters, got %d" % len(line))
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(line)
    os.replace(tmp_path, path)
    # Re-read and re-validate what was actually written.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("written entry does not match the validated line")


if __name__ == "__main__":
    main()
