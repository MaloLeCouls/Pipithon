"""L'API de tâches a une cascade `if/elif` qui traduit un statut en libellé.
Ça marche, mais c'est verbeux et facile à oublier de mettre à jour. Le
chapitre 18 dit : `match/case` est *fait* pour ce dispatch sur littéraux.

Refactor `status_label(status)` :
- Remplace TOUS les `if/elif` par un seul `match status:`.
- Garde le comportement à l'identique (mêmes mappings, même défaut)."""
from __future__ import annotations


def status_label(status: str) -> str:
    if status == "todo":
        return "À faire"
    elif status == "doing":
        return "En cours"
    elif status == "review":
        return "En revue"
    elif status == "done":
        return "Terminé"
    elif status == "blocked":
        return "Bloqué"
    else:
        return "Inconnu"
