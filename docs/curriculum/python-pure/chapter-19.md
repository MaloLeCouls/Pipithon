---
chapter: 19
title: "Concurrency Models in Python"
fluent_python_pages: "689-730"   # approx, éd. 2 O'Reilly 2022
tier: S
status: active
prereqs: [17]
---

## Concepts clés (à drill)
- Concurrency vs parallelism (définitions précises)
- Le GIL : ce qu'il bloque réellement, ce qu'il ne bloque pas
- Threads vs processes vs coroutines : trade-offs
- I/O-bound vs CPU-bound → quel modèle choisir
- Modèles d'exécution : séquentiel, threadé, multi-process, async
- Exemple comparatif « spinner » dans les styles
- free-threading (Python 3.13+) : ce que ça change conceptuellement

## Pièges classiques
- Croire que `threading` accélère du CPU-bound pur (GIL)
- Partager un état mutable entre threads sans verrou → race condition
- `multiprocessing` et objets non picklables → erreur au spawn
- Bloquer la boucle async avec un appel synchrone lourd
- Confondre « concurrent » et « parallèle »

## Thèmes recommandés
`gpu-cluster` (Workers/Jobs *fake*), `llm-serving` (Scheduler *fake*),
`monitoring` (probes concurrentes), `delivery`.

## Référence « checkpoint » niveau 5
Reproduire le **spinner** dans ses 3 implémentations (thread / process /
async) avec le même calcul bloquant — cf. `fluentpython/example-code-2e`
dossier `19-concurrency`.

## Lien PyMistral
`pymistral_link: null`. Base des serveurs d'inférence asynchrones
(`mapping-mistral.md` Couche 1, tier S). Thèmes ML *fake* dominants.
