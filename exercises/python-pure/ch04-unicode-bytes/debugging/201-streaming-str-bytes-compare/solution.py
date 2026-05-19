"""Correction :
- Bug : `received` est des bytes, `expected` une str. En Python 3,
  bytes == str vaut TOUJOURS False (types disjoints), sans exception
  -> faux négatif silencieux.
- Fix : décoder `received` (UTF-8) pour comparer deux str. (Encoder
  `expected` marcherait aussi ; on reste en str, plus lisible.)
"""


def is_expected(received: bytes, expected: str) -> bool:
    return received.decode("utf-8") == expected
