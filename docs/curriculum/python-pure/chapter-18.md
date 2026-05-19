---
chapter: 18
title: "with, match, and else Blocks"
fluent_python_pages: "637-678"   # approx, éd. 2 O'Reilly 2022
tier: S
status: active
prereqs: [9]
---

## Concepts clés (à drill)
- Context managers : `__enter__` / `__exit__` (valeur de retour, gestion exception)
- `contextlib` : `@contextmanager`, `closing`, `suppress`, `redirect_stdout`,
  `nullcontext`, `ExitStack`
- `try/else`, `for/else`, `while/else` (sémantique surprenante du `else`)
- `match`/`case` en profondeur : littéraux, capture, class patterns,
  séquences, mappings, OR (`|`), guards (`if`), wildcard (`_`)
- Quand `match` est idiomatique vs sur-utilisé

## Pièges classiques
- `__exit__` qui retourne `True` par erreur → exception avalée silencieusement
- `@contextmanager` sans `try/finally` autour du `yield` → cleanup non garanti
- `for/else` cru exécuté « si vide » (en fait : si pas de `break`)
- Class pattern `Point(x, y)` sans `__match_args__` → ne matche pas positionnellement
- `case [x]` qui matche aussi une str (séquence) de façon inattendue
- `match` avec `_` non final masquant des cases suivants

## Thèmes recommandés
`gpu-cluster` (allocation de ressources *fake*, context manager), `llm-serving`
(KVCache scope *fake*), `monitoring` (silence d'alerte), `tasks`.

## Référence « checkpoint » niveau 5
Reproduire **`LookingGlass`** (context manager qui inverse stdout via
`__enter__`/`__exit__`) **et** une variante `@contextmanager` — cf.
`fluentpython/example-code-2e` dossier `18-with-match`.

## Lien PyMistral
`pymistral_link: null`. Context managers = gestion ressources GPU/files
(`mapping-mistral.md` Couche 1, tier S). Thèmes ML *fake* dominants.
