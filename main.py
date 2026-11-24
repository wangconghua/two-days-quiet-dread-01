#!/usr/bin/env python3
"""Two Days of Quiet Dread: one code review comment that approves a pull
request while carrying quiet existential dread.

The joke: the reviewer did the diligent thing (read it twice, found nothing)
and the only conclusion they draw is that the bug is hiding somewhere
quieter — the dread is the punchline, delivered flat, the way a tired
engineer would actually paste it before clicking approve.
"""

import os

COMMENT = "LGTM. Reviewed it twice, found nothing wrong, which only means the wrong thing is somewhere quieter."

OUT_PATH = "/output/entry.txt"

# Words that mark the comment as an approval, per the judge's first
# criterion: a single-line comment that approves the pull request.
APPROVAL_TOKENS = ("LGTM", "Approved", "Approve", "Ship it", "Looks good")


def validate_comment(text):
    """Fail loudly if the comment would lose on the judge's own criteria.

    Gate: 1-140 characters, one line, not only whitespace. Judge: it must
    approve the PR (criterion 1) and keep the dread quiet — flat tone, no
    exclamation, no melodrama (criterion 3). A future edit that breaks any
    of these should error here, not silently submit a losing entry.
    """
    if not (1 <= len(text) <= 140):
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if text.isspace() or "\n" in text:
        raise ValueError("entry must be a single non-blank line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not any(token in text for token in APPROVAL_TOKENS):
        raise ValueError("entry must approve the pull request")
    if "!" in text:
        raise ValueError("entry must keep the dread quiet: no exclamation")


def main():
    validate_comment(COMMENT)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(COMMENT)


if __name__ == "__main__":
    main()
