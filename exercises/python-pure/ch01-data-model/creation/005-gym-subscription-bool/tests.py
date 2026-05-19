from solution_user import Subscription


def test_active_subscription_is_truthy():
    assert bool(Subscription(30)) is True


def test_used_if_statement():
    assert "actif" if Subscription(1) else "expiré"


def test_zero_days_is_falsy():
    assert bool(Subscription(0)) is False


def test_bool_returns_actual_bool():
    assert type(bool(Subscription(5))) is bool


def test_negative_days_is_falsy():
    # edge case : un compteur négatif (bug amont) ne doit pas paraître actif
    assert bool(Subscription(-3)) is False
