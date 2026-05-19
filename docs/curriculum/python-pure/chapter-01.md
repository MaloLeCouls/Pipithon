---
chapter: 1
title: "The Python Data Model"
fluent_python_pages: "1-22"   # approx, éd. 2 O'Reilly 2022
tier: S
status: active
prereqs: []
---

## Concepts clés (à drill)
- `__repr__` vs `__str__` (qui appelle qui, fallback `repr` si pas de `str`)
- `__init__`, construction d'objet
- `__len__` et le protocole `len()`
- `__getitem__` (indexation, slicing, itération « gratuite », `in` gratuit)
- `__bool__` (et fallback sur `__len__`)
- `__abs__`, dunders numériques (`__add__`, `__mul__`) en survol
- Pourquoi « Pythonic » : `len(x)` au lieu de `x.len()` — émulation des built-ins
- Carte mentale des dunders par catégorie (container, numérique, callable, etc.)

## Pièges classiques
- `__repr__` sans guillemets autour des `str` (doit être ~évaluable / sans ambiguïté)
- Confondre `__repr__` (dev, non ambigu) et `__str__` (user) — définir le mauvais
- Implémenter `__getitem__` sans gérer `slice` → itération/`in` cassés sur tranche
- Oublier que `__getitem__(0..)` rend l'objet **itérable** sans `__iter__`
- `__bool__` qui retourne autre chose qu'un `bool`

## Thèmes recommandés
Concrets uniquement (chap. 1) : `furniture`, `library`, `ecommerce`. Pas de jargon ML.

## Référence « checkpoint » niveau 5
Reproduire **`FrenchDeck`** (`__len__` + `__getitem__` → deck itérable, sliçable,
`in`, `random.choice`, `sorted`). Cf. repo public `fluentpython/example-code-2e`
dossier `01-data-model`.

## Lien PyMistral
Aucun (chap. < 8). `pymistral_link: null`. Thèmes concrets uniquement.
Cf. `docs/context/pymistral-link.md`.
