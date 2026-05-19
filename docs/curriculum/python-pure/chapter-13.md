---
chapter: 13
title: "Interfaces, Protocols, and ABCs"
fluent_python_pages: "423-460"   # approx, éd. 2 O'Reilly 2022
tier: A
status: active
prereqs: [11]
---

## Concepts clés (à drill)
- Duck typing originel ; goose typing (ABC)
- `abc` : `ABC`, `@abstractmethod`, `register` (virtual subclass)
- `collections.abc` : `Iterable`, `Container`, `Sized`, `Hashable`, `MutableMapping`…
- `typing.Protocol` (PEP 544), `@runtime_checkable`
- Différence sémantique **ABC vs Protocol** (nominal vs structurel)
- Quand `isinstance` est légitime (controversé) vs duck typing

## Pièges classiques
- `@runtime_checkable` ne vérifie que la **présence** des méthodes, pas leur signature
- `register` ne force pas l'implémentation (pas de garde-fou)
- Sous-classer une ABC sans implémenter tous les `@abstractmethod` → `TypeError` à l'instanciation
- `isinstance(x, Sequence)` vrai pour str (piège fréquent)
- Protocol importé de `typing` vs ABC de `collections.abc` confondus

## Thèmes recommandés
`ml-pipeline` (DataLoader/Dataset comme Protocol *fake*), `monitoring`
(Probe/Metric interface), `delivery`, `tasks`.

## Référence « checkpoint » niveau 5
Reproduire l'ABC **`Tombola`** + sous-classes (`BingoCage`, `LottoBlower`,
`TomboList` via `register`) **ou** un `typing.Protocol` `runtime_checkable` —
cf. `fluentpython/example-code-2e` dossier `13-protocol-abc`.

## Lien PyMistral
`pymistral_link: null`. ABCs/Protocols = clé pour lire vLLM/transformers
(`mapping-mistral.md` Couche 1, tier S). Thèmes ML *fake* autorisés.
