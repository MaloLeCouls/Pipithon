---
chapter: 10
title: "Design Patterns with First-Class Functions"
fluent_python_pages: "323-340"   # approx, éd. 2 O'Reilly 2022
tier: B
status: active
prereqs: [7]
---

## Concepts clés (à drill)
- Strategy pattern : fonctions vs hiérarchie de classes (version pythonique)
- Refactor d'un pattern OO classique en first-class functions
- Command pattern simplifié (callable au lieu d'objet Command)
- Découverte dynamique de stratégies via `globals()` / introspection de module
- Choisir « le moins de code qui exprime l'intention »

## Pièges classiques
- Sur-ingénierie : créer une hiérarchie de classes là où une fonction suffit
- `globals()` non filtré → ramasse des callables non voulus
- Stratégie sans interface claire → couplage implicite
- État partagé entre stratégies « fonctions » via closure mal maîtrisée

## Thèmes recommandés
`ecommerce` (promotions/remises — le cas d'école), `tasks` (règles de tri),
`delivery` (stratégies de routage), `monitoring` (règles d'alerte).

## Référence « checkpoint » niveau 5
Reproduire le refactor **`Order` + promotions** : de classes `Promotion` vers
des **fonctions** + sélection de la meilleure via introspection — cf.
`fluentpython/example-code-2e` dossier `10-dp-1class-func`.

## Lien PyMistral
`pymistral_link: null`. Thèmes ML *fake* possibles (chap. ≥ 8), mais ce
chapitre reste bien servi par `ecommerce` (promotions).
