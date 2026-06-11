import inspect

from solution_user import apply


def test_no_coupon_returns_price():
    assert apply(100) == 100


def test_coupon_applies_discount():
    assert apply(100, "PROMO10") == 90


def test_annotation_mentions_none():
    sig = inspect.signature(apply)
    ann = str(sig.parameters["coupon"].annotation)
    assert "None" in ann, f"coupon doit accepter None dans son type ({ann})"


def test_default_is_none():
    sig = inspect.signature(apply)
    assert sig.parameters["coupon"].default is None
