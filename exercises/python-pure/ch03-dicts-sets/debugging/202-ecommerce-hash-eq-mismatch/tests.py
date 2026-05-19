from solution_user import Coupon


def test_equality_still_holds():
    assert Coupon("SAVE10", 10) == Coupon("SAVE10", 10)
    assert Coupon("SAVE10", 10) != Coupon("SAVE10", 20)


def test_hash_consistent_with_eq():
    a, b = Coupon("SAVE10", 10), Coupon("SAVE10", 10)
    assert a == b
    assert hash(a) == hash(b)


def test_set_deduplicates():
    s = {Coupon("SAVE10", 10), Coupon("SAVE10", 10), Coupon("VIP", 50)}
    assert len(s) == 2


def test_dict_lookup_by_value():
    d = {Coupon("SAVE10", 10): "active"}
    assert d[Coupon("SAVE10", 10)] == "active"


def test_distinct_coupons_kept():
    # edge : des coupons réellement différents ne fusionnent pas
    s = {Coupon("A", 5), Coupon("A", 10)}
    assert len(s) == 2
