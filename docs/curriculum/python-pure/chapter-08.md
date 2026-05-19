---
chapter: 8
title: "Type Hints in Functions"
fluent_python_pages: "245-292"   # approx, éd. 2 O'Reilly 2022
tier: S
status: active
prereqs: [7]
---

## Concepts clés (à drill)
- Gradual typing ; duck vs nominal vs structural typing
- `Any`, `Optional[X]`, `Union` / syntaxe `X | Y` (3.10+)
- Generics : `list[int]`, `dict[str, list[int]]`, `tuple[int, ...]` vs `tuple[int, str]`
- `Iterable` / `Sequence` / `Mapping` en paramètre (principe de Liskov : accepter large)
- `Callable[[Arg, ...], Ret]`
- `TypeVar` (génériques de fonction)
- `typing.Protocol` static vs `@runtime_checkable`
- `NoReturn` ; lecture de la sortie `mypy`

## Pièges classiques
- Annoter le paramètre en `list` alors que `Iterable` suffit (trop restrictif)
- `Optional[X]` oublié quand `None` est une valeur possible
- `def f(x: list = [])` : le mutable default reste un bug malgré l'annotation
- `tuple[int]` (1-uple) vs `tuple[int, ...]` (n-uple) confondus
- Croire que les hints sont vérifiés au runtime (ils ne le sont pas)

## Thèmes recommandés
Bascule : `ecommerce`/`tasks` (concrets) **+ introduction** de `llm-serving`,
`ml-pipeline` (fonctions de tokenisation/sampling *fake*, typées). Jargon ML
désormais autorisé (chap. ≥ 8).

## Référence « checkpoint » niveau 5
Reproduire **`show_count`** : fonction pluralisée entièrement annotée, validée
mypy strict — cf. `fluentpython/example-code-2e` dossier `08-def-type-hints`.

## Lien PyMistral
`pymistral_link: null` (framework non fourni). **Pont thématique ouvert** :
thèmes `llm-serving` / `ml-pipeline` autorisés (vocabulaire *fake*, aucune
classe PyMistral inventée). Cf. `docs/context/pymistral-link.md`.
