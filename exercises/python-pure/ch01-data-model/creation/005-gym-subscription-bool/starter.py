"""Une salle de sport veut écrire `if member.subscription:` pour savoir si
l'abonnement est encore valable.

Implémente la classe `Subscription` :
- `__init__(self, remaining_days: int)`.
- `__bool__` : vrai si et seulement si remaining_days > 0.
"""


class Subscription:
    def __init__(self, remaining_days: int) -> None:
        ...

    def __bool__(self) -> bool:
        ...
