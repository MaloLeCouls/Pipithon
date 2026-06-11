from pymistral import BPETokenizer, Token
from solution_user import Encoder, count_tokens


def test_count_with_bpe_tokenizer():
    tk = BPETokenizer()
    assert count_tokens("abc", tk) == 3


def test_empty_string_yields_zero():
    tk = BPETokenizer()
    assert count_tokens("", tk) == 0


def test_bpe_satisfies_protocol_structurally():
    tk = BPETokenizer()
    assert isinstance(tk, Encoder), "BPETokenizer doit satisfaire Encoder par structure"


def test_custom_class_can_satisfy_protocol():
    class FakeEncoder:
        def encode(self, text: str) -> list[Token]:
            return [Token(i, c) for i, c in enumerate(text.upper())]
    fake = FakeEncoder()
    assert isinstance(fake, Encoder)
    assert count_tokens("hi", fake) == 2


def test_object_without_encode_is_not_encoder():
    class NotAnEncoder:
        pass
    assert not isinstance(NotAnEncoder(), Encoder)
