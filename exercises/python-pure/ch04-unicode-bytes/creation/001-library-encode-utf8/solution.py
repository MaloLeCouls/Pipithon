"""Choix de design :
- .encode("utf-8") explicite : on ne dépend pas de l'encodage par défaut
  de la plateforme (toujours utf-8 en pratique, mais l'expliciter est
  l'idiome robuste — surtout pour des données qui voyagent en binaire).
"""


def to_utf8(title: str) -> bytes:
    return title.encode("utf-8")
