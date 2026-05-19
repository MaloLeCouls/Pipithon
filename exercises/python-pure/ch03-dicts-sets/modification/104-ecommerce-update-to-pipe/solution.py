"""Choix de design :
- `base | extra` exprime la fusion non destructive en une expression :
  nouveau dict, extra prioritaire sur clé commune, base intacte. Plus
  lisible que copy()+update() (deux étapes, une variable temporaire).
"""


def merge_pricing(
    base: dict[str, float], extra: dict[str, float]
) -> dict[str, float]:
    return base | extra
