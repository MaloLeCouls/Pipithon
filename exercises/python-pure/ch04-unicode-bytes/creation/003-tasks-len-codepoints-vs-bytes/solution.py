"""Choix de design :
- len(title) compte les code points (ce que voit l'utilisateur, à peu
  près) ; len(title.encode("utf-8")) compte les octets (ce que coûte le
  stockage/réseau). Confondre les deux est LA méprise du chapitre.
"""


def sizes(title: str) -> tuple[int, int]:
    return len(title), len(title.encode("utf-8"))
