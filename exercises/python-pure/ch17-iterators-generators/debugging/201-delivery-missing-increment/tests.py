import pytest

from solution_user import Package, PackageStream


def make_stream() -> PackageStream:
    return PackageStream([
        Package("TRK-1", "delivered"),
        Package("TRK-2", "pending"),
        Package("TRK-3", "delivered"),
    ])


def test_iterates_all_then_stops():
    ids = [p.tracking_id for p in make_stream()]
    assert ids == ["TRK-1", "TRK-2", "TRK-3"]


def test_stopiteration_after_end():
    it = iter(make_stream())
    for _ in range(3):
        next(it)
    with pytest.raises(StopIteration):
        next(it)


def test_each_next_advances():
    it = iter(make_stream())
    assert next(it).tracking_id == "TRK-1"
    assert next(it).tracking_id == "TRK-2"
    assert next(it).tracking_id == "TRK-3"


def test_empty_stream_stops_immediately():
    it = iter(PackageStream([]))
    with pytest.raises(StopIteration):
        next(it)


def test_does_not_loop_forever():
    # Edge case : sans le fix, ce list() ne se terminerait jamais. La
    # validation aurait alors un timeout (= échec — exactement ce qu'on veut
    # pour le starter).
    result = list(make_stream())
    assert len(result) == 3
