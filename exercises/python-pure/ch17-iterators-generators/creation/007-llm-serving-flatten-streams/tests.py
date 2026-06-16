import collections.abc as abc

from pymistral import Token
from solution_user import flatten_streams


def make_stream(prefix: str, n: int):
    for i in range(n):
        yield Token(id=i, text=f"{prefix}{i}")


def test_concatenates_in_order():
    flat = flatten_streams([make_stream("A", 2), make_stream("B", 3)])
    texts = [t.text for t in flat]
    assert texts == ["A0", "A1", "B0", "B1", "B2"]


def test_returns_iterator_lazy():
    flat = flatten_streams([make_stream("X", 1)])
    assert isinstance(flat, abc.Iterator)


def test_streams_is_iterated_once():
    # On passe un GENERATOR de streams (usage unique). flatten_streams ne
    # doit pas tenter de le ré-itérer.
    def streams_gen():
        yield make_stream("A", 1)
        yield make_stream("B", 1)

    texts = [t.text for t in flatten_streams(streams_gen())]
    assert texts == ["A0", "B0"]


def test_empty_streams():
    assert list(flatten_streams([])) == []


def test_streams_with_empty_substream_skipped():
    flat = flatten_streams([make_stream("A", 1), make_stream("Z", 0), make_stream("B", 2)])
    assert [t.text for t in flat] == ["A0", "B0", "B1"]
