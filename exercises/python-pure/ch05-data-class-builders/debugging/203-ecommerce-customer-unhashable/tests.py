from solution_user import Customer, dedupe_customers


def test_dedupe_preserves_order():
    a = Customer("C1", "a@x.com")
    b = Customer("C2", "b@x.com")
    a2 = Customer("C1", "a@x.com")
    assert dedupe_customers([a, b, a2]) == [a, b]


def test_customer_hashable_in_set():
    c = Customer("C1", "a@x.com")
    assert c in {Customer("C1", "a@x.com")}


def test_customer_usable_as_dict_key():
    c = Customer("C1", "a@x.com")
    d = {c: 1}
    assert d[Customer("C1", "a@x.com")] == 1


def test_eq_field_wise():
    assert Customer("C1", "a@x.com") == Customer("C1", "a@x.com")
    assert Customer("C1", "a@x.com") != Customer("C1", "b@x.com")


def test_empty_input():
    assert dedupe_customers([]) == []
