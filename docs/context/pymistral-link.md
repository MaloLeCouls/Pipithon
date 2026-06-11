# pymistral-link.md — Framework désormais FOURNI (interne au repo, 2026-06-11)

**Statut : FOURNI.** Le framework `pymistral` est défini *à l'intérieur* du
repo (`exercises/_pymistral/pymistral/`). Décision actée lors du lot M3 de
l'atelier A (PROMPT_pipithon_upgrade) : on n'attend plus de livrable externe,
on construit le fil rouge nous-mêmes.

## Vue d'ensemble

Mini-framework d'inférence LLM **jouet**, Python pur (stdlib uniquement), pas
de vraie inférence : simulation déterministe pour donner aux exos `ch >= 8`
une narrative bout-en-bout (« j'ai construit mon `KVCache` au ch11, itéré au
ch17, exposé en async au ch21 »).

| Classe | Module | Chapitre d'introduction |
|---|---|---|
| `Token` | `pymistral.tokens` | 1 (data model) |
| `ConversationHistory` + `Turn` | `pymistral.history` | 2 (sequences) / 16 (overload) |
| `Vocabulary` | `pymistral.vocabulary` | 3 (dicts/sets) |
| `BPETokenizer` | `pymistral.tokenizer` | 4 (unicode/bytes) |
| `GenerationConfig` | `pymistral.config` | 5 (dataclasses) |
| `Logits` | `pymistral.logits` | 11 (Pythonic object, Vector2d-like) |
| `KVCache` | `pymistral.cache` | 11 / 15 (generics) |
| `Sampler` Protocol + `greedy_sampler` / `top_k_sampler` / `top_p_sampler` | `pymistral.sampling` | 7 (HOF) / 10 (patterns) / 13 (Protocol) |
| `Request`, `BatchedRequests` | `pymistral.batching` | 12 (sequences) |
| `Scheduler` | `pymistral.scheduler` | 12 / 19-21 (concurrence) |

Détail dans `exercises/_pymistral/README.md`.

## Comment l'importer dans un exo

```python
# starter.py / solution.py / tests.py — chapitre ≥ 8 typiquement
from pymistral import GenerationConfig, Logits, top_k_sampler
```

Mécanique :

- **Webapp (Pyodide)** : `web/scripts/build-pymistral.mjs` (prebuild) lit le
  paquet, sérialise en `web/lib/_pymistral-bundle.ts`. Au chargement Pyodide,
  `lib/pyodide.ts` écrit les fichiers sous `/exo/pymistral/`. `/exo` est déjà
  sur `sys.path` → `from pymistral import …` marche.
- **Validateur** (`tools/validate_exercise.py`) : copie le paquet dans le
  tmpdir avant `pytest`. L'absence du dossier est tolérée (pré-bootstrap).

## Champ `meta.yaml: pymistral_link`

- **Chap. < 8** : reste à `null` (pas de jargon ML avant ch8, règle d'or
  `themes.md`).
- **Chap. ≥ 8 où c'est cohérent** : valeur = dotted-path du module/symbole
  visé, ex. `pymistral.sampling`, `pymistral.kvcache`, `pymistral.scheduler.Scheduler`.
- **Chap. ≥ 8 sans lien narratif direct** : reste à `null`.

Le validateur accepte désormais `pymistral_link: null | <str>` (vérifié dans
`tools/validate_exercise.py`).

## À faire lors du seed ch6-ch9 (M1)

1. Ch6-7 (mutability, functions first-class) : pas de classe pymistral introduite
   *de force*, mais quelques exos peuvent prendre un objet pymistral existant
   (`ConversationHistory` deepcopy au ch6, samplers enregistrables au ch7).
2. Ch8 (type hints) : annotation d'extensions de pymistral. Premier vrai
   usage massif du framework.
3. Ch9 (décorateurs) : `@timeit`/`@cache`/`@retry`/`@deprecated`/`@validate_args`
   appliqués sur les fonctions de `pymistral.sampling`.

> Règle de progression des thèmes (rappel `INIT_PROMPT.md` §3.4) : chap. 1-7
> = thèmes concrets 1-10 ; thèmes 11-14 (proches LLM/ML) à partir du chap. 8,
> dominants après le chap. 14. `pymistral` *complète* ce pont thématique sans
> le remplacer.
