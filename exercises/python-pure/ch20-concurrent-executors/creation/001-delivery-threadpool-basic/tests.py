from solution_user import track_all


def test_returns_results_in_order():
    assert track_all(["A", "B", "C"]) == [
        "shipped:A",
        "shipped:B",
        "shipped:C",
    ]


def test_empty_input():
    assert track_all([]) == []


def test_single_id():
    assert track_all(["X"]) == ["shipped:X"]


def test_handles_many_ids():
    result = track_all([f"PKG-{i}" for i in range(20)])
    assert len(result) == 20
    assert result[0] == "shipped:PKG-0"
    assert result[-1] == "shipped:PKG-19"


def test_uses_threadpool():
    import ast
    import inspect
    import solution_user
    tree = ast.parse(inspect.getsource(solution_user))
    has_tpe = any(
        isinstance(n, ast.Name) and n.id == "ThreadPoolExecutor"
        for n in ast.walk(tree)
    )
    assert has_tpe, "Utilise `ThreadPoolExecutor`."
