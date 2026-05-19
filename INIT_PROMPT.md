# INIT — Webapp d'entraînement Python (Mistral track)

> **Pour Claude Code.** Lis ce prompt en entier avant de toucher au code. Pose tes questions de clarification *uniquement* sur ce qui est ambigu ici — sinon, suis les décisions déjà prises. La phase 0 doit se faire avant tout le reste.

---

## 0. Mission

Tu vas initialiser dans ce repo une webapp d'exercices de code dont **moi (l'utilisateur)** je suis la cible : je prépare un MS IA à Télécom Paris (rentrée sept 2026) avec objectif Mistral AI / NVIDIA Paris-Zurich / Hugging Face en décembre 2027 sur des postes ML Inference. Voir le fichier `Mapping_competences_ML_Inference_Mistral_dec2027.md` (déjà présent dans le contexte du projet Claude.ai mais **à recopier dans `/docs/context/` du repo dès la phase 0 — je te le fournis ci-dessous**).

**La webapp sert à drill du Python idiomatique, puis (plus tard) des maths ML, des algos, du PyTorch, du code reading open-source.** C'est un dojo personnel, pas un produit grand public.

**Le point clé** : le repo doit contenir *toute l'information nécessaire* pour qu'à n'importe quel moment je puisse t'ouvrir dans le terminal et te dire "génère-moi 5 exercices sur les decorators chapitre 9 thème entreprise de meubles" — et que tu produises immédiatement des exos cohérents, sans que je ré-explique le format, le ton, ou la pédagogie. **Ce repo est ton manuel d'opération.**

---

## 1. Décisions techniques (déjà prises — ne pas re-débattre)

| Choix | Décision | Raison |
|---|---|---|
| Frontend | Next.js 15 (App Router) + TypeScript | Standard, déployable Vercel gratuit |
| Style | Tailwind CSS + shadcn/ui | Rapide, propre, pas de design custom au début |
| Éditeur de code | Monaco Editor (`@monaco-editor/react`) | Même éditeur que VSCode, familiarité |
| Exécution Python | **Pyodide** (CPython compilé en WASM) chargé côté client | Zéro backend, sandboxé navigateur, suffisant pour Python pur |
| Tests | `pytest` exécuté dans Pyodide via `micropip.install("pytest")` | Standard, lisible, ce que j'utiliserai dans la vraie vie |
| Stockage progression | `localStorage` au début, schéma JSON | Pas de DB tant que je suis seul utilisateur |
| Stockage exercices | Fichiers YAML + .py dans le repo, scannés au build | Versionnés Git, éditables, générables par toi |
| Package manager | `pnpm` côté JS, `uv` côté Python (pour scripts tooling) | Les plus rapides 2025-2026 |
| Déploiement | Vercel (auto sur push `main`) | Gratuit, zero-config Next.js |
| Lint/format | Biome (JS/TS) + ruff (Python) | Modernes, rapides |

**Ne propose pas de Streamlit, Gradio, Flask, ou Anvil.** J'ai écarté.

**Ne propose pas Docker pour le dev local au début.** On verra plus tard.

---

## 2. Vision produit

### 2.1 Ce que je vois quand j'ouvre la webapp

Une sidebar gauche avec **les tracks** (au lancement, une seule active : `python-pure`), chaque track contenant des **chapitres**, chaque chapitre listant ses **exercices**. Un exercice cliqué ouvre une vue 3 panneaux :

```
┌──────────────────────────────────────────────────────────────┐
│  Header : titre exo · type · difficulté · concepts ciblés    │
├────────────────────────┬─────────────────────────────────────┤
│                        │                                     │
│  Énoncé (markdown)     │   Monaco editor (code starter)      │
│  + indices à révéler   │                                     │
│  progressivement       │                                     │
│  + lien chapitre       │                                     │
│  Fluent Python         ├─────────────────────────────────────┤
│                        │   [ Run ]   [ Submit ]              │
│                        │                                     │
│                        │   Console / résultats pytest        │
│                        │   (verts/rouges par test)           │
└────────────────────────┴─────────────────────────────────────┘
```

### 2.2 Comportement des boutons

- **Run** : exécute le code de l'utilisateur dans Pyodide, affiche stdout/stderr/erreurs. Ne lance **pas** les tests. Sert juste à tester du code rapidement.
- **Submit** : lance la suite `tests.py` via pytest. Affiche test par test : ✅ pass / ❌ fail avec message d'erreur. Si tous verts → confettis discrets + bouton "voir solution" + bouton "exercice suivant" + mark `completed` en localStorage.
- **Reveal hint** (bouton tertiaire) : révèle les indices un par un. Chaque exercice a 1 à 3 hints progressifs.
- **Voir solution** : *grisé tant que pas submit réussi OU tant que pas 3 tentatives échouées*. Diff visuel (côte à côte) ma solution vs la solution référence.

### 2.3 Progression visible

Sur chaque chapitre : barre `X/N exercices complétés`. Sur chaque track : barre globale. Pas de gamification lourde (pas de badges, pas de XP) — juste des compteurs sobres.

### 2.4 Ce qu'on NE fait PAS au MVP

- Pas d'auth, pas de comptes (mono-utilisateur, je suis tout seul).
- Pas de partage social.
- Pas de leaderboard.
- Pas de mode dark/light toggle au lancement (dark only suffit).
- Pas d'export PDF, pas de stats avancées.
- **Pas d'IA dans la webapp pour évaluer le code.** Les tests pytest tranchent. Point.

---

## 3. Pédagogie (le cœur — à graver dans le CLAUDE.md du repo)

### 3.1 Tracks

Au lancement, **une seule track active** :

- **`python-pure`** : couvre Fluent Python (Ramalho, 2e éd), chapitres 1 à 21. Chapitres 22-24 (descriptors, metaclasses) sont marqués `optional` dans le repo, exercices à générer plus tard.

Tracks à **scaffolder vides** dès la phase 0 (dossiers + README "à venir") pour que l'archi montre la trajectoire :

- `math-foundations` (algèbre linéaire, calc, probas — avec numpy plus tard)
- `algorithms` (NeetCode patterns en Python)
- `pytorch-basics` (tensors, autograd, nn.Module)
- `performance-python` (cProfile, line_profiler, optimisations)
- `code-reading` (lire un snippet de vLLM/transformers/llama.cpp, répondre à des questions sur ce que ça fait)
- `testing-discipline` (pytest avancé, fixtures, hypothesis)

### 3.2 Les 3 types d'exercices

Chaque chapitre doit avoir des exercices des 3 types, dans un ratio recommandé **50% creation / 30% modification / 20% debugging** (sur l'ensemble du chapitre, pas par concept).

#### Type A — `creation`

L'utilisateur écrit du code from scratch à partir d'un starter quasi vide (signatures de fonctions/classes avec `pass` ou `...` et une docstring décrivant le contrat). Tests à faire passer.

#### Type B — `modification`

Le starter contient du code **qui fonctionne mais imparfait** : trop verbeux, non-idiomatique, lent, mal typé, sans dunders, etc. La consigne demande un refactor précis (ex: "réécris cette boucle en list comprehension", "ajoute `__repr__` et `__eq__`", "remplace l'héritage par de la composition", "type-annote toute la fonction"). Les tests vérifient que **le comportement est préservé** ET que **le refactor est appliqué** (par ex. via `ast.parse` qui inspecte le code pour vérifier la présence d'un `ListComp` au lieu d'une `For`, ou via mypy).

Ce type prépare au travail de PR open-source : lire du code existant, le rendre meilleur sans casser. **C'est crucial. Ne le bâcle pas.**

#### Type C — `debugging`

Le starter contient du code **cassé** : bugs subtils, edge cases manqués, mauvaise gestion de la mutabilité, off-by-one, copies shallow là où il faut deep, etc. Les tests échouent au démarrage. Consigne : faire passer les tests **sans réécrire le code from scratch** (idéalement on tracke le nombre de lignes modifiées et on encourage le minimum).

Préparation à : lire des stack traces, comprendre du code qu'on n'a pas écrit, fixer un bug en chirurgie.

### 3.3 Répétition style "exos de maths de 3e"

Pour chaque concept clé d'un chapitre, **8 à 12 exercices** qui drillent le même concept sous des angles différents :

- même concept, thème différent (meubles → livraison → club sport → bibliothèque)
- même concept, niveau de difficulté différent
- même concept, mais avec un piège classique (mutable default arg, late binding closure, etc.)
- même concept, mais en version `modification` au lieu de `creation`
- même concept, mais en `debugging`

Le but : que la 10e fois où je vois `__hash__`, je le code en réflexe, pas en réfléchissant.

### 3.4 Thèmes business (pas d'abstractions vides au début)

**Banni au démarrage** : `Foo`, `Bar`, `Animal`, `Shape`, `Vehicle` génériques, `class A`, `def func(x, y)`.

**Liste de thèmes autorisés à puiser, par ordre de "familiarité concrète"** (du plus quotidien au plus métier) :

| # | Thème | Vocabulaire type |
|---|---|---|
| 1 | Entreprise de meubles | Chair, Table, Desk, Sofa, ref, price, stock, supplier, Order |
| 2 | Livraison / logistique | Package, Driver, Route, Address, ETA, status, warehouse |
| 3 | E-commerce simple | Product, Cart, Customer, Order, Discount, Coupon, Invoice |
| 4 | Club de sport / salle | Member, Subscription, Class, Trainer, Booking, attendance |
| 5 | Bibliothèque | Book, Author, Loan, Reader, ISBN, due_date, fine |
| 6 | Restaurant | Dish, Menu, Order, Table, Reservation, ingredient |
| 7 | Cabinet médical | Patient, Doctor, Appointment, Prescription, Diagnosis |
| 8 | RH / paie | Employee, Contract, Payslip, Leave, Manager |
| 9 | Plateforme de streaming | User, Movie, Episode, Watchlist, Rating, Recommendation |
| 10 | API REST de gestion de tâches | Task, Project, User, Tag, Status, Deadline |

**Et plus tard, à mesure que les chapitres avancent** (ch 8-21, type hints, async, etc.), introduire progressivement des thèmes **plus proches de mon métier visé** :

| # | Thème | Vocabulaire type |
|---|---|---|
| 11 | Serveur d'inférence LLM (fake) | Token, Prompt, Response, Sampler, KVCache, Batch |
| 12 | Pipeline de données ML | Dataset, Batch, Tokenizer, Vocabulary, DataLoader |
| 13 | Système de monitoring | Metric, Alert, Threshold, Dashboard, Timeseries |
| 14 | Cluster GPU / scheduling | Job, GPU, Worker, Queue, Resource, allocation |

**Règle d'or de progression** : un chapitre 1-7 (le socle Python) doit utiliser **majoritairement les thèmes 1-10** (concrets, du quotidien). Les thèmes 11-14 (proches LLM/ML) n'apparaissent qu'à partir du **chapitre 8** et deviennent dominants après le chapitre 14.

C'est aligné avec le projet "PyMistral" décrit dans le doc `Mapping_competences_ML_Inference_Mistral_dec2027.md` que tu vas lire — la webapp et PyMistral se renforcent mutuellement à partir du chapitre 8.

### 3.5 Courbe de difficulté à l'intérieur d'un chapitre

Échelle 1 à 5, à respecter strictement à la génération :

- **1** : application directe du concept, contrat ultra-clair, 1 fonction de 5-15 lignes. Pas de piège.
- **2** : application directe + 1 cas limite à gérer (None, liste vide, négatif).
- **3** : combine le concept avec un concept du chapitre précédent. Le piège classique du chapitre (ex: late binding closure pour ch 9) est *présent mais signalé dans l'énoncé*.
- **4** : combine 2-3 concepts, le piège classique est présent et *non signalé*. Demande une vraie modélisation (2-3 classes ou fonctions qui interagissent).
- **5** : exo "checkpoint" du chapitre. Reproduit un exemple du livre Fluent Python (cf. repo `fluentpython/example-code-2e`). C'est le test "j'ai compris le chapitre, oui ou non". Un seul par chapitre.

À la génération de 10 exos pour un concept, viser une **distribution 3-3-2-1-1** (3 niveau 1, 3 niveau 2, 2 niveau 3, 1 niveau 4, 1 niveau 5).

### 3.6 Mapping des 24 chapitres Fluent Python (concepts clés)

À la phase 1, tu vas créer un fichier `docs/curriculum/python-pure/chapter-XX.md` pour **chacun des 24 chapitres**. Le contenu de référence est dans le fichier `Mapping_competences_ML_Inference_Mistral_dec2027.md` (présent dans le projet Claude.ai) section "Couche 1" + dans le fichier `Message_3.md` (présent aussi) section "Mapping chapitres Fluent Python → exercices PyMistral".

**Avant la phase 1, fais ceci** : demande-moi en chat de te coller dans le contexte ces deux documents si tu n'y as pas accès direct. *Ne devine pas le contenu de Fluent Python à partir de tes souvenirs* — utilise la table de référence du mapping qui est ma vérité.

Chaque `chapter-XX.md` doit contenir :

```yaml
---
chapter: 1
title: "The Python Data Model"
fluent_python_pages: "1-30"  # référence éd 2
tier: S  # selon mon mapping
status: active  # active | optional | locked
prereqs: []  # IDs des chapitres prérequis
---

## Concepts clés (à drill)
- `__repr__` vs `__str__`
- `__eq__`, `__hash__` et leur contrat
- `__len__`, `__getitem__`, `__contains__`
- ... (un bullet par concept, 5-12 par chapitre)

## Pièges classiques
- `__hash__` redéfini sans `__eq__` (ou inverse) → set/dict cassés
- ... (3-7 pièges)

## Thèmes recommandés pour ce chapitre
- meubles, livraison, bibliothèque (concrets — c'est le premier chapitre)

## Référence "checkpoint" exercice niveau 5
- Reproduire la classe `FrenchDeck` du chapitre 1 (Ramalho)

## Lien PyMistral
- Classe `Token` du framework PyMistral (cf. Message_3.md)
```

### 3.7 Anti-patterns à bannir à la génération

Quand tu génères des exos, **NE FAIS PAS** :

1. Des exos qui se résolvent en 1 ligne triviale (`return x + y`).
2. Des exos qui testent une connaissance de bibliothèque externe non couverte par le chapitre (pas de `requests`, `pandas`, etc. avant le chapitre concerné).
3. Des énoncés avec du jargon ML/inference *avant* le chapitre 8.
4. Des "exemples" comme "implementez `Foo` qui hérite de `Bar`". Toujours du concret.
5. Des tests qui valident la *forme* du code (nombre de lignes, présence d'un mot-clé) **sauf pour le type modification** où c'est explicitement le but.
6. Des exos qui exigent du `import` exotique non disponible dans Pyodide. Vérifie ta liste avant.
7. Des hints qui donnent la solution directement. Un hint guide la pensée, ne révèle pas.
8. Des solutions non-idiomatiques. Si je viens ici drill du Python idiomatique, la solution référence doit être **pythonique**, pas "qui marche".

---

## 4. Format des exercices (la grammaire — à graver)

### 4.1 Arborescence d'un exercice

```
exercises/python-pure/ch01-data-model/creation/001-chair-class-basics/
├── meta.yaml
├── starter.py
├── solution.py
└── tests.py
```

### 4.2 Convention de nommage

`{type-counter}-{slug}/` où :
- `type-counter` : 3 chiffres pour `creation` (001-099), 3 chiffres pour `modification` (101-199), 3 chiffres pour `debugging` (201-299)
- `slug` : kebab-case court, max 6 mots

Ça permet de visuellement classer par type sans changer de dossier.

### 4.3 `meta.yaml` — schéma

```yaml
id: ch01-001-chair-class-basics       # unique global
chapter: 1
chapter_slug: data-model
type: creation                         # creation | modification | debugging
difficulty: 1                          # 1-5
estimated_minutes: 5                   # estimation honnête
concepts:                              # tags des concepts du chapitre drillés
  - __repr__
  - __init__
theme: furniture                       # un des thèmes section 3.4
title: "Une classe Chair propre"
short_description: "Modélise une chaise avec un __repr__ lisible."
hints:
  - "Pense à ce qui doit s'afficher quand tu fais print(chair)."
  - "Le format attendu est : Chair(ref='A1', price=99)."
  - "__repr__ doit retourner une str, pas la print elle-même."
reference_book: "Fluent Python ch 1, p. 4-7 (Vector2d analogue)"
pymistral_link: null                   # null pour ch 1-7 thèmes concrets
tags:
  - dunder
  - oop-basics
```

### 4.4 `starter.py` — convention

Toujours :
- Un module docstring qui *re-décrit la consigne en français* (l'utilisateur peut lire dans son IDE plus tard).
- Les signatures complètes avec type hints attendues (sauf si le chapitre est *justement* sur les type hints — alors elles manquent).
- Des `...` ou `raise NotImplementedError("À implémenter")` aux endroits à compléter.
- **Aucun code accessoire qui distrait**. Si le test a besoin d'une fonction utilitaire, elle est dans `tests.py`.

Exemple type creation :

```python
"""
Une entreprise de meubles a besoin de représenter ses chaises.

Implémente la classe Chair avec :
- un constructeur prenant `ref` (str) et `price` (int)
- une représentation `__repr__` au format : Chair(ref='A1', price=99)
"""


class Chair:
    def __init__(self, ref: str, price: int) -> None:
        ...

    def __repr__(self) -> str:
        ...
```

Exemple type modification :

```python
"""
Le code ci-dessous fonctionne mais n'est pas pythonique.

Refactor :
1. Ajoute __repr__ qui retourne : Chair(ref='A1', price=99)
2. Ajoute __eq__ qui compare deux chaises sur ref ET price
3. Rends la classe hashable (__hash__) cohérente avec __eq__
4. Ne casse aucun test existant.
"""


class Chair:
    def __init__(self, ref, price):
        self.ref = ref
        self.price = price

    def get_ref(self):       # à supprimer après refactor (utilise l'attribut directement)
        return self.ref

    def get_price(self):
        return self.price
```

Exemple type debugging :

```python
"""
Cette classe Chair a 2 bugs. Les tests les exposent.

Trouve et corrige sans réécrire from scratch.
"""


class Chair:
    def __init__(self, ref, price):
        self.ref = ref
        self.price = price

    def __repr__(self):
        return f"Chair(ref={self.ref}, price={self.price})"   # bug 1 : pas de quotes autour de ref

    def __eq__(self, other):
        return self.ref == other.ref                            # bug 2 : ne compare pas price
```

### 4.5 `solution.py`

Le code de référence, idiomatique, type-annoté, avec un commentaire en haut expliquant les 2-3 choix de design. Ne contient **aucun import non-stdlib** sauf si le chapitre l'exige.

### 4.6 `tests.py`

Format pytest standard. Conventions :

- 3 à 8 tests par exercice. Pas 1 (insuffisant), pas 20 (overkill).
- Chaque test a un nom *descriptif* : `test_repr_format_with_quoted_ref`, pas `test_1`.
- Le **dernier test** d'un exo `modification` ou `debugging` vérifie qu'un cas limite/edge case est géré (montre que ce n'est pas du code-pour-passer-les-tests-visibles).
- Pour les exos `modification` qui vérifient une **forme** de code (ex: présence de list comprehension), utilise `ast.parse` :

```python
import ast
import inspect
from solution_user import ma_fonction  # ce que l'utilisateur a écrit

def test_uses_list_comprehension():
    source = inspect.getsource(ma_fonction)
    tree = ast.parse(source)
    has_listcomp = any(isinstance(node, ast.ListComp) for node in ast.walk(tree))
    has_for_loop = any(isinstance(node, ast.For) for node in ast.walk(tree))
    assert has_listcomp, "Tu dois utiliser une list comprehension."
    assert not has_for_loop, "Pas de boucle for explicite (remplace par la comprehension)."
```

### 4.7 Le module `solution_user`

Dans Pyodide, le code que l'utilisateur écrit dans le Monaco editor est sauvegardé sous le nom de module `solution_user`. Les `tests.py` importent depuis `solution_user`. C'est ta convention.

---

## 5. Arborescence cible du repo

```
.
├── README.md
├── CLAUDE.md                          # ⭐ LE fichier que tu liras à chaque ouverture du repo
├── package.json
├── pnpm-lock.yaml
├── biome.json
├── tsconfig.json
├── next.config.ts
├── tailwind.config.ts
├── pyproject.toml                     # pour les scripts tooling Python (uv)
├── docs/
│   ├── context/
│   │   ├── mapping-mistral.md         # copie de Mapping_competences_ML_Inference_Mistral_dec2027.md
│   │   └── pymistral-link.md          # copie de la section pertinente de Message_3.md
│   ├── pedagogy.md                    # section 3 de ce prompt, étendue
│   ├── exercise-format.md             # section 4 de ce prompt, étendue
│   ├── themes.md                      # section 3.4 de ce prompt, étendue avec exemples de vocabulaire
│   ├── generation-recipes.md          # "comment générer 5 exos sur X" — recettes prêtes
│   └── curriculum/
│       └── python-pure/
│           ├── chapter-01.md
│           ├── chapter-02.md
│           └── ... (jusqu'à chapter-24.md)
├── exercises/
│   ├── python-pure/
│   │   ├── ch01-data-model/
│   │   │   ├── creation/
│   │   │   ├── modification/
│   │   │   └── debugging/
│   │   ├── ch02-sequences/
│   │   └── ...
│   ├── math-foundations/.gitkeep
│   ├── algorithms/.gitkeep
│   ├── pytorch-basics/.gitkeep
│   ├── performance-python/.gitkeep
│   ├── code-reading/.gitkeep
│   └── testing-discipline/.gitkeep
├── tools/                             # scripts Python utilitaires
│   ├── validate_exercise.py           # vérifie qu'un exo respecte le format + ses tests passent
│   ├── validate_all.py                # validate sur tout le repo (CI)
│   ├── index_builder.py               # construit exercises-index.json scanné par la webapp
│   └── pyproject.toml
├── public/
│   └── pyodide/                       # éventuel cache local
└── web/                               # ou racine, à toi de voir selon ton scaffolding Next.js
    ├── app/
    │   ├── layout.tsx
    │   ├── page.tsx                   # accueil : liste des tracks
    │   ├── tracks/[track]/page.tsx    # liste chapitres
    │   ├── tracks/[track]/[chapter]/page.tsx
    │   └── tracks/[track]/[chapter]/[exercise]/page.tsx
    ├── components/
    │   ├── ExerciseView.tsx
    │   ├── MonacoEditor.tsx
    │   ├── PyodideRunner.tsx
    │   ├── TestResults.tsx
    │   ├── HintsPanel.tsx
    │   ├── DiffSolution.tsx
    │   └── Sidebar.tsx
    ├── lib/
    │   ├── pyodide.ts                 # init + chargement micropip pytest
    │   ├── exercises.ts               # parse YAML, build index
    │   ├── progress.ts                # localStorage helpers
    │   └── runner.ts                  # logique run/submit
    └── public/
```

---

## 6. Todolist phasée

**Règle générale** : à la fin de chaque phase, tu fais un commit avec un message clair, tu me montres ce que tu as fait, et tu attends mon "ok phase suivante" avant d'enchaîner. Pas de marathon silencieux.

### Phase 0 — Bootstrap (45-60 min)

1. Initialise le repo Git si pas fait. `.gitignore` standard (Node + Python).
2. Crée la structure de dossiers vide complète (cf. section 5). Mets un `.gitkeep` dans les dossiers vides.
3. Scaffolde Next.js 15 avec App Router + TypeScript + Tailwind dans le dossier `web/` (ou racine, à toi de décider — *justifie ton choix dans le commit*).
4. Installe les deps : `monaco-editor`, `@monaco-editor/react`, `pyodide`, `js-yaml`, `gray-matter`, `shadcn/ui` (init).
5. Crée `pyproject.toml` racine avec `uv` pour les scripts tooling. Deps : `pyyaml`, `pytest`, `ruff`.
6. Configure Biome + ruff.
7. Crée un README.md minimal (3 paragraphes : ce que c'est, comment lancer en dev, où regarder pour comprendre).
8. **Crée `CLAUDE.md` racine** — voir section 7 pour son contenu.
9. **Copie dans `docs/context/mapping-mistral.md`** le contenu du fichier `Mapping_competences_ML_Inference_Mistral_dec2027.md` qui est dans le projet Claude.ai. Si tu n'y as pas accès direct, demande-moi de le coller dans le chat avant de continuer la phase.
10. Idem pour `docs/context/pymistral-link.md` : extrais la section "Mapping chapitres Fluent Python → exercices PyMistral" du fichier `Message_3.md`.
11. Premier commit : `chore: bootstrap repo, next.js + pyodide stack, docs scaffold`.

### Phase 1 — Curriculum (60-90 min)

1. Crée les 24 fichiers `docs/curriculum/python-pure/chapter-XX.md` selon le template section 3.6, en t'appuyant **strictement** sur le mapping Mistral et la section PyMistral copiés en phase 0. Chapitres 22-24 marqués `status: optional`.
2. Crée `docs/pedagogy.md`, `docs/exercise-format.md`, `docs/themes.md`, `docs/generation-recipes.md`. **Étoffe les sections 3 et 4 de ce prompt**. Ajoute des exemples concrets de vocabulaire pour chaque thème (10 noms de meubles type, 10 statuts de livraison type, etc.).
3. Commit : `docs: curriculum complet python-pure + pédagogie`.

### Phase 2 — Premiers exercices seed (90-120 min)

Génère les **premiers exercices pour amorcer** :

- **Chapitre 1** (Data Model) : 10 exos creation (thèmes 1-3), 5 modification, 3 debugging.
- **Chapitre 2** (Sequences) : 8 creation, 4 modification, 2 debugging.

Soit ~32 exos. Chacun avec ses 4 fichiers (`meta.yaml`, `starter.py`, `solution.py`, `tests.py`). Respect strict du format section 4. Distribution de difficulté section 3.5.

Tu écris aussi en parallèle `tools/validate_exercise.py` qui :
- Charge `meta.yaml`, vérifie le schéma.
- Lance `pytest tests.py` avec `solution.py` chargée comme `solution_user`. **Doit passer 100%** (sinon l'exo est bugué).
- Si type `creation` : lance avec `starter.py` chargé comme `solution_user`. **Doit échouer** (sinon le starter contient déjà la solution).
- Si type `debugging` : lance avec `starter.py`. **Doit échouer** (sinon il n'y a pas de bug à trouver).

Lance `validate_exercise.py` sur les 32 exos avant de commit. Si un seul échoue, corrige-le.

Commit : `feat: seed exercises ch1-2 (32 exos) + validator script`.

### Phase 3 — Webapp MVP (3-4h, peut-être en plusieurs commits)

1. `lib/pyodide.ts` : init Pyodide, micropip install pytest, cache du runtime entre exos.
2. `lib/exercises.ts` : scan du dossier `exercises/` au build (Next.js `generateStaticParams`), construit l'index, expose via `getExercise(track, chapter, id)`.
3. `components/MonacoEditor.tsx` : wrapper Monaco, thème dark, langage python, sauvegarde auto draft dans localStorage par exo.
4. `components/PyodideRunner.tsx` : prend le code utilisateur + `tests.py`, écrit `solution_user.py` dans le FS Pyodide, lance pytest, parse le résultat (JUnit XML ou parsing stdout).
5. `components/TestResults.tsx` : affichage test par test (icône, nom, message d'erreur tronqué + expand).
6. Routes Next.js complètes : home → track → chapitre → exo.
7. Sidebar avec progression localStorage.
8. Bouton Run / Submit / Hint / Voir solution avec les comportements de la section 2.2.
9. Diff solution avec `react-diff-viewer-continued` ou équivalent.

Commit en plusieurs morceaux logiques.

### Phase 4 — Polish (1-2h)

1. Compteur de progression visible.
2. Confetti discret au pass (`canvas-confetti`).
3. Sauvegarde de l'état du draft (code utilisateur) par exo dans localStorage.
4. Bouton "reset starter" qui efface le draft et restaure le starter.
5. Mobile : pas prioritaire, mais que ça ne soit pas cassé en responsive (Monaco en read-only sur mobile suffit au pire).
6. README étoffé avec captures d'écran.

### Phase 5 — Documentation pour génération future (30 min)

C'est **la phase la plus importante** pour la pérennité du projet.

Écris `docs/generation-recipes.md` qui contient des **prompts prêts à l'emploi** que je peux te re-donner plus tard :

```markdown
## Recette : "Générer N exercices sur un concept"

Quand l'utilisateur dit "génère-moi N exos sur [concept] chapitre [X] thème [T]", tu :

1. Lis `docs/curriculum/python-pure/chapter-X.md` pour identifier les pièges classiques.
2. Lis `docs/themes.md` section [T] pour le vocabulaire.
3. Génère N exos avec distribution de difficulté section 3.5 (3-3-2-1-1 pour N=10).
4. Couvre les 3 types proportionnellement : 50/30/20.
5. Au moins un exo doit déclencher le piège classique du chapitre.
6. Valide chaque exo avec `python tools/validate_exercise.py path/to/exo`.
7. Crée un commit par batch de 10.

## Recette : "Ajouter une nouvelle track"

[...]

## Recette : "Reviewer mes solutions"

Quand l'utilisateur dit "j'ai fait l'exo X, regarde", tu :
1. Lis sa solution dans `solution_user.py` (qu'il colle).
2. Lis `solution.py` (référence).
3. Compare sur 4 axes : correctness, idiomatic, performance, lisibilité.
4. Donne le feedback structuré, pas de "good job" vide.
```

Commit final : `docs: generation recipes for future exercise creation`.

---

## 7. Contenu obligatoire du `CLAUDE.md` racine

Ce fichier est lu par toi à chaque fois que je t'ouvre dans ce repo. Il doit contenir, en français, concis :

1. **Mission du repo** (3-5 lignes).
2. **Stack technique** avec les décisions de la section 1 de ce prompt.
3. **Tracks actuelles et leur statut** (table).
4. **Pointeurs vers les docs** : `pedagogy.md`, `exercise-format.md`, `themes.md`, `generation-recipes.md`, `curriculum/`.
5. **Anti-patterns à bannir** (copie de la section 3.7).
6. **Commande de validation** : "avant tout commit qui touche `exercises/`, lance `python tools/validate_all.py`".
7. **Ton et style des énoncés** : tutoiement de l'apprenant, français, concis, ton "coach technique" pas scolaire.
8. **Section "Si on te dit X, fais Y"** : un mini-runbook des demandes fréquentes (générer N exos, ajouter un chapitre, modifier la difficulté d'un exo, etc.) avec un pointeur vers la recette correspondante.

Vise 200-300 lignes max. Si tu débordes, c'est que tu mets du contenu qui doit être dans `docs/` à la place.

---

## 8. Conventions de qualité

- **Tests** : tout exo généré doit passer `validate_exercise.py`. Pas de "je commit, je validerai après".
- **Commits atomiques** : un commit = un changement logique. Message en anglais, conventional commits (`feat:`, `fix:`, `docs:`, `chore:`).
- **Pas de TODO** dans le code mergé sur main. Si un truc est inachevé, ouvre une issue GitHub locale (fichier `TODO.md` au pire).
- **Pas de dépendance ajoutée sans justification** dans le message de commit ou dans `CLAUDE.md`.
- **Type strict** côté TS (`"strict": true`), pas de `any`.
- **mypy strict** sur les solutions Python qui couvrent les chapitres type-hints (≥ ch 8).

---

## 9. Ce que je veux voir avant que tu commences vraiment

Avant la phase 0, **réponds-moi** par écrit à ces 4 questions, courtement :

1. Tu as bien accès au contenu de `Mapping_competences_ML_Inference_Mistral_dec2027.md` et `Message_3.md` dans le projet Claude.ai ? Si non, je colle quoi pour que tu démarres ?
2. Tu mets Next.js à la racine du repo ou dans `web/` ? Argumente ton choix en 2 lignes.
3. Tu vois une décision dans ce prompt qui te paraît mauvaise pour l'usage que je viens de décrire ? Si oui, dis-le maintenant.
4. Estimation honnête du temps total phases 0 à 4 ?

Ensuite, on enchaîne phase 0.

---

*Fin du prompt d'initialisation. Bon courage. Pas de "let me start by..." dans tes réponses, va droit au but.*
