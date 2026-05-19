"""Choix de design (l'idée du chapitre 4) :
- nfc_equal : normaliser NFC les DEUX opérandes puis == . Sans ça, deux
  chaînes identiques à l'œil mais composées différemment sont jugées !=.
- fold_equal : NFC puis casefold() puis == . casefold() est le pli
  agressif (pas .lower()) -> 'ß' == 'ss', etc. fold_equal accepte donc
  tout ce que nfc_equal accepte, plus les différences de casse.
- On réutilise nfc_equal de fait : même squelette, une étape de plus.
"""

import unicodedata


def _nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


def nfc_equal(a: str, b: str) -> bool:
    return _nfc(a) == _nfc(b)


def fold_equal(a: str, b: str) -> bool:
    return _nfc(a).casefold() == _nfc(b).casefold()
