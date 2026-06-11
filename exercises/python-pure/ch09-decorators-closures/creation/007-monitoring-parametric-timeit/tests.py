from solution_user import TIMINGS, timed


def setup_function():
    TIMINGS.clear()


def test_basic_parametric_decoration():
    @timed("hot")
    def add(a, b):
        return a + b
    add(2, 3)
    assert TIMINGS == [("hot", 5)]


def test_label_is_per_function():
    @timed("A")
    def f1():
        return 1
    @timed("B")
    def f2():
        return 2
    f1()
    f2()
    f1()
    assert TIMINGS == [("A", 1), ("B", 2), ("A", 1)]


def test_return_value_preserved():
    @timed("x")
    def double(n):
        return n * 2
    assert double(7) == 14


def test_three_levels_present():
    # Le call timed("...") doit renvoyer une fn (décorateur), pas appliquer direct.
    dec = timed("test")
    assert callable(dec)
    @dec
    def f():
        return 0
    assert callable(f)
