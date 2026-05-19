---
chapter: 16
title: "Operator Overloading"
fluent_python_pages: "529-556"   # approx, éd. 2 O'Reilly 2022
tier: B
status: active
prereqs: [11]
---

## Concepts clés (à drill)
- Règles & garde-fous de l'overloading en Python
- Unaires : `__neg__`, `__pos__`, `__abs__`, `__invert__`
- Binaires + **reflected** : `__add__` / `__radd__`, `__mul__` / `__rmul__`
- `return NotImplemented` (≠ `raise NotImplementedError`) pour déléguer
- Augmented : `__iadd__` (in-place vs création)
- Comparaisons riches : `__eq__`, `__lt__`… + `functools.total_ordering`

## Pièges classiques
- `raise NotImplementedError` au lieu de `return NotImplemented` → casse `a + b` symétrique
- `__eq__` défini sans `__hash__` → objet non hashable (rappel ch 11)
- `__iadd__` qui retourne `None` (oublier `return self`)
- Type checking trop strict dans `__add__` (refuse les types compatibles)
- `total_ordering` sans `__eq__` + un opérateur d'ordre

## Thèmes recommandés
`ml-pipeline` (addition de Batch/vecteurs *fake*), `monitoring` (somme de
Timeseries), `ecommerce` (Money), `furniture` (dimensions).

## Référence « checkpoint » niveau 5
Reproduire **`Vector` avec opérateurs** : `+`/`radd`, `*` scalaire/`rmul`,
`==`, `@` (matmul) avec `NotImplemented` propre — cf.
`fluentpython/example-code-2e` dossier `16-op-overloading`.

## Lien PyMistral
`pymistral_link: null`. Thèmes ML *fake* dominants (chap. > 14).
