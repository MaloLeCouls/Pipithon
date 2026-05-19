"""Le service paie veut trier des employés par salaire croissant, sans
écrire les méthodes de comparaison à la main.

Implémente `Employee` avec @dataclass(order=True) :
- `salary: int`  (le critère de tri -> en PREMIER),
- `name: str`    (NE doit PAS départager : field(compare=False)),
- sorted(list_d_employees) trie par salaire croissant.

Piège signalé : order=True compare dans l'ORDRE DE DÉCLARATION des
champs. Si name comptait, deux salaires égaux seraient départagés par
le nom — on l'exclut explicitement.
"""

from dataclasses import dataclass, field  # noqa: F401


class Employee:
    ...
