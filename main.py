"""One-line review of my own Monday, for the make.fun bounty
"Monday, Reviewed in One Line".

The whole entry is a single review line: a one-star verdict on my Monday,
with three concrete details — the 9 a.m. meeting that ran two hours, an
inbox at 47 unread, and office coffee that tasted like it had already
resigned. The script validates the line and drops it into /output/entry.txt.
"""

from pathlib import Path

# The review itself: one line, exactly 143 characters.
LINE = (
    "My Monday earned one star: the 9 a.m. meeting ran two hours, "
    "my inbox hit 47 unread, and the office coffee tasted like it "
    "had already resigned."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Strip and sanity-check the review; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"review must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if not text.endswith("."):
        raise ValueError("review must end with a full stop")
    return text


def main() -> None:
    text = validate(LINE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
