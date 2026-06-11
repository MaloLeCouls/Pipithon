"""Cette fonction dépend explicitement de BPETokenizer. Trop restrictif :
tout objet qui sait `encode(str) -> list[Token]` devrait marcher.

Refactor :
1. Définis un `Protocol` `Encoder` avec la méthode `encode(self, text: str) -> list[Token]`.
2. Change l'annotation de `encoder` pour utiliser ton Protocol.

Le validateur exige mypy --strict ; la solution doit passer, le starter doit
échouer (BPETokenizer importé puis utilisé comme annotation = couplage trop fort).
"""
from pymistral import BPETokenizer, Token  # noqa: F401


def encode_all(texts, encoder: BPETokenizer):
    return [encoder.encode(t) for t in texts]
