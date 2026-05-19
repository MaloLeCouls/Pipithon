from solution_user import apply_promo


def test_merge_adds_new_skus():
    assert apply_promo({"A": 10.0}, {"B": 5.0}) == {"A": 10.0, "B": 5.0}


def test_promo_overrides_base():
    assert apply_promo({"A": 10.0, "B": 9.0}, {"A": 7.0}) == {"A": 7.0, "B": 9.0}


def test_inputs_not_mutated():
    base = {"A": 10.0}
    promo = {"A": 7.0}
    apply_promo(base, promo)
    assert base == {"A": 10.0}
    assert promo == {"A": 7.0}


def test_empty_promo_returns_base_copy():
    base = {"A": 1.0}
    out = apply_promo(base, {})
    assert out == {"A": 1.0}
    assert out is not base


def test_override_direction_is_correct():
    # edge : si on inversait les opérandes, A vaudrait 10 (faux)
    assert apply_promo({"A": 10.0}, {"A": 7.0})["A"] == 7.0
