---
chapter: 20
title: "Concurrent Executors"
fluent_python_pages: "731-756"   # approx, éd. 2 O'Reilly 2022
tier: A
status: active
prereqs: [19]
---

## Concepts clés (à drill)
- `concurrent.futures` : `ThreadPoolExecutor`, `ProcessPoolExecutor`
- `Future` : `result()`, `done()`, exceptions ; `Executor.map`
- `as_completed` vs ordre de soumission
- vs threads/processes « à la main » (pourquoi le pool)
- Téléchargements parallèles (cas d'école), gestion d'erreurs par tâche
- Choisir thread pool vs process pool (I/O vs CPU)

## Pièges classiques
- Exception dans une tâche silencieuse tant qu'on n'appelle pas `.result()`
- `Executor.map` qui ré-ordonne / bloque sur le plus lent
- `ProcessPoolExecutor` avec fonction non picklable (lambda, closure)
- Sur-souscription : trop de workers → contention
- Oublier `with Executor(...)` → threads/process non nettoyés

## Thèmes recommandés
`gpu-cluster` (batch de Jobs *fake*), `delivery` (scans parallèles),
`monitoring` (collecte multi-probe), `ml-pipeline` (chargement de shards *fake*).

## Référence « checkpoint » niveau 5
Reproduire le **téléchargement de drapeaux** : version séquentielle vs
`ThreadPoolExecutor` + `as_completed` (mesure du speedup) — cf.
`fluentpython/example-code-2e` dossier `20-executors`.

## Lien PyMistral
`pymistral_link: null`. Thèmes ML *fake* dominants (chap. > 14).
