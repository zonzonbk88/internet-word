"""The Internet in One Word — entry program.

Writes a single word describing the whole internet to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).

Entry word: "feral" — the internet, untamed: no owner, no off switch,
everyone shouting at once. Short enough to land in one beat, true of the
whole internet rather than one app, and surprising next to the obvious
picks (chaos, memes, endless).

Deterministic: no network, no randomness, no timestamps.
"""

import os


ENTRY_WORD = "feral"


def validate_entry(word: str) -> None:
    """Gate check: exactly one word, 1-30 chars, not only whitespace.

    One word means a single whitespace-free token: word.split() must
    return exactly one part, and the word must equal that part (no
    leading/trailing whitespace, no internal whitespace).
    """
    if not word or word != word.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if len(word.split()) != 1 or word.split()[0] != word:
        raise ValueError("entry must be exactly one word")
    if not 1 <= len(word) <= 30:
        raise ValueError("entry must be 1-30 characters")


def main() -> None:
    validate_entry(ENTRY_WORD)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the file holds exactly the word, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_WORD)


if __name__ == "__main__":
    main()
