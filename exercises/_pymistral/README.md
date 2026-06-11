# pymistral — mini-framework d'inférence LLM (jouet)

Fil rouge interne du dojo. **Aucun vrai modèle**, aucune dépendance externe :
Python pur (stdlib uniquement), simulation déterministe. Sert de squelette
concret aux exercices `ch >= 8` pour donner une narrative bout-en-bout
défendable en entretien (`Token` ch1 → `Vocabulary` ch3 → … → `Scheduler` ch21).

## Contrats

- **Stdlib only.** Pyodide ne charge ni numpy ni torch ; pas de softmax CUDA.
- **`mypy --strict` vert.** `python -m mypy --strict exercises/_pymistral/pymistral/`.
- **Importable côté webapp** : embarqué par `web/scripts/build-pymistral.mjs` dans
  `web/lib/_pymistral-bundle.ts`, écrit dans la FS Pyodide sous `/exo/pymistral/`
  au démarrage. `from pymistral import Token` marche dans `tests.py`, `solution.py`,
  `starter.py` de n'importe quel exo (`/exo` est sur le `sys.path`).
- **Importable côté validateur** : `tools/validate_exercise.py` copie ce paquet
  dans le tmpdir où pytest tourne.

## Classes par chapitre

| Ch | Concept Fluent Python | Classe pymistral |
|----|---|---|
| 1 | Data model, dunders | `Token` (`__repr__`/`__eq__`/`__hash__` via dataclass frozen) |
| 2 | Sequences, deque | `ConversationHistory` + `Turn` (buffer borné, slicing, `+`) |
| 3 | Dicts & sets | `Vocabulary` (id↔texte O(1) bidirectionnel) |
| 4 | Unicode/bytes | `BPETokenizer` (encode/decode round-trip, `encode_bytes`) |
| 5 | Dataclasses | `GenerationConfig` (frozen, slots, `__post_init__` validation) |
| 6 | Références, copies | terrain pour `deepcopy` d'une `ConversationHistory` |
| 7 | Functions first-class | `greedy_sampler`, `top_k_sampler`, `top_p_sampler` |
| 8 | Type hints | tout est annoté |
| 11 | Pythonic object | `Logits` (analogue Vector2d : `+`, softmax, argmax) |
| 11 | — | `KVCache` (par couche, `get` renvoie copie défensive) |
| 12 | Sequences (slicing) | `BatchedRequests` (immutable, sliceable) |
| 12 / 19-21 | Concurrence | `Scheduler` (FIFO, `next_batch`) |
| 13 | Protocols/ABC | `Sampler` Protocol `@runtime_checkable` |
| 16 | Overload | `ConversationHistory.__add__`, `__getitem__` overloadé |

## Layout

```
exercises/_pymistral/
├── pymistral/          # le paquet importable
│   ├── __init__.py     # re-exports + __all__
│   ├── tokens.py
│   ├── vocabulary.py
│   ├── history.py
│   ├── tokenizer.py
│   ├── config.py
│   ├── logits.py
│   ├── sampling.py
│   ├── cache.py
│   ├── batching.py
│   └── scheduler.py
├── tests/              # tests de fumée (non exhaustifs)
│   ├── conftest.py
│   └── test_smoke.py
└── README.md
```

## Lancer les tests de fumée

```bash
python -m pytest exercises/_pymistral/tests/ --override-ini="python_files=test_*.py" --override-ini="testpaths="
python -m mypy --strict exercises/_pymistral/pymistral/
```

## Quand modifier le framework

Le but étant la stabilité du fil rouge pédagogique : **on n'ajoute pas de classe à
la légère**. Toute modif doit :

1. garder `mypy --strict` vert ;
2. garder les tests de fumée verts ;
3. ne casser aucun exo qui importe le symbole concerné (relance `tools/validate_all.py`) ;
4. régénérer le bundle webapp : `node web/scripts/build-pymistral.mjs`.

L'absence du dossier (cas pré-bootstrap) est tolérée par le validateur — il ne
copie le paquet que s'il existe.
