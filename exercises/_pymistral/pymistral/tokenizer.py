"""BPETokenizer — tokenizer caractère-par-caractère jouet. Chapitre 4 (unicode/bytes).

C'est *pas* du vrai BPE (pas de merges) : un caractère = un token. Le but
est de drilller la frontière `str`/`bytes`, l'encodage UTF-8 et le round-trip
encode/decode, pas de battre tiktoken.
"""
from __future__ import annotations

from collections.abc import Iterable

from pymistral.tokens import Token
from pymistral.vocabulary import Vocabulary


class BPETokenizer:
    """Tokenizer trivial : 1 code point = 1 token. Vocab auto-construit.

    Le contrat round-trip est garanti : `decode(encode(s)) == s`.
    """

    def __init__(self, vocab: Vocabulary | None = None) -> None:
        self._vocab = vocab if vocab is not None else Vocabulary()

    @property
    def vocab(self) -> Vocabulary:
        return self._vocab

    def encode(self, text: str) -> list[Token]:
        out: list[Token] = []
        for ch in text:
            tid = self._vocab.add(ch)
            out.append(Token(id=tid, text=ch))
        return out

    def decode(self, tokens: Iterable[Token]) -> str:
        return "".join(t.text for t in tokens)

    def encode_bytes(self, data: bytes, encoding: str = "utf-8") -> list[Token]:
        """Pratique pour les exos chapitre 4 : décode bytes puis tokenize."""
        return self.encode(data.decode(encoding))

    def __repr__(self) -> str:
        return f"BPETokenizer(vocab_size={len(self._vocab)})"
