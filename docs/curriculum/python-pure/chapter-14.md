---
chapter: 14
title: "Inheritance: For Better or For Worse"
fluent_python_pages: "461-490"   # approx, éd. 2 O'Reilly 2022
tier: B
status: active
prereqs: [11, 13]
---

## Concepts clés (à drill)
- `super()` : pourquoi il est subtil (coopératif, dépend du MRO)
- MRO et algorithme C3 ; `__mro__`
- Multiple inheritance, diamond problem
- Mixins : règles de design (petits, orthogonaux, suffixe `Mixin`)
- Sous-classer les built-ins (`list`/`dict`) : pourquoi c'est piégeux
- `__init_subclass__` (hook moderne)
- Composition > héritage : quand basculer

## Pièges classiques
- Appeler `Parent.__init__(self, ...)` au lieu de `super().__init__(...)` en MI
- Sous-classer `dict` et s'attendre à ce que `__setitem__` soit utilisé par `update`/`__init__`
- Diamond : `__init__` appelé deux fois ou jamais (MRO mal compris)
- Mixin qui suppose des attributs non garantis par la classe hôte
- Ordre des bases inversé → MRO inattendu

## Thèmes recommandés
`payroll` (types de contrats/employés), `gym` (abonnements), `delivery`
(véhicules), `tasks`. Garder concret malgré l'avancement.

## Référence « checkpoint » niveau 5
Reproduire un cas **multiple inheritance + mixin** type `UpperCaseMixin` /
`UpperDict` (effet du MRO sur les built-ins) — cf.
`fluentpython/example-code-2e` dossier `14-inheritance`.

## Lien PyMistral
`pymistral_link: null`. À partir d'ici les thèmes 11-14 (ML *fake*) deviennent
**dominants** (`themes.md` règle d'or) ; ce chapitre reste lisible sur `payroll`.
