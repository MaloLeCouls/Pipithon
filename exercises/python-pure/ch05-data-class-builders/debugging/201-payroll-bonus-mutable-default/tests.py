from solution_user import Payslip


def test_default_bonuses_empty():
    assert Payslip("E1", 1000.0).bonuses == []


def test_total_with_bonuses():
    assert Payslip("E1", 1000.0, [100.0, 50.0]).total() == 1150.0


def test_defaults_not_shared_between_instances():
    a = Payslip("E1", 1000.0)
    b = Payslip("E2", 2000.0)
    a.bonuses.append(10.0)
    assert b.bonuses == []


def test_explicit_bonuses_preserved():
    p = Payslip("E1", 1000.0, [42.0])
    assert p.bonuses == [42.0]
