# exercise-format.md — La grammaire d'un exercice

> Extension de `INIT_PROMPT.md` §4. Vérité de référence pour la **structure**
> d'un exo et son `meta.yaml`. Le validator (`tools/validate_exercise.py`,
> phase 2) applique ce contrat mécaniquement.

## 1. Arborescence

```
exercises/python-pure/ch01-data-model/creation/001-chair-repr-basics/
├── meta.yaml
├── starter.py
├── solution.py
└── tests.py
```

## 2. Nommage

`ch{NN}-{slug-chapitre}/{type}/{compteur}-{slug-exo}/`

- `compteur` : `001-099` creation · `101-199` modification · `201-299` debugging.
  Classe visuellement par type sans changer de dossier.
- `slug-exo` : kebab-case, ≤ 6 mots, en anglais court.
- Slugs chapitres figés : voir `exercises/python-pure/` (ch01-data-model …
  ch24-class-metaprogramming).

## 3. `meta.yaml` — schéma

```yaml
id: ch01-001-chair-repr-basics        # unique global : ch{NN}-{compteur}-{slug}
chapter: 1
chapter_slug: data-model
type: creation                         # creation | modification | debugging
difficulty: 1                          # 1-5 (cf. pedagogy.md §4)
estimated_minutes: 5                   # estimation honnête
concepts:                              # tags concepts du chapitre drillés
  - __repr__
  - __init__
theme: furniture                       # un slug de themes.md
title: "Une classe Chair propre"
short_description: "Modélise une chaise avec un __repr__ lisible."
hints:                                 # 1 à 3, progressifs, ne révèlent pas
  - "Que doit afficher print(chair) ?"
  - "Format attendu : Chair(ref='A1', price=99)."
  - "__repr__ retourne une str, ne print pas."
reference_book: "Fluent Python ch 1 (analogue Vector2d)"
pymistral_link: null                   # null partout tant que framework non fourni
tags:
  - dunder
  - oop-basics
```

Champs obligatoires : `id, chapter, chapter_slug, type, difficulty,
estimated_minutes, concepts, theme, title, short_description, hints,
reference_book, pymistral_link, tags`. `pymistral_link` **toujours `null`**
(cf. `context/pymistral-link.md`).

## 4. `starter.py`

- Module docstring qui **re-décrit la consigne en français** (lisible en IDE).
- Signatures complètes **avec type hints attendus** — *sauf* si le chapitre
  porte justement sur les type hints (ch 8, 15) : alors elles manquent.
- `...` ou `raise NotImplementedError("À implémenter")` aux trous.
- **Aucun code accessoire distrayant.** Une fn utilitaire de test va dans `tests.py`.
- Type `modification` : code qui marche mais imparfait (verbeux, non-idiomatique,
  lent, mal typé, sans dunders…). Type `debugging` : code cassé, bugs commentés
  dans la solution, pas dans le starter.

## 5. `solution.py`

- Code de référence **idiomatique**, type-annoté (≥ ch 8), `solution_user`-compatible.
- En-tête : 2-3 lignes de commentaire expliquant les **choix de design**.
- **Aucun import non-stdlib** sauf si le chapitre l'exige.

## 6. `tests.py`

- Format `pytest`. **3 à 8 tests** (pas 1, pas 20).
- Importe depuis `solution_user` (le code user est écrit là dans Pyodide).
- Noms **descriptifs** : `test_repr_quotes_ref`, jamais `test_1`.
- Dernier test d'un `modification`/`debugging` = un **edge case** (anti
  code-pour-passer-les-tests-visibles).
- `modification` vérifiant une *forme* → `ast` + `inspect.getsource` :

```python
import ast, inspect
from solution_user import normalize_refs

def test_uses_list_comprehension():
    tree = ast.parse(inspect.getsource(normalize_refs))
    assert any(isinstance(n, ast.ListComp) for n in ast.walk(tree)), \
        "Utilise une list comprehension."
    assert not any(isinstance(n, ast.For) for n in ast.walk(tree)), \
        "Pas de boucle for explicite."
```

## 7. Convention `solution_user`

Le code Monaco de l'utilisateur est écrit dans Pyodide sous le module
`solution_user`. `tests.py` importe **toujours** depuis `solution_user`.
Le validator charge tour à tour `solution.py` puis `starter.py` sous ce nom.

### 7.bis Importer le framework `pymistral`

Le paquet `pymistral` (mini-framework d'inférence jouet, cf.
`docs/context/pymistral-link.md` et `exercises/_pymistral/README.md`) est
**toujours disponible** dans `tests.py` / `solution.py` / `starter.py` :

```python
from pymistral import Token, GenerationConfig, top_k_sampler
```

Mécanique : monté dans la FS Pyodide à l'init (`web/lib/pyodide.ts` +
`web/lib/_pymistral-bundle.ts`), et copié dans le tmpdir du validateur
(`tools/validate_exercise.py`). Pas d'installation, pas de réseau.

Convention : `pymistral_link` dans `meta.yaml` pointe le module/symbole utilisé
quand c'est pertinent (chap. ≥ 8 typiquement), `null` sinon.

## 8. Contrat du validator (phase 2)

`tools/validate_exercise.py` par exo :

1. `meta.yaml` parse + conforme au schéma §3.
2. `solution.py` chargée comme `solution_user` → `pytest` **100 % vert**
   (sinon exo bugué).
3. `creation`/`debugging` : `starter.py` chargé comme `solution_user` →
   `pytest` **doit échouer** (sinon le starter contient la solution / pas de bug).
4. `modification` : starter passe les tests de comportement mais **échoue** les
   tests de forme (`ast`/mypy) — le refactor reste à faire.

`tools/validate_all.py` = §1-4 sur tout le repo. Un échec = non commitable.
**Pas de « je validerai après ».**
