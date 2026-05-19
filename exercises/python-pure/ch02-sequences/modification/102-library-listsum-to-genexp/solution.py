"""Choix de design :
- sum(genexp) consomme les valeurs à la volée : aucune liste temporaire
  allouée. Sur un gros journal de prêts, c'est O(1) mémoire au lieu de
  O(n) — et c'est l'idiome attendu (les crochets superflus sautent en review).
"""


def late_fees_total(loans: list[dict]) -> float:
    return sum(loan["fine"] for loan in loans if loan["late"])
