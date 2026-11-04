"""Verbatim quote check shared by the extractor and the scorer.

A quote is verbatim if it appears in the policy after both are normalized:
Markdown markup (bold, code ticks, table pipes, list bullets) is removed,
curly quotes become straight, and whitespace collapses. Words, numbers, and
punctuation must match exactly.
"""

import re

_MARKUP = re.compile(r"\*\*|__|`|\|")
_BULLET = re.compile(r"^\s*[-*]\s+", re.MULTILINE)
_SPACE = re.compile(r"\s+")
_CURLY = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"'})


def normalize(text: str) -> str:
    text = text.translate(_CURLY)
    text = _BULLET.sub("", text)
    text = _MARKUP.sub(" ", text)
    return _SPACE.sub(" ", text).strip()


def is_verbatim(quote: str, policy_text: str) -> bool:
    q = normalize(quote)
    return bool(q) and q in normalize(policy_text)
