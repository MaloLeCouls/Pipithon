import collections.abc as abc

from pymistral import Token, Vocabulary
from solution_user import stream_tokens


def test_yields_one_token_per_char():
    vocab = Vocabulary()
    tokens = list(stream_tokens("abc", vocab))
    assert len(tokens) == 3
    assert all(isinstance(t, Token) for t in tokens)
    assert [t.text for t in tokens] == ["a", "b", "c"]


def test_ids_match_vocab():
    vocab = Vocabulary()
    tokens = list(stream_tokens("ab", vocab))
    assert tokens[0].id == vocab.id_of("a")
    assert tokens[1].id == vocab.id_of("b")


def test_repeated_char_reuses_id():
    vocab = Vocabulary()
    tokens = list(stream_tokens("aba", vocab))
    assert tokens[0].id == tokens[2].id  # même caractère => même id
    assert tokens[0].id != tokens[1].id


def test_returns_iterator_lazy():
    vocab = Vocabulary()
    gen = stream_tokens("hello", vocab)
    assert isinstance(gen, abc.Iterator)
    # Avant d'avoir tiré, le vocab ne contient encore aucun caractère.
    assert len(vocab) == 0
    next(gen)
    assert len(vocab) == 1


def test_empty_text_yields_nothing():
    vocab = Vocabulary()
    assert list(stream_tokens("", vocab)) == []
    assert len(vocab) == 0
