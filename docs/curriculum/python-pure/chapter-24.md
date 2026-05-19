---
chapter: 24
title: "Class Metaprogramming"
fluent_python_pages: "895-934"   # approx, éd. 2 O'Reilly 2022
tier: B
status: optional
prereqs: [13, 22]
---

## Concepts clés (à drill)
- Classes = objets first-class
- Création dynamique : `type(name, bases, dict)`
- Class decorators
- `__init_subclass__` (hook moderne, souvent préférable aux metaclasses)
- Metaclasses : `type` comme métaclasse, métaclasse custom
- Quand metaclasses indispensables vs over-engineering
- Cas pratiques : registration, validation, frameworks (ORM, ABC)

## Pièges classiques
- Utiliser une metaclasse là où `__init_subclass__` / class decorator suffit
- Conflit de métaclasses en héritage multiple → `TypeError`
- `type(name, bases, ns)` avec `ns` mal construit (méthodes manquantes)
- Effet de bord à l'import (registration) difficile à tracer
- Croire que `__init_subclass__` est appelé pour la classe de base elle-même

## Thèmes recommandés
`ml-pipeline` (registry de composants *fake*), `monitoring` (registry de
métriques), `gpu-cluster`, `tasks`.

## Référence « checkpoint » niveau 5
Reproduire une classe **`Checked`** validée via `__init_subclass__`, puis sa
variante metaclasse équivalente (comparer) — cf.
`fluentpython/example-code-2e` dossier `24-class-metaprog`.

## Lien PyMistral
`pymistral_link: null`. Chapitre `optional`, **le plus dispensable** pour
l'angle ML (`mapping-mistral.md` : code metaclass-heavy rare en ML systems).
À générer en dernier.
