"""Choix de design :
- _norm = NFC puis casefold : casefold() gère les plis agressifs
  ('ß'->'ss', 'ı', etc.) là où lower() échoue ; NFC d'abord pour que les
  formes composées/décomposées coïncident. L'ordre (NFC puis casefold)
  est l'idiome recommandé pour une comparaison "caseless" robuste.
- On filtre en préservant l'ordre (comprehension sur titles).
"""

import unicodedata


def _norm(s: str) -> str:
    return unicodedata.normalize("NFC", s).casefold()


def search(titles: list[str], query: str) -> list[str]:
    q = _norm(query)
    return [t for t in titles if q in _norm(t)]
