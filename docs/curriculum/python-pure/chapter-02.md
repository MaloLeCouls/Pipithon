---
chapter: 2
title: "An Array of Sequences"
fluent_python_pages: "23-72"   # approx, éd. 2 O'Reilly 2022
tier: S
status: active
prereqs: [1]
---

## Concepts clés (à drill)
- Mutables (`list`, `bytearray`, `array`, `deque`) vs immutables (`tuple`, `str`, `bytes`)
- Container sequences vs flat sequences
- List comprehensions vs generator expressions (mémoire, lazy)
- Tuple comme record (positionnel) vs tuple comme liste immutable
- Unpacking : `a, b = ...`, `*rest`, `*` en appel, nested
- `match`/`case` sur séquences (capture, `_`, `*`)
- Slicing : objets `slice`, `[a:b:c]`, pas négatif, slice assignment, multidim
- `+` / `*` sur séquences et pièges de copie superficielle (`[[]] * 3`)
- `+=` / `*=` : mutable (in-place) vs immutable (rebind)
- `list.sort()` (in-place, retourne None) vs `sorted()` ; paramètre `key`
- `bisect` : recherche dichotomique, `insort` ; `array.array`, `deque`, `memoryview`

## Pièges classiques
- `lst = [[]] * 3` → 3 références au **même** sous-objet
- `a += b` sur tuple/str crée un nouvel objet (rebind), sur list mute en place
- `sort()` retourne `None` → `x = lst.sort()` perd la donnée
- Slice assignment avec un itérable de taille différente (change la longueur)
- Confondre `list.append` (1 élément) et `extend` (itère)
- Generator expression consommée une seule fois

## Thèmes recommandés
`furniture`, `delivery`, `ecommerce`, `library` (catalogues, commandes, files).

## Référence « checkpoint » niveau 5
Reproduire la **recherche + insertion ordonnée via `bisect`** (grades, table de
lookup) — cf. `fluentpython/example-code-2e` dossier `02-array-seq`.

## Lien PyMistral
Aucun (chap. < 8). `pymistral_link: null`. Thèmes concrets uniquement.
