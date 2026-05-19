import ast
import inspect

from solution_user import invert


def test_basic_invert():
    assert invert({"978-1": "Dune", "978-2": "Neuromancer"}) == {
        "Dune": "978-1",
        "Neuromancer": "978-2",
    }


def test_empty():
    assert invert({}) == {}


def test_input_not_mutated():
    src = {"i": "t"}
    invert(src)
    assert src == {"i": "t"}


def test_uses_items_and_dictcomp():
    tree = ast.parse(inspect.getsource(invert))
    assert any(isinstance(n, ast.DictComp) for n in ast.walk(tree)), \
        "utilise une dict comprehension"


def test_duplicate_title_last_isbn_wins():
    # edge : titres homonymes -> dernier isbn (sémantique dict)
    assert invert({"i1": "Sapiens", "i2": "Sapiens"}) == {"Sapiens": "i2"}
