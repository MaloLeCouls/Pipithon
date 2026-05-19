---
chapter: 12
title: "Special Methods for Sequences"
fluent_python_pages: "397-422"   # approx, éd. 2 O'Reilly 2022
tier: A
status: active
prereqs: [1, 11]
---

## Concepts clés (à drill)
- Construire une séquence custom complète et pythonique
- Protocol (duck) vs interface formelle
- `__getitem__` qui gère **`int` ET `slice`** (et renvoie le bon type)
- `__len__`, `__iter__`, `__contains__`
- `__getattr__` pour attributs dynamiques accessibles par nom (ex. `v.x`)
- `__hash__` d'une séquence (réduction via `functools.reduce` / `operator.xor`)
- `__eq__` robuste entre séquences

## Pièges classiques
- `__getitem__` qui ne préserve pas le type sur slice (retourne `list` au lieu de `Self`)
- `__getattr__` sans `__setattr__` cohérent → incohérence lecture/écriture
- `__hash__` qui ne combine pas tous les composants (collisions massives)
- Oublier `__len__` → `len()` casse alors que l'objet semble « séquence »
- `__getattr__` qui boucle (accès à un attribut inexistant en interne)

## Thèmes recommandés
`ml-pipeline` (Batch/Sample indexable *fake*), `delivery` (Route comme
séquence d'arrêts), `streaming` (Watchlist), `library`.

## Référence « checkpoint » niveau 5
Reproduire **`Vector`** multidimensionnel : `__getitem__` int+slice typé,
`__getattr__` (x/y/z/t), `__hash__` via reduce, `__eq__`, `__repr__` — cf.
`fluentpython/example-code-2e` dossier `12-seq-hacking`.

## Lien PyMistral
`pymistral_link: null`. Thèmes ML *fake* autorisés ; une séquence custom
indexable préfigure les structures `Batch`/`KVCache` (vocabulaire seulement).
