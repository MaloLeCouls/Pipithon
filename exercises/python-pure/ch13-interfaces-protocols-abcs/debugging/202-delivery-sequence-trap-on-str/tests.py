import pytest

from solution_user import route


def test_accepts_list():
    assert route(["A", "B", "C"]) == "A -> B -> C"


def test_accepts_tuple():
    assert route(("X", "Y")) == "X -> Y"


def test_rejects_str():
    # Le starter passe la chaîne par silence et produit "1 -> 2 -> 3 -> ...".
    # La solution doit lever TypeError.
    with pytest.raises(TypeError):
        route("123 Main St")


def test_rejects_bytes():
    with pytest.raises(TypeError):
        route(b"raw")


def test_rejects_int():
    with pytest.raises(TypeError):
        route(42)
