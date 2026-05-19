# pymistral-link.md — Décision : option B prise (2026-05-19)

**Statut : DÉBLOQUÉ (option B).** La phase 1 (curriculum) est autorisée.

## Décision actée

L'utilisateur a fourni le **2026-05-19** la table des matières officielle
publique de *Fluent Python* 2e (Ramalho, O'Reilly 2022, Python 3.10+) —
faits bibliographiques, *pas* un souvenir du contenu interdit par
`INIT_PROMPT.md` §3.6 — avec sa classification de priorité ML inference.

Cette TOC croisée avec `mapping-mistral.md` (Couche 1) est la **vérité de
calibration** des `docs/curriculum/python-pure/chapter-XX.md`. Copie de
travail cochable : `learning-journal/python-deep/fluent_python_inventory.md`.

→ **Curriculum bâti SANS framework PyMistral.** Le champ `meta.yaml:
pymistral_link` reste **`null` partout** jusqu'à réception du framework.

## Ce qui manque toujours (à fournir plus tard)

La **description du projet PyMistral** : le framework fil rouge (classes
`Token`/`Sampler`/`KVCache`/`Batch`…) cité par `INIT_PROMPT.md` §3.6. Tant
qu'il n'est pas fourni :

- `pymistral_link: null` dans tous les `meta.yaml`.
- Section « Lien PyMistral » des `chapter-XX.md` = pointeur vers ce fichier,
  + (chap. ≥ 8 seulement) le **pont thématique** autorisé par `INIT_PROMPT.md`
  §3.4 : thèmes 11-14 (serveur d'inférence LLM *fake*, pipeline de données ML,
  monitoring, cluster GPU) — du vocabulaire métier, **aucune classe PyMistral
  inventée**.

## À faire quand le framework PyMistral arrivera

1. Documenter ici ses classes/responsabilités.
2. Re-générer / annoter les `chapter-XX.md` (section « Lien PyMistral »).
3. Renseigner `pymistral_link` dans les `meta.yaml` concernés (chap. ≥ 8).
4. Re-valider tous les exos touchés (`tools/validate_all.py`).

> Règle de progression des thèmes (rappel `INIT_PROMPT.md` §3.4) : chap. 1-7
> = thèmes concrets 1-10 ; thèmes 11-14 (proches LLM/ML) à partir du chap. 8,
> dominants après le chap. 14.
