from solution_user import accumulate


def test_two_calls_do_not_share_state():
    a = accumulate(1)
    b = accumulate(2)
    assert a == [1]
    assert b == [2]


def test_explicit_acc_preserved():
    acc: list[int] = [10]
    out = accumulate(20, acc)
    assert out == [10, 20]
    assert out is acc


def test_repeated_default_isolated():
    results = [accumulate(i) for i in range(5)]
    for i, r in enumerate(results):
        assert r == [i], f"appel {i} a vu d'autres features : {r}"
