from solution_user import Employee


def test_sort_by_salary_then_name():
    emps = [
        Employee(2000.0, "Zoe"),
        Employee(1500.0, "Alice"),
        Employee(2000.0, "Anna"),
    ]
    ordered = sorted(emps)
    assert [(e.salary, e.name) for e in ordered] == [
        (1500.0, "Alice"),
        (2000.0, "Anna"),
        (2000.0, "Zoe"),
    ]


def test_lt_direct():
    assert Employee(1000.0, "Bob") < Employee(2000.0, "Anna")


def test_eq_still_field_wise():
    assert Employee(1500.0, "Alice") == Employee(1500.0, "Alice")
    assert Employee(1500.0, "Alice") != Employee(1500.0, "Bob")


def test_no_manual_dunder_lt():
    # @dataclass(order=True) doit avoir généré __lt__, pas l'humain.
    assert "__lt__" in vars(Employee)


def test_is_a_dataclass():
    assert "__dataclass_fields__" in vars(Employee)
