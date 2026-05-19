---
chapter: 23
title: "Attribute Descriptors"
fluent_python_pages: "863-894"   # approx, éd. 2 O'Reilly 2022
tier: B
status: optional
prereqs: [22]
---

## Concepts clés (à drill)
- Protocol descriptor : `__get__`, `__set__`, `__delete__`
- Data descriptor vs non-data descriptor (priorité de lookup)
- `property`/`classmethod`/`staticmethod`/méthodes **sont** des descriptors
- Storage de la valeur (par instance vs partagé) ; `__set_name__` (auto-naming)
- Ordre de lookup des attributs ; cas pratiques (validation, lazy, champs ORM)

## Pièges classiques
- Stocker la valeur sur le descriptor (partagé entre instances) au lieu de l'instance
- `__set_name__` non utilisé → nom d'attribut codé en dur / collisions
- Data vs non-data descriptor : croire qu'un attribut d'instance gagne toujours
- Descriptor défini sur l'instance et non sur la classe (ne se déclenche pas)
- Récursion via `instance.__dict__` mal manipulé

## Thèmes recommandés
`ml-pipeline` (champs validés *fake*), `ecommerce` (Quantity ≥ 0), `payroll`,
`monitoring` (Threshold bornée).

## Référence « checkpoint » niveau 5
Reproduire **`LineItem` + descriptor `Quantity`** (validation > 0, `__set_name__`,
storage par instance) — cf. `fluentpython/example-code-2e` dossier `23-descriptor`.

## Lien PyMistral
`pymistral_link: null`. Chapitre `optional` (INIT §3.1), tier B (culture :
ORM/configs ML). Thèmes ML *fake* dominants.
