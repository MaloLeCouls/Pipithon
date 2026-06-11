from solution_user import Package, same_data, same_object


def test_same_object_true_for_alias():
    p = Package("X1", 1.2)
    alias = p
    assert same_object(p, alias) is True


def test_same_object_false_for_distinct_instances():
    a = Package("X1", 1.2)
    b = Package("X1", 1.2)
    assert same_object(a, b) is False


def test_same_data_true_for_equal_attrs():
    a = Package("X1", 1.2)
    b = Package("X1", 1.2)
    assert same_data(a, b) is True


def test_same_data_false_for_different_weight():
    a = Package("X1", 1.2)
    b = Package("X1", 1.3)
    assert same_data(a, b) is False


def test_returns_bool_not_string():
    p = Package("X1", 1.2)
    assert isinstance(same_object(p, p), bool)
    assert isinstance(same_data(p, p), bool)
