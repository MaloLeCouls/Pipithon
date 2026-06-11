import inspect

from solution_user import titles


def test_titles_from_list():
    assert titles([{"title": "a"}, {"title": "b"}]) == ["a", "b"]


def test_titles_from_generator():
    gen = ({"title": s} for s in "xy")
    assert titles(gen) == ["x", "y"]


def test_titles_from_tuple():
    assert titles(({"title": "z"},)) == ["z"]


def test_annotation_uses_iterable_not_list():
    sig = inspect.signature(titles)
    ann = str(sig.parameters["tasks"].annotation)
    assert "Iterable" in ann, f"utilise Iterable, pas list ({ann})"
