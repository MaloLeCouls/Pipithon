import inspect

from solution_user import total


def test_total_of_multiple_prices():
    assert total((10, 20, 30)) == 60


def test_total_of_empty():
    assert total(()) == 0


def test_total_of_single():
    assert total((42,)) == 42


def test_annotation_is_variable_length_tuple():
    sig = inspect.signature(total)
    ann = str(sig.parameters["prices"].annotation)
    assert "..." in ann, f"utilise tuple[int, ...] (longueur variable) : {ann}"
