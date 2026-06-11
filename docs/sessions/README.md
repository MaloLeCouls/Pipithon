# `docs/sessions/` — archive des prompts d'opération et livrables ponctuels

Ce dossier contient les **inputs** (prompts utilisateurs lançant une session de
travail importante) et les **outputs** (livrables ponctuels comme un audit) qui
n'ont pas leur place dans le manuel d'opération (`CLAUDE.md`) ni dans la doc
pédagogique (`docs/{pedagogy,exercise-format,themes,generation-recipes}.md`).

Convention de nommage : `YYYY-MM-DD-<slug>.{md,txt}`.

## Inventaire

| Fichier | Type | Résumé |
|---|---|---|
| `2026-06-10-audit-request.txt` | input | Prompt utilisateur : « audit exhaustif + auto-critique » |
| `2026-06-10-audit.md` | output | Livrable de cet audit : Partie A description + Partie B propositions, classées P0-P2 |
| `2026-06-11-upgrade-request.md` | input | Prompt « PROMPT COLOSSAL » : roadmap ateliers A-D, top 5 priorités |

Les commits exécutant ces prompts sont chaînés sur `main` (cf. `git log --oneline`).
