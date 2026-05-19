# pedagogy.md — La pédagogie de pipithon

> Extension de `INIT_PROMPT.md` §3. Source de vérité pour **comment** drilller.
> `CLAUDE.md` §3-§7 en est le résumé opérationnel. Ici : le détail.

## 1. Principe directeur

Drill de **Python idiomatique** par répétition façon « exos de maths de 3e » :
le même concept revu 8-12 fois sous des angles variés jusqu'à devenir un
**réflexe**, pas une réflexion. Cible : profil *ML Inference Engineer*
(Mistral/NVIDIA/HF, déc. 2027 — cf. `context/mapping-mistral.md`).

Test de maîtrise (anti-pattern cat 5 n°1, `mapping-mistral.md` §5) : *si tu ne
peux pas recoder de mémoire l'exemple checkpoint d'un chapitre, tu ne l'as pas
appris.* Chaque chapitre a un exo niveau 5 qui est ce test.

## 2. Les 3 types d'exercices

| Type | Compteur dossier | Le starter… | Les tests vérifient… | Prépare à… |
|---|---|---|---|---|
| `creation` | 001-099 | signatures + `...`/`NotImplementedError` + docstring contrat | comportement attendu | écrire from scratch |
| `modification` | 101-199 | code **qui marche mais imparfait** | comportement **préservé** ET refactor **appliqué** (`ast`/mypy) | PR open-source : améliorer sans casser |
| `debugging` | 201-299 | code **cassé**, tests rouges au départ | comportement corrigé, edge case géré | lire stack trace, fix chirurgical |

Ratio cible **sur l'ensemble d'un chapitre** (pas par concept) :
**50 % creation / 30 % modification / 20 % debugging**.

`modification` est **crucial** (c'est le geste du contributeur OSS, signal
Mistral #1). Ne jamais le bâcler. Ses tests `ast`/mypy valident la *forme*
(seul cas où c'est autorisé, cf. anti-pattern §5).

## 3. Répétition « exos de maths de 3e »

Pour chaque concept clé d'un chapitre, **8 à 12 exos** qui drillent le même
concept en variant **un seul axe à la fois** :

- thème différent (meubles → livraison → bibliothèque → …)
- difficulté différente (cf. §4)
- avec/sans le piège classique du chapitre
- bascule de type (creation → modification → debugging)

But concret : la 10ᵉ fois où je vois `__hash__`, je le code en réflexe.

## 4. Courbe de difficulté (échelle 1-5, stricte)

| Niv. | Forme | Piège | Taille type |
|---|---|---|---|
| **1** | application directe, contrat ultra-clair | aucun | 1 fn, 5-15 lignes |
| **2** | application directe + 1 cas limite (None, vide, négatif) | aucun | 1 fn + garde |
| **3** | combine avec un concept du chapitre précédent | piège du chapitre **présent ET signalé** dans l'énoncé | 1-2 fn/classe |
| **4** | combine 2-3 concepts, vraie modélisation | piège **présent ET non signalé** | 2-3 classes/fn qui interagissent |
| **5** | **checkpoint** du chapitre, reproduit l'exemple canonique | — | 1 seul par chapitre |

Distribution pour 10 exos d'un concept : **3-3-2-1-1** (3×N1, 3×N2, 2×N3,
1×N4, 1×N5). Le niveau 5 référence l'exemple canonique du repo public
`fluentpython/example-code-2e` (cf. `chapter-XX.md` → « Référence checkpoint »).

## 5. Progression des thèmes (règle d'or)

Détail + vocabulaire : `themes.md`. Règle :

- **Chap. 1-7** (socle Python) : thèmes **1-10** concrets/quotidiens
  (meubles, livraison, e-commerce, club sport, bibliothèque, restaurant,
  cabinet médical, RH, streaming, todo API). **Pas de jargon ML.**
- **Chap. 8+** : introduction progressive des thèmes **11-14** (serveur
  d'inférence LLM *fake*, pipeline données ML, monitoring, cluster GPU).
- **Après chap. 14** : thèmes 11-14 deviennent dominants.

Aligné avec le futur projet PyMistral (cf. `context/pymistral-link.md`) — la
webapp et PyMistral se renforcent à partir du chap. 8.

## 6. Ton et style des énoncés

- **Français**, **tutoiement** de l'apprenant.
- Concis, **coach technique** — pas scolaire, zéro « Bravo ! » vide.
- Énoncé = un contrat clair. Le piège est signalé (niv. ≤ 3) ou non (niv. ≥ 4).
- Hints : 1 à 3, progressifs, **guident la pensée sans la révéler**.
- Solution réf : **idiomatique** (pas « qui marche »), type-annotée dès le
  chap. 8, 2-3 lignes de commentaire expliquant les choix de design.

## 7. Anti-patterns à bannir à la génération (= `CLAUDE.md` §5)

1. Exo résolu en 1 ligne triviale (`return x + y`).
2. Tester une lib externe non couverte par le chapitre.
3. Jargon ML/inference **avant le chap. 8**.
4. `Foo`/`Bar`/`Animal`/`Shape` génériques — toujours du concret métier.
5. Tests qui valident la *forme* du code — **sauf** type `modification`.
6. `import` indispo dans Pyodide — vérifier avant.
7. Hint qui donne la solution.
8. Solution non-idiomatique.

## 8. Validation (non négociable)

Avant tout commit touchant `exercises/` : `uv run python tools/validate_all.py`.
Par exo : `meta.yaml` conforme au schéma ; `solution.py` → pytest 100 % vert ;
`starter.py` → pytest **doit échouer** (types `creation`/`debugging`). Un exo
qui ne passe pas le validator **n'est pas commitable**. Détail : `exercise-format.md` §6.
