"""Choix de design :
- first, *middle, last = route : exprime exactement l'intention ; middle
  est garanti list (vide si len == 2), pas besoin de slicing manuel.
- Garde-fou explicite : un unpacking first/*middle/last exige >= 2
  éléments, sinon ValueError -> on le signale clairement plutôt que de
  laisser remonter un ValueError cryptique.
"""


def split_route(route: list[str]) -> tuple[str, list[str], str]:
    if len(route) < 2:
        raise ValueError("route trop courte")
    first, *middle, last = route
    return first, middle, last
