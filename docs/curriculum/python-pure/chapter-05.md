---
chapter: 5
title: "Data Class Builders"
fluent_python_pages: "157-186"   # approx, éd. 2 O'Reilly 2022
tier: S
status: active
prereqs: [1]
---

## Concepts clés (à drill)
- `collections.namedtuple` (champs, `_fields`, `_asdict`, `_replace`, defaults)
- `typing.NamedTuple` (annoté, méthodes)
- `@dataclass` : `field`, `default_factory`, `__post_init__`, `frozen=True`,
  `order=True`, `kw_only`
- Comparaison des 3 approches (immutabilité, méthodes, typing, héritage)
- `__repr__`/`__eq__`/`__hash__` générés (et conditions du `__hash__`)
- « Data class comme code smell » : quand c'est légitime vs anémique

## Pièges classiques
- `default_factory` oublié : `field(default=[])` partagé entre instances (= mutable default)
- `frozen=True` + `__post_init__` qui veut écrire un champ → `FrozenInstanceError`
  (utiliser `object.__setattr__`)
- `eq=True, frozen=False` → `__hash__` mis à `None` (instance non hashable)
- `namedtuple` mutable attendu (il est immutable)
- Champ sans défaut après un champ avec défaut → `TypeError`

## Thèmes recommandés
`ecommerce` (LineItem, Invoice), `payroll` (Payslip), `delivery` (Address),
`library`. Records = cas d'usage naturel.

## Référence « checkpoint » niveau 5
Reproduire un **resource record `@dataclass`** type DublinCore (champs
optionnels, `default_factory`, `__repr__` propre) — cf.
`fluentpython/example-code-2e` dossier `05-data-classes`.

## Lien PyMistral
Aucun (chap. < 8). `pymistral_link: null`. Thèmes concrets uniquement.
