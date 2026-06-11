"""Bug : annotation ment + pas de guard.
Fix : annonce `str | None`, branche sur is None.
"""
from __future__ import annotations


def driver_label(driver: str | None) -> str:
    if driver is None:
        return "unassigned"
    return driver.upper()
