---
chapter: 9
title: "Decorators and Closures"
fluent_python_pages: "293-322"   # approx, éd. 2 O'Reilly 2022
tier: S
status: active
prereqs: [7]
---

## Concepts clés (à drill)
- Syntaxe `@`, sémantique de remplacement de la fonction
- **Quand** Python exécute un décorateur (à l'import / définition)
- LEGB ; closures, variables libres ; `nonlocal`
- Décorateur simple (wrapper) ; `functools.wraps` (préserver métadonnées)
- Décorateurs paramétrés (factory à 3 niveaux)
- Décorateurs empilés (ordre d'application)
- `functools.lru_cache` / `cache`, `singledispatch`
- Décorateur de classe vs de fonction

## Pièges classiques
- **Late binding closure** : `[lambda: i for i in range(3)]` capture `i`, pas sa valeur
- Compteur en closure sans `nonlocal` → `UnboundLocalError`
- Oublier `functools.wraps` → `__name__`/`__doc__` du wrapper écrasés
- Décorateur paramétré : un niveau de fonction manquant
- `lru_cache` sur méthode → fuite mémoire (cache l'instance via `self`)
- Ordre des décorateurs empilés mal raisonné

## Thèmes recommandés
`tasks` (audit/timing), `ecommerce` (cache de prix), `monitoring`
(instrumentation), `llm-serving` (cache de prompts *fake*).

## Référence « checkpoint » niveau 5
Reproduire **`make_averager`** (closure avec `nonlocal`) **+ `clock`**
(décorateur paramétré + `wraps`) — cf. `fluentpython/example-code-2e` dossier
`09-closure-deco`.

## Lien PyMistral
`pymistral_link: null`. Thèmes ML *fake* autorisés (chap. ≥ 8) — décorateurs
ubiquitaires en PyTorch/vLLM/FastAPI (cf. `mapping-mistral.md` Couche 1).
