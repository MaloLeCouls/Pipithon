from solution_user import Employee


def test_sort_by_salary():
    emps = [Employee(5000, "Sam"), Employee(3000, "Lee"), Employee(4000, "Ana")]
    assert [e.name for e in sorted(emps)] == ["Lee", "Ana", "Sam"]


def test_comparison_operators():
    assert Employee(3000, "A") < Employee(4000, "B")
    assert Employee(5000, "A") > Employee(4000, "B")


def test_name_excluded_from_comparison():
    # même salaire -> "égaux" pour la comparaison (name ne départage pas)
    assert not (Employee(3000, "Aaa") < Employee(3000, "Zzz"))
    assert not (Employee(3000, "Zzz") < Employee(3000, "Aaa"))


def test_equality_by_compared_fields():
    assert Employee(3000, "X") == Employee(3000, "Y")


def test_stable_sort_preserves_input_order_on_ties():
    # edge : tri stable -> ordre d'entrée conservé à salaire égal
    emps = [Employee(3000, "first"), Employee(3000, "second")]
    assert [e.name for e in sorted(emps)] == ["first", "second"]
