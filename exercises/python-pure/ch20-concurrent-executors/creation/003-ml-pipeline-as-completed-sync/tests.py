from solution_user import order_by_completion


def test_order_inverted_delays():
    # Index 2 (delay 0.005) doit finir AVANT index 0 (delay 0.05).
    result = order_by_completion([0.05, 0.03, 0.005])
    assert result[0] == 2


def test_empty_input():
    assert order_by_completion([]) == []


def test_all_indices_present():
    result = order_by_completion([0.01, 0.02, 0.005, 0.0, 0.015])
    assert sorted(result) == [0, 1, 2, 3, 4]


def test_smallest_delay_first():
    result = order_by_completion([0.01, 0.0, 0.02])
    assert result[0] == 1
