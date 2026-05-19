# generation-recipes.md — Recettes prêtes à l'emploi

> Prompts opérationnels. Quand l'utilisateur dit X, applique la recette Y.
> `CLAUDE.md` §8 (runbook) pointe ici. Phase la plus importante pour la
> pérennité : sans ces recettes, chaque demande ré-explique le format.

---

## Recette — « Génère N exos sur \<concept\> ch \<X\> thème \<T\> »

1. Lis `docs/curriculum/python-pure/chapter-{X}.md` : concepts clés, **pièges
   classiques**, référence checkpoint niv. 5.
2. Lis `docs/themes.md` section `<T>` : vocabulaire concret. Vérifie la **règle
   d'or** (ch 1-7 → thèmes 1-10 ; jargon ML interdit avant ch 8).
3. Distribution de difficulté (N=10) : **3-3-2-1-1** (`pedagogy.md` §4).
   Adapter au prorata pour N≠10.
4. Ratio types sur le lot : **~50 % creation / 30 % modification / 20 %
   debugging** (`pedagogy.md` §2).
5. **≥ 1 exo déclenche le piège classique** du chapitre (signalé si niv. ≤ 3,
   non signalé si niv. ≥ 4).
6. Varie **un seul axe à la fois** entre exos du même concept (thème, OU
   difficulté, OU type) — répétition « maths de 3e ».
7. Chaque exo : 4 fichiers (`meta.yaml`, `starter.py`, `solution.py`,
   `tests.py`) conformes à `exercise-format.md`. `pymistral_link: null`.
8. Numérote en continu dans le bon range (creation 001+, modification 101+,
   debugging 201+) sans collision avec l'existant.
9. **Valide** : `uv run python tools/validate_exercise.py <chemin>` pour chacun.
   Un échec → corrige avant de continuer. Pas de commit d'exo non validé.
10. Commit par **batch de 10** : `feat: seed exercises ch{X} <concept> (N exos)`.
    Montre le diff, attends le « ok ».

Garde-fous (`pedagogy.md` §7) : pas de one-liner trivial ; pas de lib hors
chapitre ; pas de `Foo/Bar` ; hints qui guident sans révéler ; solution
idiomatique ; tests de forme **seulement** pour `modification`.

---

## Recette — « Ajoute un chapitre / une track »

1. Track : crée `exercises/<track>/` + `creation|modification|debugging/.gitkeep`
   par chapitre. Statut dans `CLAUDE.md` §3 (`locked` → `active`).
2. Chapitre : dossier `exercises/python-pure/ch{NN}-{slug}/` (3 sous-dossiers)
   + `docs/curriculum/python-pure/chapter-{NN}.md` selon le template (frontmatter
   + concepts + pièges + thèmes + checkpoint + lien PyMistral).
3. Calibre **strictement** sur `context/mapping-mistral.md` (tier) +
   `learning-journal/python-deep/fluent_python_inventory.md` (concepts). Ne
   devine pas le contenu de Fluent Python (INIT §3.6).
4. Mets à jour `CLAUDE.md` §3 (table tracks) et `fluent_python_inventory.md`.
5. Commit : `docs: add chapter/track <name> scaffold`.

---

## Recette — « J'ai fait l'exo X, regarde »

1. L'utilisateur colle son `solution_user`. Lis-le + `solution.py` de l'exo.
2. Compare sur **4 axes**, dans cet ordre :
   - **Correctness** : passe-t-il `tests.py` ? edge cases ?
   - **Idiomatique** : pythonique ? (le cœur du dojo — sois exigeant)
   - **Performance** : complexité, copies inutiles, allocations.
   - **Lisibilité** : nommage, structure, type hints.
3. Feedback **structuré et direct**, ton coach (`pedagogy.md` §6). **Pas de
   « good job » vide.** Pointe le diff concret avec la réf, explique le *pourquoi*
   idiomatique, propose la version cible.
4. Si récurrent : suggère de noter l'anti-pattern (asset d'entretien cat 5,
   `mapping-mistral.md` Couche 17).

---

## Recette — « Change la difficulté de l'exo X »

1. Relis `pedagogy.md` §4 (échelle 1-5).
2. Ajuste `meta.yaml: difficulty` **et** la cohérence : énoncé (piège signalé
   si ≤ 3, masqué si ≥ 4), nombre de concepts combinés, taille, tests.
3. Re-valide l'exo. Commit : `fix: recalibrate difficulty ch{X}-{id}`.

---

## Recette — « Phase suivante »

Reprends `INIT_PROMPT.md` §6 à la phase courante (`CLAUDE.md` §0). Si phase 1
et `context/pymistral-link.md` est encore un placeholder → **stop**, redemande
le framework PyMistral. (Au 2026-05-19 : phase 1 faite via option B, phase 2 =
exos seed ch1-2 + `tools/validate_exercise.py`.) Workflow : commit en fin de
phase, montre le diff, **attends le « ok »**. Conventional commits, message en
anglais, footer co-author Claude. Pas de marathon silencieux.
