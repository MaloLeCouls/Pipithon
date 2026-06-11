from solution_user import make_task_factories


def test_each_factory_returns_its_own_index():
    factories = make_task_factories(5)
    assert [f() for f in factories] == [0, 1, 2, 3, 4]


def test_zero_factories():
    assert make_task_factories(0) == []


def test_one_factory():
    factories = make_task_factories(1)
    assert factories[0]() == 0


def test_factories_are_distinct_callables():
    factories = make_task_factories(3)
    # ce sont des fonctions distinctes même si elles capturent un scope partagé.
    assert factories[0] is not factories[1]


def test_large_n_no_leak():
    factories = make_task_factories(100)
    assert [f() for f in factories] == list(range(100))
