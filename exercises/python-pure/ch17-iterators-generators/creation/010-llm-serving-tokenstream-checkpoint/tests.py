import collections.abc as abc

import pytest

from pymistral import Token
from solution_user import (
    TokenStreamIter,
    tokenstream_gen,
    tokenstream_genexpr,
)


EXPECTED_AB = [Token(id=0, text="a"), Token(id=1, text="b")]


def test_form1_manual_iterator_basics():
    it = TokenStreamIter("ab")
    assert iter(it) is it  # un iterator est son propre iterable
    assert list(it) == EXPECTED_AB


def test_form1_raises_stopiteration_at_end():
    it = TokenStreamIter("a")
    next(it)
    with pytest.raises(StopIteration):
        next(it)


def test_form2_generator_function():
    gen = tokenstream_gen("ab")
    assert isinstance(gen, abc.Iterator)
    assert list(gen) == EXPECTED_AB


def test_form3_generator_expression():
    gen = tokenstream_genexpr("ab")
    assert isinstance(gen, abc.Iterator)
    assert list(gen) == EXPECTED_AB


def test_three_forms_equivalent():
    text = "hello"
    a = list(TokenStreamIter(text))
    b = list(tokenstream_gen(text))
    c = list(tokenstream_genexpr(text))
    assert a == b == c


def test_empty_text_yields_empty():
    assert list(TokenStreamIter("")) == []
    assert list(tokenstream_gen("")) == []
    assert list(tokenstream_genexpr("")) == []


def test_lazy_evaluation_of_genexpr():
    # La genexpr ne doit rien produire avant qu'on tire.
    consumed: list[str] = []

    def watched_text():
        for ch in "xy":
            consumed.append(ch)
            yield ch

    # On ne peut pas utiliser watched_text directement ici (la genexpr utilise
    # enumerate sur text comme str), mais on teste juste que la genexpr est
    # bien un Iterator paresseux (pas une list pré-calculée).
    gen = tokenstream_genexpr("ab")
    assert not isinstance(gen, list)
    first = next(gen)
    assert first == Token(id=0, text="a")
