import solution_user
from solution_user import discount, make_discount


def test_discount_basic():
    assert discount(100, 0.2) == 80.0


def test_make_discount_specializes():
    d = make_discount(0.5)
    assert d(100) == 50.0


def test_class_is_gone():
    # le coeur du refactor : la classe doit être supprimée.
    assert not hasattr(solution_user, "PercentageDiscount"), \
        "supprime la classe PercentageDiscount"


def test_make_discount_returns_callable():
    d = make_discount(0.1)
    assert callable(d)


def test_two_specializations_independent():
    light = make_discount(0.1)
    heavy = make_discount(0.5)
    assert light(100) == 90.0
    assert heavy(100) == 50.0


def test_specialization_uses_partial():
    # un partial a un attribut .func et .keywords.
    d = make_discount(0.25)
    assert hasattr(d, "func") and hasattr(d, "keywords"), \
        "utilise functools.partial"
