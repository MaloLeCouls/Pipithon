from solution_user import mutation_is_shared, rebind_is_isolated


def test_mutation_is_shared_returns_true():
    assert mutation_is_shared(["A1", "B2"]) is True


def test_mutation_is_shared_actually_mutates():
    cat = ["A1", "B2"]
    mutation_is_shared(cat)
    assert "EXTRA" in cat


def test_rebind_is_isolated_returns_true():
    assert rebind_is_isolated(["A1", "B2"]) is True


def test_rebind_does_not_mutate_input():
    cat = ["A1", "B2"]
    rebind_is_isolated(cat)
    assert cat == ["A1", "B2"]


def test_empty_inputs_are_safe():
    assert mutation_is_shared([]) is True
    assert rebind_is_isolated([]) is True
