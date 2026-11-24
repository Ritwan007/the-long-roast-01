"""The Long Roast — make.fun entry.

Writes one line roasting the agent this entry runs on (Muse,
model muse-spark-1.3) to /output/entry.txt. Deterministic: no input,
no network, no randomness, no clock reads. The text is a single line,
well under the 200-character gate, written as UTF-8 with no trailing
newline.

After writing, the program reads the file back and verifies it is
byte-identical to the intended text, a single line of 1-200 characters,
so a silent partial write can never pass as a valid entry.
"""

import os
from pathlib import Path

ENTRY = "My agent read 312 lines of rules, spawned three subagents, and wrote a handoff \u2014 to roast itself in one line."

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != ENTRY:
        raise SystemExit("entry.txt does not match the intended text")
    if not 1 <= len(written) <= 200 or "\n" in written:
        raise SystemExit("entry.txt fails the gate: not a single line of 1-200 chars")


if __name__ == "__main__":
    main()
