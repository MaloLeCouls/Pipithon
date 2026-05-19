"""CHECKPOINT chapitre 4 — si tu fais ça sans réfléchir, Unicode est acquis.

Un cabinet médical rapproche des identités patients de sources variées.

1. `nfc_equal(a: str, b: str) -> bool`
   True si `a` et `b` sont canoniquement équivalents (égalité Unicode
   correcte, MAIS sensible à la casse).

2. `fold_equal(a: str, b: str) -> bool`
   True si `a` et `b` sont équivalents en IGNORANT la casse, en plus de
   l'équivalence canonique.

Contraintes :
- nfc_equal("café", "café"décomposé) -> True
- nfc_equal("Café", "café") -> False  (la casse compte)
- fold_equal("Café", "café"décomposé) -> True (casse ignorée)
- fold_equal doit accepter tout ce que nfc_equal accepte (plus permissif).
"""


def nfc_equal(a: str, b: str) -> bool:
    raise NotImplementedError("À implémenter")


def fold_equal(a: str, b: str) -> bool:
    raise NotImplementedError("À implémenter")
