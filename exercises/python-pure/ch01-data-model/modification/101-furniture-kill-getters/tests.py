import inspect

from solution_user import Chair


def test_behavior_attributes_preserved():
    c = Chair("A1", 99)
    assert c.ref == "A1"
    assert c.price == 99


def test_repr_added():
    assert repr(Chair("A1", 99)) == "Chair(ref='A1', price=99)"


def test_getters_removed():
    assert not hasattr(Chair, "get_ref"), "get_ref doit disparaître"
    assert not hasattr(Chair, "get_price"), "get_price doit disparaître"


def test_class_is_lean():
    # forme : seules __init__ et __repr__ (pas de getters réintroduits)
    methods = {n for n, _ in inspect.getmembers(Chair, inspect.isfunction)}
    assert methods == {"__init__", "__repr__"}, f"méthodes inattendues : {methods}"


def test_repr_handles_apostrophe_ref():
    # edge case : refactor robuste, pas un f-string manuel fragile
    assert repr(Chair("O'1", 5)) == 'Chair(ref="O\'1", price=5)'
