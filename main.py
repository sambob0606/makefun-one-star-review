#!/usr/bin/env python3
"""The One-Star Review of Something Essential entry.

Writes a single original deadpan one-star review (<=160 characters) of
sleep, an everyday essential, to /output/entry.txt. Stdlib only; no
network, no reads outside the repo.
"""

import os

REVIEW = (
    "One star. Sleep takes eight hours every night and returns me to the "
    "exact same problems, only now I am also late for them."
)
# The joke is a complaint filed in earnest against a thing that cannot be
# fixed. The grievance is true and daily: sleep eats a third of the day
# and hands the same problems back. The turn lands in the last few words
# ("only now I am also late for them") — the rest reads straight, the
# sting arrives at the end. One sentence, one joke, no exclamation marks,
# no winking. Well under 160 characters; no trailing newline in the file.


def main() -> None:
    text = REVIEW.strip()
    assert 1 <= len(text) <= 160, f"review is {len(text)} chars, must be 1-160"
    assert text.strip(), "review must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
