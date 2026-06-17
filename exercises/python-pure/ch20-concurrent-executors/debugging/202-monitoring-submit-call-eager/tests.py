from solution_user import sample_all


def test_basic_three():
    assert sample_all(["cpu", "mem", "disk"]) == [3, 3, 4]


def test_empty():
    assert sample_all([]) == []


def test_does_not_raise_typeerror():
    """Le starter lève TypeError car ex.submit(int) tente d'appeler un int."""
    sample_all(["x"])  # ne doit PAS lever
