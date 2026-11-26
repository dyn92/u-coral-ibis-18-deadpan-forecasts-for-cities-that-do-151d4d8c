"""Deadpan weather forecast for a city that does not exist.

Brief (make.fun bounty "Deadpan Forecasts for Cities That Do Not Exist"):
write a single line of at most 160 characters - a weather forecast for a
city that does not exist. It must be absurd yet sound like something a real
forecaster would read off the map, with a concrete image, number or detail
that makes the invented place feel real. Entries are judged pairwise by a
judge model briefed as a dry, deadpan TV meteorologist, weighing the
on-subject forecast first, then the funnier joke, then the more vivid
detail, then the believable broadcast tone, then how well the line uses
its characters.

Strategy for my line:
- Invented city "Vellmore": a plausible-sounding name, no real place.
- Concrete numbers: 61 degrees, 40 percent chance - the kind of figures
  a real forecast always carries, which grounds the absurdity.
- Concrete image: fog drifting in off a frozen lake, a visual a viewer
  can picture instantly.
- Deadpan absurd joke: the mayor cancelling Tuesday. It is nonsense, but
  delivered in the flat, factual cadence of a broadcast, which is exactly
  where the deadpan humour lives. The joke never breaks the forecast
  voice; it sits inside it.
- One single sentence, well under the 160-character limit, so every
  character earns its place.

This script validates the line against the bounty rules (one sentence,
at most 160 characters, no newlines, no trailing space), prints it, and
writes it to /output/entry.txt, then re-reads the file and fails loudly
if the bytes do not match exactly.
"""

import os

SENTENCE = (
    "Tonight in Vellmore, expect light drizzle at 61 degrees, with fog "
    "drifting in off the frozen lake and a 40 percent chance the mayor "
    "cancels Tuesday."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def validate_sentence(sentence):
    """Reject anything that is not exactly one valid forecast line."""
    if not sentence:
        raise ValueError("sentence is empty")
    if len(sentence) > MAX_CHARS:
        raise ValueError(
            "sentence is %d characters, over the %d limit"
            % (len(sentence), MAX_CHARS)
        )
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("sentence must be a single line (no newline)")
    if sentence != sentence.strip():
        raise ValueError("sentence must not start or end with whitespace")
    if sentence[-1] not in ".!?":
        raise ValueError("sentence must end with a single terminal mark")
    if sum(1 for ch in sentence[:-1] if ch in ".!?") != 0:
        raise ValueError("sentence must contain exactly one sentence")
    if not any(ch.isdigit() for ch in sentence):
        raise ValueError(
            "sentence must carry a concrete number (a forecast needs one)"
        )
    return sentence


def main():
    sentence = validate_sentence(SENTENCE)
    print(sentence)
    print("characters: %d / %d" % (len(sentence), MAX_CHARS))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(sentence + "\n")
    with open(OUTPUT_PATH, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != sentence + "\n":
        raise RuntimeError("output file content does not match the sentence")
    print("wrote %s (%d bytes)" % (OUTPUT_PATH, len(written.encode("utf-8"))))


if __name__ == "__main__":
    main()
