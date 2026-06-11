import inspect

from pymistral import BPETokenizer
from solution_user import encode_all


def test_works_with_bpe_tokenizer():
    tk = BPETokenizer()
    out = encode_all(["ab", "c"], tk)
    assert [len(toks) for toks in out] == [2, 1]


def test_works_with_any_encoder_like_object():
    class Fake:
        def encode(self, text: str):
            from pymistral import Token
            return [Token(i, c) for i, c in enumerate(text)]
    out = encode_all(["xy"], Fake())
    assert len(out[0]) == 2


def test_encoder_annotation_is_protocol_not_bpe():
    sig = inspect.signature(encode_all)
    ann = str(sig.parameters["encoder"].annotation)
    assert "BPETokenizer" not in ann, \
        f"l'annotation doit être un Protocol, pas BPETokenizer ({ann})"
