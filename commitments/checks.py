"""Plain-code checks shared by the incident skill and the scorers. No LLM."""

import re
from datetime import datetime, timedelta, timezone


def duration_value(text: str | None) -> tuple | None:
    """Comparable value for a duration, so PT72H equals P3D. None if unreadable."""
    if not text:
        return None
    text = text.strip()
    m = re.fullmatch(r"P(?:(\d+)Y)?(?:(\d+)D)?(?:T(?:(\d+)H)?)?", text)
    if m and any(m.groups()):
        years, days, hours = (int(g or 0) for g in m.groups())
        return ("hours", (years * 365 + days) * 24 + hours)
    m = re.fullmatch(r"(\d+)\s+(business days?|calendar days?|days?|hours?)", text.lower())
    if m:
        n, unit = int(m.group(1)), m.group(2)
        if unit.startswith("business"):
            return ("business days", n)
        return ("hours", n if unit.startswith("hour") else n * 24)
    return None


def add_duration(start: datetime, duration: str) -> datetime | None:
    """Deadline from a start time and a contract duration. Weekends are skipped
    for business days. Holidays are not, because no contract here lists them."""
    value = duration_value(duration)
    if value is None:
        return None
    unit, n = value
    if unit == "hours":
        # Through UTC, so a clock change inside the window cannot shift the result.
        return (start.astimezone(timezone.utc) + timedelta(hours=n)).astimezone(start.tzinfo)
    result = start
    while n:
        result += timedelta(days=1)
        if result.weekday() < 5:
            n -= 1
    return result


def contacts(text: str) -> set[str]:
    """Email addresses and phone numbers in a string, in comparable form."""
    found = set(re.findall(r"[\w.+-]+@[\w.-]+\w", text.lower()))
    phones = re.findall(r"\+?\d[\d\s().-]{7,}\d", text)
    return found | {re.sub(r"\D", "", p) for p in phones}
