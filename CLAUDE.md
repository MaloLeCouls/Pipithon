# CLAUDE.md — Manuel d'opération de `pipithon`

> Lis ce fichier en entier à chaque ouverture du repo : c'est ta source de vérité
> opérationnelle. Le détail long vit dans `docs/`. Si ce fichier déborde, c'est que
> du contenu doit migrer dans `docs/`.

## 0. État actuel (tenir à jour à chaque phase)

- **Phase 0 (bootstrap) : faite.** Repo Git, stack Next.js + Pyodide, scaffold docs.
- **Phase 1 (curriculum) : faite (option B, 2026-05-19).** 24 `chapter-XX.md` +
  `docs/{pedagogy,exercise-format,themes,generation-recipes}.md` +
  `learning-journal/python-deep/fluent_python_inventory.md`. Calibré sur la TOC
  publique Fluent Python 2e × `mapping-mistral.md`.
- **M3 (framework PyMistral interne) : fait (2026-06-11).** Paquet jouet
  `exercises/_pymistral/pymistral/` (10 modules, ~300 lignes, `mypy --strict`
  vert, 21 tests de fumée). Embarqué côté webapp via
  `web/scripts/build-pymistral.mjs` → `web/lib/_pymistral-bundle.ts`, écrit
  dans la FS Pyodide sous `/exo/pymistral/`. Côté validateur : copié dans le
  tmpdir avant pytest. `meta.yaml: pymistral_link` accepte désormais `null` OU
  une string dotted-path (ex. `pymistral.sampling`). Détail : `docs/context/pymistral-link.md`.
- **M2 (mode mypy strict pour `modification`) : fait (2026-06-11).** Champ
  optionnel `meta.yaml: tests_form_kind: mypy`. Quand présent, le validateur
  exige `mypy --strict` vert sur `solution.py` ; pour `modification` il exige
  en plus que `starter.py` ÉCHOUE mypy (sinon les annotations sont déjà là).
  Pas de passe mypy côté Pyodide (fallback AST documenté `exercise-format.md` §9).
- **Phase 2 + seed étoffé : faite.** Seed ch1-ch5 (cf. ligne « track active »
  ci-dessous). `validate_exercise.py` + `validate_all.py` opérationnels
  (solution-verte/starter-rouge, timeout filet, logs flushés). Cible de
  calibration : Python fluent pour ML Inference Engineer
  (NVIDIA/Google/Mistral/Apple) + OSS vLLM/SGLang.
- **Phase 3 (webapp MVP) : faite (build vert, 97 pages SSG).** `web/` :
  `lib/{exercises,pyodide,progress}.ts` + composants (Monaco, TestResults,
  HintsPanel, DiffSolution, ExerciseWorkbench, Progress) + routes home →
  track → chapitre → exo. Pyodide+pytest côté client, run/submit, hints
  progressifs, solution gated (réussite ou 3 échecs), progression
  localStorage. ⚠️ runtime Pyodide navigateur non testé end-to-end ici
  (build/typecheck/lint OK ; à fumer-tester via `pnpm dev`).
- **Phase 4 (polish) : faite.** Confetti maison sur Submit vert (canvas,
  zéro dep, burst uniquement à la première réussite), reset par exo
  (statut + brouillon, confirm si déjà vert) + reset global sur la home,
  tap-targets mobile élargis (Run/Submit/Reset + boutons indices/solution),
  section « Aperçu » + « Stack en bref » au README + 4 captures live
  (home / track / chapter / workbench).
- **Perf nav (suivi UX) : passe 1.** Latence perçue sur les transitions
  signalée 2026-06-04 → lazy-load Monaco sur le workbench + mémo cache de
  `getAllExercises` côté server. À revérifier sur build prod si la sensation
  persiste (cf. memory `webapp-nav-latency`).
- **Atelier A (M1 ch6-9 + M2 + M3) : fait (2026-06-11).** 72 nouveaux exos
  Fluent Python chapitres 6 à 9 (mutability / functions first-class /
  type hints / decorators+closures), tous ratios 50/30/20 respectés,
  checkpoints niveau 5 reproduits (HauntedBus, BingoCage, show_count, clock).
  Premiers exos qui importent `pymistral` à partir du ch.8 (pont thématique
  ML ouvert par la règle d'or `themes.md`). 4 exos avec `tests_form_kind:
  mypy` actif. Cf. `docs/sessions/2026-06-11-upgrade-request.md` pour la
  roadmap restante (ateliers B, C, D).
- Track active : `python-pure` (**158 exos validés** ; ch1 18, ch2 14,
  ch3 18, ch4 18, ch5 18, ch6 18, ch7 18, ch8 18, ch9 18 ; ch10-ch24
  scaffold). **Couverture du contrat : ~38 %.**
- Prochaine action (atelier A reliquat) : C2 ch17 generators (streaming
  tokens *via* pymistral), C3 ch18 context managers (`@inference_context`),
  C4 ch21 asyncio (Scheduler async, vérifier `asyncio.run` Pyodide), C5
  ch13 Protocol/ABC plein, M5 mode « refaire de mémoire » côté webapp.
  Ensuite ateliers B (type `review` + tracks code-reading/oss-onboarding /
  testing-discipline / métrique PR scopée) puis C (modes chrono +
  closed-book) puis D (concours bot-programming, parallèle).
  Lancer en local : `cd web && pnpm dev` (si bloqué par `sharp@0.34.5`
  ignoré, lancer `node node_modules/next/dist/bin/next dev` en attendant
  de débloquer l'allowlist pnpm — l'allowlist est déjà dans `pnpm-workspace.yaml`).
- Validation exos (pas d'`uv` ici) : `python tools/validate_all.py`
  (158/158 verts au 2026-06-11).

## 1. Mission

Dojo de code **mono-utilisateur** pour préparer un profil *ML Inference Engineer*
(cibles Mistral / NVIDIA / Hugging Face, déc. 2027 — cf.
`docs/context/mapping-mistral.md`). On drille du **Python idiomatique** par
répétition façon « exos de maths de 3e », puis maths ML / algos / PyTorch /
code-reading. Le repo contient *toute* l'info pour générer des exos cohérents sans
ré-expliquer le format. **Ce repo est ton manuel d'opération.**

## 2. Stack technique (décisions arrêtées — ne pas re-débattre)

| Choix | Décision |
|---|---|
| Frontend | Next.js 15 (App Router) + TypeScript, dans `web/` |
| Style | Tailwind v4 + shadcn/ui |
| Éditeur | Monaco (`@monaco-editor/react`) |
| Exécution Python | **Pyodide** (CPython WASM), client-side, zéro backend |
| Tests | `pytest` dans Pyodide ; code user importé comme module `solution_user` |
| Progression | `localStorage` (mono-user, pas de DB) |
| Exercices | YAML + `.py` versionnés Git, scannés au build |
| Package mgr | `pnpm` via corepack (JS) ; `uv` (Python tooling) |
| Déploiement | Vercel (auto sur push `main`, *Root Directory = `web/`*) |
| Lint/format | Biome (`web/biome.json`) + ruff (`pyproject.toml`) |

Bannis : Streamlit/Gradio/Flask/Anvil ; Docker dev local (au début) ; **IA d'éval
dans la webapp** (les tests pytest tranchent, point).

Écarts assumés vs `INIT_PROMPT.md` §5 : Next.js entièrement auto-contenu dans
`web/` (configs incluses) au lieu de configs JS à la racine — garde la racine =
manuel d'op lisible, Vercel trivial. Tailwind v4 (pas de `tailwind.config.ts`,
thème via CSS `@theme`) car c'est le défaut `create-next-app` 15 et l'esprit
« moderne/rapide » de la spec.

## 3. Tracks et statut

| Track | Statut | Couverture |
|---|---|---|
| `python-pure` | **active** | Fluent Python 2e ch 1-21 ; ch 22-24 `optional` |
| `math-foundations` | locked | algèbre lin., calcul, probas (numpy) |
| `algorithms` | locked | patterns NeetCode en Python |
| `pytorch-basics` | locked | tensors, autograd, `nn.Module` |
| `performance-python` | locked | cProfile, line_profiler, optim |
| `code-reading` | locked | snippets vLLM / transformers / llama.cpp |
| `testing-discipline` | locked | pytest avancé, fixtures, hypothesis |

## 4. Documentation (pointeurs)

- `docs/pedagogy.md` — pédagogie complète (3 types, répétition, difficulté 1-5).
- `docs/exercise-format.md` — grammaire d'un exo (arbo, `meta.yaml`, conventions).
- `docs/themes.md` — thèmes business + vocabulaire par thème.
- `docs/generation-recipes.md` — prompts prêts à l'emploi (recettes).
- `docs/curriculum/python-pure/chapter-XX.md` — concepts/pièges par chapitre.
- `docs/context/mapping-mistral.md` — cible métier (vérité de calibration).
- `docs/context/pymistral-link.md` — lien webapp ↔ projet PyMistral.

> Les `docs/*.md` pédago sont créés en **phase 1**. D'ici là, la vérité de
> référence est `INIT_PROMPT.md` §3-4 + ce fichier.

## 5. Anti-patterns à bannir à la génération (copie `INIT_PROMPT.md` §3.7)

1. Exos résolus en 1 ligne triviale (`return x + y`).
2. Tester une lib externe non couverte par le chapitre (pas de `requests`/`pandas`
   avant le chapitre concerné).
3. Jargon ML/inference **avant le chapitre 8**.
4. `Foo` / `Bar` / `Animal` / `Shape` génériques — toujours du concret métier.
5. Tests qui valident la *forme* du code — **sauf** type `modification` (le but).
6. `import` exotique indispo dans Pyodide — vérifier la liste avant.
7. Hints qui donnent la solution. Un hint guide la pensée, ne révèle pas.
8. Solutions non-idiomatiques. La solution réf doit être **pythonique**.

## 6. Validation (obligatoire)

**Avant tout commit touchant `exercises/` : `uv run python tools/validate_all.py`.**
Par exo, `tools/validate_exercise.py` vérifie : `meta.yaml` conforme au schéma ;
`solution.py` chargée comme `solution_user` → pytest **100 % vert** ; `starter.py`
chargé → pytest **doit échouer** (types `creation`/`debugging`). Un exo qui ne
passe pas le validator **n'est pas commitable**. Pas de « je validerai après ».

> Scripts créés en phase 2. D'ici là : validation manuelle au même standard.

## 7. Ton et style des énoncés

- **Français**, **tutoiement** de l'apprenant.
- Concis, ton **coach technique** — pas scolaire, pas de « Bravo ! » vide.
- Énoncé = un contrat clair (+ le piège signalé ou non selon la difficulté §3.5).
- Hints : 1 à 3, progressifs, guident la pensée sans la révéler.
- Solution réf : idiomatique, type-annotée (≥ ch 8), 2-3 lignes de commentaire
  expliquant les choix de design.

## 8. Runbook — « Si on te dit X, fais Y »

| Si on te dit… | Fais… |
|---|---|
| « génère N exos sur \<concept\> ch \<X\> thème \<T\> » | `docs/generation-recipes.md` §"Générer N exos" : lis `curriculum/.../chapter-X.md` (pièges) + `themes.md` (vocab T) ; distribution difficulté 3-3-2-1-1 (N=10) ; ratio types 50/30/20 ; ≥1 exo déclenche le piège du chapitre ; valide chaque exo ; commit par batch de 10. |
| « ajoute un chapitre / une track » | `docs/generation-recipes.md` §"Ajouter une track" ; scaffold dossiers + `chapter-XX.md` depuis le mapping. |
| « j'ai fait l'exo X, regarde » | `docs/generation-recipes.md` §"Reviewer" : compare le `solution_user` collé vs `solution.py` sur 4 axes — correctness, idiomatic, perf, lisibilité. Feedback structuré, pas de « good job ». |
| « change la difficulté de l'exo X » | Relis pédagogie §3.5 ; ajuste `meta.yaml: difficulty` + énoncé/tests cohérents ; re-valide. |
| « phase suivante » | Reprends `INIT_PROMPT.md` §6 à la phase courante (cf. §0). Si phase 1 et `pymistral-link.md` encore placeholder → **stop**, redemande le contenu. |

> Workflow : commit en fin de phase, montrer le diff, **attendre le « ok »** avant
> d'enchaîner. Commits atomiques, conventional commits, message en anglais,
> co-author footer Claude obligatoire. Pas de marathon silencieux.
