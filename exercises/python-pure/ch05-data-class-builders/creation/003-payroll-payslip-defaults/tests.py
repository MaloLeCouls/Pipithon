from solution_user import Payslip


def test_defaults_applied():
    p = Payslip("E1", 3000.0)
    assert p.currency == "EUR"
    assert p.tax_rate == 0.2


def test_required_fields():
    p = Payslip("E1", 3000.0)
    assert p.employee_id == "E1"
    assert p.gross == 3000.0


def test_override_defaults():
    p = Payslip("E2", 5000.0, currency="USD", tax_rate=0.3)
    assert p.currency == "USD"
    assert p.tax_rate == 0.3


def test_eq_with_defaults():
    assert Payslip("E1", 3000.0) == Payslip("E1", 3000.0, "EUR", 0.2)


def test_repr_contains_defaults():
    # edge : le repr généré montre aussi les champs à défaut
    assert "currency='EUR'" in repr(Payslip("E1", 3000.0))
