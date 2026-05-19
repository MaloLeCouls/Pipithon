import pytest

from solution_user import Invoice


def test_total_computed():
    inv = Invoice("F1", [(2, 10.0), (1, 5.5)])
    assert inv.total == 25.5


def test_empty_lines_total_zero():
    assert Invoice("F2", []).total == 0.0


def test_total_not_a_constructor_arg():
    # field(init=False) : passer total en positionnel doit échouer
    with pytest.raises(TypeError):
        Invoice("F3", [(1, 1.0)], 999.0)


def test_fields_kept():
    inv = Invoice("F1", [(1, 2.0)])
    assert inv.invoice_id == "F1"
    assert inv.lines == [(1, 2.0)]


def test_repr_contains_total():
    # edge : le total dérivé apparaît dans le repr généré
    assert "total=" in repr(Invoice("F1", [(1, 2.0)]))
