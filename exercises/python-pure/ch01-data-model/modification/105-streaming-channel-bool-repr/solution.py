"""Choix de design :
- __bool__ porte la sémantique 'live' : `if channel:` se lit naturellement
  et tout code conditionnel marche sans appeler une méthode maison.
- __repr__ encode l'état dans une forme non ambiguë : la branche offline
  est explicite plutôt que viewers=0 (intention claire en log/debug).
- is_live()/describe() supprimées : repr() + truthiness couvrent les besoins.
"""


class Channel:
    def __init__(self, name: str, viewers: int) -> None:
        self.name = name
        self.viewers = viewers

    def __bool__(self) -> bool:
        return self.viewers > 0

    def __repr__(self) -> str:
        if self:
            return f"Channel(name={self.name!r}, viewers={self.viewers})"
        return f"Channel(name={self.name!r}, offline)"
