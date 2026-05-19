---
chapter: 15
title: "More About Type Hints"
fluent_python_pages: "491-528"   # approx, éd. 2 O'Reilly 2022
tier: A
status: active
prereqs: [8]
---

## Concepts clés (à drill)
- `@overload` : signatures multiples cohérentes
- `TypedDict` (records typés type JSON)
- `typing.cast` (et pourquoi c'est un aveu, pas une preuve)
- Lecture des hints au runtime : `__annotations__`, `get_type_hints`
- Generic classes user-defined (`class Stack(Generic[T])`)
- Variance : covariance, contravariance, invariance (intuition)
- Generic static protocols

## Pièges classiques
- `@overload` sans implémentation concrète finale → erreur
- `cast` utilisé pour « faire taire mypy » au lieu de corriger le type
- `TypedDict` partiel vs total mal géré (`total=False`)
- Variance : container mutable invariant (mettre `list[Animal]` ≠ `list[Dog]`)
- `get_type_hints` qui échoue sur forward refs non résolues

## Thèmes recommandés
`llm-serving` (config de sampling `TypedDict` *fake*), `ml-pipeline`
(Batch générique), `monitoring`, `tasks`.

## Référence « checkpoint » niveau 5
Reproduire un **conteneur générique** type `LottoBlower`/`Tombola` paramétré
(`Generic[T]`) avec variance correcte — cf. `fluentpython/example-code-2e`
dossier `15-more-types`.

## Lien PyMistral
`pymistral_link: null`. Type hints avancés = codebases Mistral typées
(`mapping-mistral.md` Couche 1). Thèmes ML *fake* dominants (chap. > 14).
