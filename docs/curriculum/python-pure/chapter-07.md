---
chapter: 7
title: "Functions as First-Class Objects"
fluent_python_pages: "221-244"   # approx, éd. 2 O'Reilly 2022
tier: S
status: active
prereqs: [1]
---

## Concepts clés (à drill)
- Fonctions = objets (assignées, passées, retournées, stockées)
- Higher-order : `map`, `filter`, `reduce` et leurs alternatives idiomatiques
  (comprehensions, `sum`, `any`/`all`)
- `lambda` : usage légitime (clé de tri) et limites
- 9 flavors de callables ; objets callables via `__call__`
- Introspection : `__name__`, `__qualname__`, `__doc__`, `__defaults__`, `__code__`
- Paramètres : positionnels, keyword-only (`*`), positional-only (`/`), `**kwargs`
- `inspect.Signature` / `Parameter`
- `operator.itemgetter` / `attrgetter` / `methodcaller`
- `functools.partial`, `partialmethod`

## Pièges classiques
- `reduce` là où `sum`/`any`/`all`/comprehension est plus clair
- `lambda` nommée assignée à une variable (préférer `def`)
- `key=lambda x: x.attr` au lieu de `operator.attrgetter('attr')`
- `partial` qui fige un argument mutable
- Mélanger keyword-only / positional-only à mauvais escient

## Thèmes recommandés
`ecommerce` (stratégies de remise), `tasks` (tri/filtre), `delivery`
(callbacks de routage), `streaming` (recommandations).

## Référence « checkpoint » niveau 5
Reproduire **`BingoCage`** (objet callable via `__call__`) + introspection
d'une `factorial` (signature, defaults) — cf. `fluentpython/example-code-2e`
dossier `07-1class-func`.

## Lien PyMistral
Aucun (chap. < 8). `pymistral_link: null`. Dernier chapitre « concret pur » —
le pont thématique ML s'ouvre au chapitre 8.
