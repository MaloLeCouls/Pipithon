"""Un sampler peut échouer (rate-limit, etc.). On veut retenter automatiquement.

Implémente le décorateur paramétré `retry(max_attempts: int = 3)` :
- pattern 3 étages.
- Le wrapper exécute la fonction décorée.
- Si elle lève une exception : il retente, jusqu'à `max_attempts` au total.
- Si tous les essais échouent : il relève la DERNIÈRE exception.
- Si l'un réussit : il renvoie son résultat (les essais précédents sont oubliés).
"""
from __future__ import annotations


def retry(max_attempts: int = 3):
    ...
