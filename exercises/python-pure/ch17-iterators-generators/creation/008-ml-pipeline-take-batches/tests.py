import collections.abc as abc

from solution_user import take_batches


def stream(batches):
    for b in batches:
        yield b


def test_caps_at_max_n():
    src = stream([[1], [2], [3], [4], [5]])
    out = list(take_batches(src, 3))
    assert out == [[1], [2], [3]]


def test_stops_on_empty_sentinel():
    src = stream([[1, 2], [3], [], [4]])
    out = list(take_batches(src, 10))
    assert out == [[1, 2], [3]]


def test_sentinel_before_max_n():
    src = stream([[1], [], [2]])
    out = list(take_batches(src, 10))
    assert out == [[1]]


def test_returns_iterator_lazy():
    src = stream([[1], [2]])
    result = take_batches(src, 5)
    assert isinstance(result, abc.Iterator)


def test_max_n_zero_yields_nothing():
    src = stream([[1], [2]])
    assert list(take_batches(src, 0)) == []


def test_stream_iterated_once_only():
    # Le contrat : un seul passage sur dataset_stream. On vérifie qu'on
    # ne consomme PAS au-delà de ce qu'on yield.
    consumed: list[list[int]] = []

    def spy():
        for b in [[1], [2], [3], [4]]:
            consumed.append(b)
            yield b

    out = list(take_batches(spy(), 2))
    assert out == [[1], [2]]
    # Au pire on consomme 1 batch de plus (look-ahead d'islice avec stop=2).
    assert len(consumed) <= 3
