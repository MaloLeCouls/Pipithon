---
chapter: 22
title: "Dynamic Attributes and Properties"
fluent_python_pages: "829-862"   # approx, éd. 2 O'Reilly 2022
tier: S
status: optional
prereqs: [11]
---

## Concepts clés (à drill)
- Data attribute vs property (interface uniforme, pas de getter/setter explicites)
- `@property` + `@x.setter` ; property pour validation
- Dynamique : `__getattr__`, `__setattr__`, `__delattr__`, `__getattribute__`
- `__dir__` ; `vars()`, `dir()`, `__dict__`
- Computed attribute lazy / `functools.cached_property`

## Pièges classiques
- `__getattr__` qui appelle un attribut menant à une récursion infinie
- `__setattr__` qui ne délègue pas à `super().__setattr__` → attribut jamais stocké
- Confondre `__getattr__` (fallback) et `__getattribute__` (toujours appelé)
- `property` qui masque un attribut d'instance du même nom
- `cached_property` sur classe `__slots__` (pas de `__dict__` → échoue)

## Thèmes recommandés
`llm-serving` (config *fake* dérivée), `monitoring` (métrique calculée),
`ml-pipeline`, `ecommerce` (total calculé).

## Référence « checkpoint » niveau 5
Reproduire **`FrozenJSON`** (`__getattr__` qui explore un JSON imbriqué)
**ou** `LineItem` avec property validée — cf. `fluentpython/example-code-2e`
dossier `22-dyn-attr-prop`.

## Lien PyMistral
`pymistral_link: null`. Chapitre `optional` (INIT §3.1) mais tier **S** pour
l'angle ML (properties très utilisées). Thèmes ML *fake* dominants.
