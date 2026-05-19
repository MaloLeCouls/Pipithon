import pytest

from solution_user import split_route


def test_many_stops():
    first, middle, last = split_route(["Depot", "A", "B", "C", "Client"])
    assert first == "Depot"
    assert middle == ["A", "B", "C"]
    assert last == "Client"


def test_exactly_two_stops_empty_middle():
    first, middle, last = split_route(["Depot", "Client"])
    assert first == "Depot"
    assert middle == []
    assert last == "Client"


def test_middle_is_a_list():
    _, middle, _ = split_route(["Depot", "X", "Client"])
    assert isinstance(middle, list)


def test_one_stop_raises():
    with pytest.raises(ValueError, match="route trop courte"):
        split_route(["Depot"])


def test_empty_route_raises():
    # edge : route vide aussi rejetée proprement
    with pytest.raises(ValueError, match="route trop courte"):
        split_route([])
