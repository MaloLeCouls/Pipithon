"""Choix de design :
- errors="replace" : sur un flux d'étiquettes potentiellement corrompu,
  la robustesse prime sur la fidélité parfaite — on préserve le reste du
  texte et on marque les trous avec U+FFFD plutôt que de tout perdre sur
  une exception. (errors="ignore" effacerait silencieusement : moins bon
  pour le diagnostic.)
"""


def safe_decode(raw: bytes) -> str:
    return raw.decode("utf-8", errors="replace")
