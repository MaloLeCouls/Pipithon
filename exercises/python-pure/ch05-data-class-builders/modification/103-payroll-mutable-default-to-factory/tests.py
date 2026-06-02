from solution_user import Payslip


def test_default_bonuses_empty():
    p = Payslip("E1", 1000.0)
    assert p.bonuses == []


def test_total_with_bonuses():
    assert Payslip("E1", 1000.0, [100.0, 50.0]).total() == 1150.0


def test_total_without_bonuses():
    assert Payslip("E1", 1000.0).total() == 1000.0


def test_default_not_shared():
    a = Payslip("E1", 1000.0)
    b = Payslip("E2", 2000.0)
    a.bonuses.append(42.0)
    assert b.bonuses == []


def test_is_a_dataclass():
    assert "__dataclass_fields__" in vars(Payslip)
