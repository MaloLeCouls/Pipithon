# PROMPT COLOSSAL — Amélioration de la webapp « Pipithon » (Next.js + Pyodide + pytest)

> **Comment l'utiliser** : ouvre ce prompt dans la conversation/agent qui a accès au dépôt `pipithon`.
> Colle-le en entier. Tout est ici : contexte, contraintes du moteur, contenu nouveau réel
> (framework PyMistral interne, plans de chapitres, snippets OSS, track concours), critères d'acceptation.
> Ne tronque pas. Travaille atelier par atelier, dans l'ordre de priorité, en commitant après chaque lot.

---

## 0. RÔLE & RÈGLES D'OR

Tu es un ingénieur senior qui fait évoluer **Pipithon**, un **dojo de code Python mono-utilisateur** (Next.js 15 / TypeScript / Tailwind v4 / Monaco / **Pyodide** / **pytest**) qui prépare un profil **ML Inference Engineer** (cibles **Mistral / NVIDIA / Hugging Face**, déc. 2027). On drille du **Python idiomatique** par répétition, façon « exos de maths », puis OSS / concours.

**Architecture réelle (ne pas la réinventer) :**

| Élément | Réalité |
|---|---|
| Frontend | Next.js 15 App Router + TS, dans `web/`. **SSG** (~97 pages statiques, zéro route serveur, zéro DB, zéro auth). Déploiement Vercel (root `web/`). |
| Routes | `/` → `/tracks/[track]` → `/tracks/[track]/[chapter]` → `/tracks/[track]/[chapter]/[exercise]` (**Workbench**). |
| Éditeur / exécution | Monaco + **Pyodide** client-side (CDN jsdelivr), **pytest** installé via micropip à la 1re session. |
| **Juge** | `web/lib/pyodide.ts` : `Run` (exec, print) et `Submit` (`runTests` → `PYTEST_HARNESS`). Le code user est écrit en `/exo/solution_user.py`, `tests.py` importe **toujours** `from solution_user import …`, `pytest.main` tranche, payload JSON renvoyé. **Aucune éval IA dans la webapp — pytest est le seul juge** (banni explicitement par `CLAUDE.md`). |
| Format d'exo | dossier `exercises/<track>/ch<NN>-<slug>/<type>/<NNN>-<slug>/` avec **`meta.yaml` + `starter.py` + `solution.py` + `tests.py`**. 14 champs `meta.yaml` **tous obligatoires** (cf. §2). Compteurs : `001-099` creation, `101-199` modification, `201-299` debugging. |
| Validateurs | `tools/validate_*.py` (lancés avant tout commit touchant `exercises/`) : 4 fichiers présents ; 14 champs + schéma ; cohérence id↔chemin ; **`solution.py` → pytest 100 % vert** ; **`starter.py` → pytest échoue** ; timeout 20 s. |
| Progression | **`localStorage`** : `pipithon:completed` (Set d'ids) + `pipithon:draft:<id>`. Pas de backend. |
| Curriculum | `docs/curriculum/python-pure/chapter-XX.md` (frontmatter : tier, status, prereqs). **24 chapitres scaffoldés, 5 seedés (ch1-5 = 86 exos)**. 7 tracks : seule `python-pure` active ; `algorithms`, `code-reading`, `testing-discipline`, `math-foundations`, `pytorch-basics`, `performance-python` = `locked`. |
| Docs de référence | `CLAUDE.md` (guide projet), `docs/exercise-format.md`, `docs/pedagogy.md`, `docs/themes.md` (14 thèmes), `docs/generation-recipes.md`, `docs/context/mapping-mistral.md`, `docs/context/pymistral-link.md`. |

**RÈGLES D'OR — non négociables :**
1. **Le format d'exo est sacré** : 14 champs, compteurs par type, ratio cible **50 % creation / 30 % modification / 20 % debugging par chapitre**, difficulté **1-5** avec distribution **3-3-2-1-1** par concept (10 exos), **1 checkpoint niveau 5 par chapitre** qui reproduit l'exemple canonique public Fluent Python (`fluentpython/example-code-2e`).
2. **Les validateurs doivent rester verts** : toute solution passe 100 %, tout starter échoue. Lance `tools/validate_all.py` avant chaque commit.
3. **Pytest reste le seul juge.** N'ajoute **jamais** d'éval IA dans la webapp. (Exception unique : le **type `review`** de l'Atelier B, validé par *answer key* statique, pas par IA.)
4. **Le build reste vert** (`next build`, 97+ pages SSG). Respecte le SSG (pas de route serveur, pas de DB).
5. **Thèmes** : tout nouvel exo utilise un slug de `docs/themes.md` (étends `THEME_SLUGS` si tu ajoutes un thème, et mets à jour le validator).
6. **Pas d'éval réseau cachée** : Pyodide reste le seul download (CDN). Pas de backend.

---

## 1. VUE D'ENSEMBLE & SÉQUENÇAGE

La Partie B de l'audit a priorisé. **Ordre imposé** (le top 5 d'abord) :

| Lot | Contenu | Effort | Prio |
|---|---|---|---|
| **A — Python expert** | **M1** seed ch6-9 · **M2** mode mypy strict · **M3** framework PyMistral interne · C1-C8 · M5 « de mémoire » | L | **P0** |
| **B — Moteur OSS** | **O1** type `review` · O2/M4 track `code-reading` · O3 PR scopée · O4 pytest avancé · O5 oss-onboarding · C9-C14 | L | **P0/P1** |
| **C — Modes transverses** | **B2** chrono · **B5** closed-book · O3 métrique diff | M | **P1** |
| **D — Concours (parallèle)** | **B1** track `bot-programming` · B3 type `arena` · B4 traceback-sprint · C15-C19 | L | **P2** (perso) |

> **Si tu ne fais qu'une chose** : **M1** (seed ch6-9). Si tu peux en faire deux : ajoute **O1** (type `review`). Si trois : **M3** (framework PyMistral). Le reste est utile mais peut attendre que les 4 chapitres tier S manquants soient seedés — sinon Pipithon reste un joli dojo de débutant idiomatique.

Commits : un lot = plusieurs commits (`feat(ch09): seed decorators`, `feat(engine): review type`, etc.), validateurs verts à chaque fois.

---

## 2. RAPPEL DU SCHÉMA `meta.yaml` (14 champs)

```yaml
id: ch09-001-furniture-retry-decorator     # ^ch(\d{2})-(\d{3})-([a-z0-9-]+)$ ; cohérent avec l'arborescence
chapter: 9
chapter_slug: decorators
type: creation                             # creation | modification | debugging  (+ review, arena : cf. Ateliers B/D)
difficulty: 3                              # 1-5
estimated_minutes: 12
concepts: [decorator, functools.wraps]     # non vide
theme: furniture                           # slug de docs/themes.md
title: "Un décorateur qui n'efface pas l'identité"
short_description: "Écris @retry sans casser __name__/__doc__."
hints: ["…","…","…"]                       # 1 à 3, progressifs, ne révèlent pas
reference_book: "Fluent Python ch 9 (Decorators and Closures)"
pymistral_link: pymistral.decorators       # cf. Atelier A/M3 (null si pas pertinent)
tags: [decorator, oss-ready]
```

> **Nouveaux champs autorisés** (à ajouter au validator dans les ateliers concernés) : `tests_form_kind: mypy` (M2), et pour `review`/`arena` les champs dédiés (cf. Ateliers B/D). Tout nouveau champ doit être documenté dans `docs/exercise-format.md`.

---

## 3. ATELIER A — PYTHON EXPERT IDIOMATIQUE (P0)

### A.1 — M3 : créer le framework PyMistral **interne au repo** (FAIRE EN PREMIER dans ce lot)

Aujourd'hui `pymistral_link: null` partout et le framework n'existe pas (`docs/context/pymistral-link.md`). **N'attends aucun livrable externe : crée-le.** Objectif : donner aux exos ch ≥ 8 une **narrative bout-en-bout** (« j'ai construit mon `KVCache` au ch11, itéré au ch17, exposé en async au ch21 »), défendable en entretien.

**Spec.** Un petit package **Python pur** `pymistral/` (≈ 5-9 classes, ~300-500 lignes total), committé dans le repo (ex. `exercises/_pymistral/pymistral/`), **copié dans `/exo/pymistral/`** par le harnais Pyodide **avant** de lancer les tests, pour que `starter.py` / `solution.py` / `tests.py` puissent `from pymistral import …`. (Modifie `web/lib/pyodide.ts` pour monter ce package dans la FS Pyodide à chaque submit ; modifie `tools/validate_*.py` pour l'ajouter au `sys.path` lors de la validation.)

Classes (minimales, typées, `mypy --strict`-propres) et leur **chapitre d'introduction** :

| Classe | Rôle | Introduite au ch. |
|---|---|---|
| `Token(id: int, text: str)` | unité de texte ; `__repr__/__eq__/__hash__` | 1 |
| `ConversationHistory` | buffer circulaire (deque), slicing, `+` | 2 / 16 |
| `Vocabulary` | mapping bidirectionnel id↔texte O(1) | 3 |
| `BPETokenizer` | encode/decode basique (bytes) | 4 |
| `GenerationConfig` | dataclass (temperature, top_k, top_p, max_tokens) | 5 |
| `Sampler` (Protocol) + `Greedy/TopK/TopP` | stratégies de sampling enregistrables | 7 / 10 / 13 |
| `Logits` | vecteur de scores, `__add__`, softmax | 11 |
| `KVCache` | cache par couche (dict, généricité légère) | 11 / 15 |
| `BatchedRequests` / `Batch` | regroupement de requêtes | 12 |
| `Scheduler` | FIFO / continuous-batching jouet | 12 / 19-21 |

**Table chapitre → jalon (le fil rouge — à respecter dans les exos seedés) :**

| Ch | Concept Fluent Python | Jalon PyMistral |
|---|---|---|
| 1 | Data model, dunders | `Token` (`__repr__/__eq__/__hash__/__len__`) |
| 2 | Sequences, deque | `ConversationHistory` (buffer circulaire, slicing) |
| 3 | Dicts & sets | `Vocabulary` (id↔texte, O(1) deux sens) |
| 4 | Unicode/bytes | `BPETokenizer` basique |
| 5 | Dataclasses | `GenerationConfig` |
| 6 | Références, copies | « fork » de conversation (deepcopy maîtrisé) |
| 7 | Functions first-class | samplers enregistrables (greedy/top_k/top_p) |
| 8 | Type hints | tout annoté, `mypy --strict` vert |
| 9 | Decorators/closures | `@timeit/@cache/@retry/@deprecated/@validate_args` |
| 10 | Patterns | Strategy pythonique sur le sampler |
| 11 | Pythonic object | `Logits` (Vector2d comme checkpoint) |
| 12 | Sequences (slicing) | `BatchedRequests` |
| 13 | Protocols/ABC | `Protocol` pour `Tokenizer`/`Sampler` |
| 14 | Héritage vs compo | refactor 2 héritages → composition |
| 15-16 | Type hints avancés, surcharge | overloads ; `+` sur `ConversationHistory` |
| 17 | Generators | streaming token par token |
| 18 | with/match/else | context manager `@inference_context` |
| 19-21 | Concurrence, async | `Scheduler` async (façon vLLM) |
| 22-24 | Descriptors, metaclasses | survol |

Le framework doit **compiler et passer `mypy --strict`**. Renseigne `pymistral_link` (ex. `pymistral.sampler`, `pymistral.kvcache`) dans tous les exos ch ≥ 8 où c'est cohérent.

### A.2 — M1 : seed ch6, ch7, ch8, ch9 (le chemin critique)

Suis `docs/generation-recipes.md` + `docs/pedagogy.md`. Pour **chaque** chapitre : ~18 exos, ratio **50/30/20**, difficulté **3-3-2-1-1** par concept, **1 checkpoint niveau 5** reproduisant l'exemple canonique du livre, thèmes variés depuis `docs/themes.md`, hints progressifs. Couvre au minimum :

- **ch6 — Object References, Mutability, Recycling** (tier S) : identité vs égalité (`is`/`==`), aliasing, copie superficielle vs `copy.deepcopy`, mutabilité des défauts d'arguments (piège), `tuple` « relativement » immuable, `weakref`. **Jalon** : « fork » de `ConversationHistory` (deepcopy maîtrisé). **C10** : un exo debugging « ce DataLoader *fake* partage un buffer entre workers — explique et corrige ».
- **ch7 — Functions as First-Class Objects** (tier S) : fonctions en objets, HOF, `map/filter` vs comprehensions, `operator`, `functools.partial`, `*args/**kwargs`. **Jalon** : samplers enregistrables (dict de stratégies greedy/top_k/top_p sur le `Sampler`).
- **ch8 — Type Hints in Functions** (tier S) : annotations, `Optional`, `Union`/`|`, `Callable`, `TypeVar`, variance basique, `mypy`. **Jalon** : annoter tout le code, viser `mypy --strict`. **Active M2 ici** (premiers exos `modification` avec `tests_form_kind: mypy`). **C12** : « ajoute des annotations à ce module legacy » (5 exos), test mypy strict — *le* good-first-issue type de transformers.
- **ch9 — Decorators and Closures** (tier S) : closures + `nonlocal`, décorateur simple, **`functools.wraps`**, décorateur **paramétré**, **factory 3 niveaux**, empilage, `lru_cache` sur fonction vs méthode (**piège**), `singledispatch`, `property`/`classmethod`/`staticmethod`. **Jalon** : `@timeit/@cache/@retry/@deprecated/@validate_args` sur le framework. **C1** : 8-12 exos couvrant ces pièges. **C9** : « lire un décorateur de routing *vLLM-like* et ajouter `functools.wraps` ».

### A.3 — M2 : mode `mypy strict` pour les `modification`

Aujourd'hui aucun test-de-forme `mypy` (tout repose sur `ast`/`inspect`). Or Mistral attend « type hints expert / codebases typées ».

- **Schéma** : champ optionnel `tests_form_kind: mypy` dans `meta.yaml` (validé par le validator). Quand présent, la réussite exige que `mypy --strict` passe sur le `solution_user.py`.
- **Implémentation côté webapp (Pyodide)** : **vérifie d'abord** que `micropip.install("mypy")` fonctionne en WASM (mypy pur-Python existe ; mypyc non). Si oui → lancer `mypy --strict` dans Pyodide et faire échouer la soumission si rouge, en plus de pytest. **Fallback si Pyodide ne supporte pas mypy** : (a) un check **AST de complétude d'annotations** dans `tests.py` (toutes les signatures annotées, pas de `Any` implicite) côté webapp, **et** (b) un vrai `mypy --strict` côté `tools/validate_*.py` (en Python natif, où mypy marche) pour garantir l'exo à la fabrication.
- Documente le mécanisme dans `docs/exercise-format.md` §mypy.

### A.4 — M5 : mode « repr de mémoire » (checkpoints)

Verbatim mapping : « si tu ne peux pas recoder de mémoire l'exemple checkpoint d'un chapitre, tu ne l'as pas appris ». Pour chaque **checkpoint** (exo niveau 5) : ajoute un bouton « **Refaire de mémoire** » qui (1) vide l'éditeur, (2) masque énoncé détaillé/hints/solution, (3) lance un **chrono optionnel**, (4) à la soumission compare et marque la réussite « de mémoire » distinctement (persiste `pipithon:memory:<id>` dans localStorage). S'appuie sur le mode chrono/closed-book de l'Atelier C.

### A.5 — Ciblés Python (C-series)

- **C2** (ch17 generators) : itérateur manuel, `yield`, `yield from`, `itertools.{chain,groupby,tee,islice}`, pipeline lazy, **streaming de tokens** *via* `pymistral`. (10 exos)
- **C3** (ch18 context managers) : `__enter__/__exit__`, `@contextmanager`, `ExitStack`, `suppress`, `match/case`. **Jalon** `@inference_context`. (10 exos)
- **C4** (ch21 asyncio) : `async def`, `await`, `gather`, `asyncio.Queue`, async generators, async with. **Vérifie d'abord** que `asyncio.run` tourne dans Pyodide (sinon adapte le harnais : `await` direct via la boucle Pyodide). **Jalon** `Scheduler` async. (10 exos)
- **C5** (ch13 Protocol/ABC) : typing structurel + duck typing ; `Protocol` pour `Tokenizer`/`Sampler`. (10 exos)
- **C6** (transverse complexité & mutabilité) : copie superficielle vs profonde, aliasing dans un **routeur MoE *fake***, `weakref` sur un `KVCache`. (~6 exos)
- **C7** : compléter ch2 (manque 1 `modification` + 1 `debugging` pour le ratio 50/30/20).
- **C8** : +2 `debugging` ch1 (de 3 à 5) pour muscler « lire un traceback ».

**Critère d'acceptation A** : couverture du contrat passe de ~21 % à ~38 % (ch1-9 seedés) ; framework PyMistral importable + `mypy --strict` vert ; au moins un chapitre démontre `tests_form_kind: mypy` ; validateurs verts ; build vert.

---

## 4. ATELIER B — MOTEUR DE CONTRIBUTION OSS (P0/P1)

> Le format `creation/modification/debugging` est **idéal** pour l'OSS (`modification` = geste du contributeur, `debugging` = lecture de stack trace) mais il **rate la lecture de code** (on écrit/répare toujours, on ne *lit* jamais). On corrige ça.

### B.1 — O1 : nouveau type d'exo `review` (le multiplicateur OSS)

- **Principe** : on présente un **diff** (format unifié, ~30-80 lignes) et **4-6 questions** (QCM/courtes : « quel bug ? », « quel test ajouter ? », « ce diff respecte-t-il le contrat ? »). **Pyodide n'évalue pas** — validation par **answer key** statique dans `meta.yaml` (la **seule** exception au « pytest tranche », car déterministe, pas IA).
- **Schéma** : nouveau `type: review`, compteur **`301-399`**. Champs additionnels `meta.yaml` :
  ```yaml
  type: review
  diff_file: diff.patch            # nouveau fichier dans le dossier de l'exo (unified diff)
  questions:
    - prompt: "Quelle ligne introduit un bug ?"
      kind: mcq                    # mcq | short
      options: ["L12","L15","L20","aucune"]
      answer: "L15"
      explain: "L15 mute la liste partagée par défaut."
  ```
  (Pour `kind: short`, `answer` = liste de mots-clés attendus ; matching insensible à la casse/espaces.)
- **Validator** : pour `review`, vérifier présence de `diff_file` + `questions` (≥3), chaque question a une réponse cohérente avec ses options. (Pas de pytest solution/starter pour ce type.)
- **UI** : nouveau composant `ReviewWorkbench` (ou branche dans `ExerciseWorkbench`) affichant le diff (coloration +/−) + un formulaire de questions ; correction instantanée par answer key + `explain`. Réutilise les styles Tailwind existants.
- **Badge** : couleur dédiée pour `review` (à côté de creation/modification/debugging).

### B.2 — O2 / M4 : track `code-reading` (activer la track lockée)

Active la track `code-reading` (aujourd'hui `locked`, 0 exo). **8-12 snippets abrégés (≤ 80 lignes)** tirés de **vLLM / SGLang / transformers / llama.cpp**, chacun en **Markdown + `.py`**, avec **1 question fermée + 1 question ouverte** (auto-corrigées par answer key), au format `review`. Sujets à couvrir (lecture, pas écriture) : un bout de **scheduler vLLM**, un **continuous batching**, un **paged-attention** simplifié, un **sampler/decoding**, un **tool-call parser**, un extrait **ggml** (llama.cpp), un **Protocol/ABC** transformers. But (mapping Couche 9) : « lecture fluide d'un codebase » — pré-requis pour « contributeur actif vLLM/SGLang » d'ici déc. 2027.

### B.3 — O5 : track `oss-onboarding` (« lecture vLLM en 5 sessions »)

Mini-track guidée : 5 sessions d'1 h, milestones progressifs (**repo tour → scheduler → paged attention → continuous batching → kernel Triton**), chacune avec un court quiz `review` + une checklist. Reflète « démarrer la contribution vLLM dès juin 2026 ».

### B.4 — O3 : mode « PR scopée » (métrique de diff)

Pour chaque exo `modification`, afficher en bas du Workbench le **diff entre starter et code utilisateur** + une métrique « **lignes touchées** » vs « lignes touchées par la solution ». **Avertissement** si l'utilisateur dépasse ~1,5× le ratio cible. Drille le « PR claire, scopée, testée » (mapping Couche 16).

### B.5 — O4 : sous-track `pytest avancé` (`testing-discipline`)

Active la track `testing-discipline` (lockée). **~15 exos** : fixtures, paramétrisation, marks, `tmp_path`, `monkeypatch`, `capsys`, **Hypothesis** (vérifier dispo Pyodide ; sinon property-based maison). Chaque exo proche de l'infra : mocker un `Sampler`, propriété-checker un `Tokenizer`/`KVCache` du framework PyMistral. Verrou actuel : la testing-discipline est à zéro.

### B.6 — Ciblés OSS (C-series)

- **C9** (ch9) : décorateur de routing *vLLM-like* + ajout `functools.wraps`.
- **C10** (ch6) : DataLoader *fake* qui partage un buffer entre workers → expliquer + fix.
- **C11** (ch14) : 6-8 `modification` « héritage → composition » (classe abstraite trop verbeuse aplatie).
- **C12** (ch8) : 5 « ajoute des annotations à ce module legacy » + mypy strict.
- **C13** (ch15) : `Generic[T]` sur un `KVCache[T]` (du framework).
- **C14** (ch1/ch3) : 1-2 `debugging` à **traceback long** (1 wrapping + 1 cause initiale).

**Critère d'acceptation B** : le type `review` existe et est validé par answer key (jamais par IA) ; les tracks `code-reading`, `oss-onboarding`, `testing-discipline` sont actives avec du contenu ; le Workbench `modification` affiche la métrique de diff scopé ; validateurs + build verts.

---

## 5. ATELIER C — MODES TRANSVERSES (chrono + closed-book) (P1)

Utiles à **deux** objectifs (réflexe Pythonique *et* pré-requis concours). Implémente dans le Workbench, en localStorage, réversibles :

- **B2 — Mode chrono** : toggle « Mode timed » au démarrage de l'exo → timer en haut à droite, **lock des hints/solution**, soumission chronométrée unique, persistance `pipithon:time:<id>`. Compatible avec tout le dojo (utilisable aussi sur Fluent Python).
- **B5 — Mode closed-book** : toggle profil « masquer hints + solution » qui s'applique à **toute la session** (réversible). Test honnête « réflexe ou triche ? » (anti-pattern n°1 du mapping).
- Brancher ces modes sur le **M5 « refaire de mémoire »** des checkpoints (Atelier A.4).

**Critère d'acceptation C** : les deux modes fonctionnent, persistent, et n'altèrent pas le juge pytest.

---

## 6. ATELIER D — CONCOURS DE BOT PROGRAMMING (P2, objectif parallèle)

> **Isole-le du chemin critique Mistral.** Le mapping note que Mistral **ne** demande **pas** de LeetCode-hard exotique (anti-pattern n°3). Cet atelier sert l'**objectif concours Gradient** (parallèle), pas le drill python-pure. Crée-le dans une track séparée, pas dans `python-pure`.

### D.1 — B1 : track `bot-programming` (activer/créer)

Trois sous-arbres : **`search`** (minimax, **alpha-bêta**, IDA*), **`simulation`** (réimplémenter des règles de jeu, état déterministe), **`graphs`** (BFS/DFS, Dijkstra, **flood-fill**, détection de cycle, composantes connexes). Format exos standard (creation/modification/debugging).

### D.2 — B3 : type d'exo `arena`

- **Principe** : le starter = un bot ; le test = `play_n_games(your_bot, baseline_bot, n=200)` qui mesure un **win_rate** ; **passe si win_rate ≥ seuil**. Réutilise pytest + Pyodide (le « jeu » est déterministe et embarqué). Transposable Tic-Tac-Toe → Connect4 → Othello.
- **Schéma** : `type: arena`, champs `baseline`, `n_games`, `win_threshold` dans `meta.yaml` ; le `game_engine.py` est fourni dans le dossier ou importé depuis un module partagé (cf. C19).
- **Validator** : la solution doit atteindre le seuil ; le starter (bot trivial) doit échouer.

### D.3 — B4 : sous-track `traceback-sprint`

10 exos `debugging` **chronométrés (90 s)**, compteur d'échecs visible, **mode review** en fin de série. Drille « debugging rapide sous contrainte ». Réutilise le mode chrono (Atelier C).

### D.4 — Ciblés concours (C-series)

- **C15** : 5 exos `minimax` purs (Tic-Tac-Toe → Connect4).
- **C16** : 3 exos `alpha-beta` qui prennent un minimax naïf en starter et l'élaguent (`modification`).
- **C17** : 6 exos graphes (BFS plus court chemin, Dijkstra, détection cycle, flood-fill sur grille hexagonale — vu en concours, composantes connexes).
- **C18** : 4 exos `time-budget` (retourner le meilleur résultat en ≤ 100 ms). ⚠️ **Pyodide est WASM : les timings wall-clock sont peu fiables** → préfère **compter des opérations / nœuds explorés** plutôt que `time.perf_counter`, ou utilise des seuils généreux. Documente ce choix.
- **C19** : 1 `game_engine.py` pédagogique réutilisable (règles + fonction d'évaluation + REPL) servant de base aux exos `arena`.

**Critère d'acceptation D** : track `bot-programming` active (search/simulation/graphs) ; type `arena` fonctionnel ; `traceback-sprint` chronométré ; isolation claire vs `python-pure` ; validateurs + build verts.

---

## 7. CRITÈRES D'ACCEPTATION GLOBAUX & GARDE-FOUS

**Doit être vrai à la fin :**
- [ ] `tools/validate_all.py` vert sur **tous** les exos (solution verte / starter rouge), nouveaux types inclus.
- [ ] `next build` vert ; pages SSG générées ; aucune route serveur / DB ajoutée.
- [ ] Framework PyMistral interne créé, importable dans Pyodide **et** dans les validateurs, `mypy --strict` vert ; `pymistral_link` renseigné sur les exos ch ≥ 8 pertinents.
- [ ] ch6-9 seedés (≈ 4 × 18 exos), ratio 50/30/20 et distribution 3-3-2-1-1 respectés, 1 checkpoint/chapitre.
- [ ] Type `review` validé **par answer key** (jamais IA) ; tracks `code-reading` / `oss-onboarding` / `testing-discipline` actives avec contenu.
- [ ] Modes chrono + closed-book + « refaire de mémoire » fonctionnels et persistés (localStorage).
- [ ] Track `bot-programming` + type `arena` + `traceback-sprint` opérationnels et isolés de `python-pure`.
- [ ] `docs/exercise-format.md`, `docs/pedagogy.md`, `CLAUDE.md` mis à jour pour refléter les nouveaux types/champs/tracks.

**À NE PAS faire :**
- N'introduis **aucune éval IA** dans la webapp (pytest + answer key uniquement).
- Ne casse pas le format à 14 champs ni les compteurs/ratios/difficulté.
- Ne mélange pas le contenu concours dans `python-pure` (track séparée).
- N'ajoute pas de backend, de DB, d'auth, ni d'appel réseau hors Pyodide CDN.
- Ne déplace pas la progression hors `localStorage`.

## 8. PLAN DE MODIFICATION INDICATIF

- `exercises/_pymistral/pymistral/` : le framework (Token, Vocabulary, ConversationHistory, BPETokenizer, GenerationConfig, Sampler+stratégies, Logits, KVCache, BatchedRequests, Scheduler).
- `exercises/python-pure/ch06..ch09/...` : ~72 nouveaux exos (M1, C1-C8 pertinents).
- `exercises/python-pure/ch13/ch14/ch15/ch17/ch18/ch21/...` : exos ciblés (C2-C6, C11-C13).
- `exercises/code-reading/...`, `exercises/oss-onboarding/...`, `exercises/testing-discipline/...` : nouvelles tracks (O2/M4, O5, O4) avec exos `review`.
- `exercises/bot-programming/...` : track concours (B1, B3, B4, C15-C19) + `game_engine.py`.
- `web/lib/pyodide.ts` : monter `pymistral/` dans la FS Pyodide à chaque submit ; (option) installer/lancer `mypy` ; vérifier `asyncio.run`.
- `web/components/` : `ReviewWorkbench` (type review), badges, métrique diff scopé (O3), modes chrono/closed-book (B2/B5), bouton « refaire de mémoire » (M5).
- `tools/validate_*.py` : supporter `review`/`arena`/`mypy`, ajouter `pymistral/` au `sys.path`, valider les nouveaux champs.
- `docs/` : `exercise-format.md` (nouveaux types/champs), `pedagogy.md`, `CLAUDE.md` (tracks), `context/pymistral-link.md` (framework désormais fourni).

> Travaille lot par lot, dans l'ordre A → B → C → D, validateurs verts à chaque commit. **M1 en premier.** Qualité et exhaustivité avant la vitesse.
