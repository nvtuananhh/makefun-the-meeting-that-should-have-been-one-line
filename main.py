"""The Meeting That Should Have Been One Line.

The program writes a single line to /output/entry.txt: the
one sentence that could have replaced an entire pointless
meeting, at most 200 characters.
"""

import os

MAX_CHARS = 200
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# One sentence, decided in the room and done: do it the way
# Sarah suggested in March. The sting lands on the last
# words — the meeting itself was the only thing still
# blocking it. After this line, no one could justify
# holding the meeting at all, and anyone who has sat
# through a useless one knows exactly how it goes: the
# decision was made months ago, the meeting was the delay.
LINE = "We're doing it exactly the way Sarah suggested in March, and this meeting was the only thing still blocking it."


def build_line():
    """Return the entry line, checked: one line, 1-200 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-200 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
