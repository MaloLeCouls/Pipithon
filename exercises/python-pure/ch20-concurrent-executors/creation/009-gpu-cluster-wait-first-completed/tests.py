from solution_user import race


def test_fastest_wins():
    # replica "c" a le plus petit delay → on attend "answer:c"
    result = race([("a", 0.05), ("b", 0.03), ("c", 0.005)])
    assert result == "answer:c"


def test_single_replica():
    assert race([("only", 0.0)]) == "answer:only"


def test_two_replicas():
    result = race([("slow", 0.05), ("fast", 0.001)])
    assert result == "answer:fast"
