---
chapter: 3
title: "Dictionaries and Sets"
fluent_python_pages: "73-110"   # approx, éd. 2 O'Reilly 2022
tier: S
status: active
prereqs: [1, 2]
---

## Concepts clés (à drill)
- Dict comprehensions ; unpacking `**`, fusion `|` / `|=`
- `match`/`case` sur mappings
- `defaultdict` + `__missing__` (et la différence des deux)
- `Counter`, `ChainMap`, `OrderedDict`, `UserDict` (quand sous-classer `UserDict`)
- `types.MappingProxyType` (vue read-only)
- Vues dynamiques : `keys()`, `values()`, `items()`
- Hash tables, dicts compacts ordonnés (3.7+) — implications perf/ordre
- `set` / `frozenset`, opérations ensemblistes, set comprehensions
- Hashabilité : contrat `__hash__` / `__eq__`

## Pièges classiques
- Sous-classer `dict` et s'attendre à ce que `__getitem__` surchargé soit utilisé
  par les built-ins → préférer `UserDict`
- `__missing__` non appelé par `get()` / `__contains__`
- Muter un dict pendant l'itération sur ses vues → `RuntimeError`
- Clé non hashable (list) → `TypeError`
- `dict.setdefault` vs `defaultdict` (allocation inutile sinon)
- Set non ordonné : tester l'égalité d'ordre est faux

## Thèmes recommandés
`ecommerce` (panier/index SKU), `library` (index ISBN), `tasks`, `delivery`.

## Référence « checkpoint » niveau 5
Reproduire **`StrKeyDict0`** (`__missing__` : clés str/non-str cohérentes pour
`[]`, `get`, `in`) — cf. `fluentpython/example-code-2e` dossier `03-dict-set`.

## Lien PyMistral
Aucun (chap. < 8). `pymistral_link: null`. Thèmes concrets uniquement.
