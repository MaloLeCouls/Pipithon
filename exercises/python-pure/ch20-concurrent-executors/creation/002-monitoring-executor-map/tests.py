from solution_user import sample_all


def test_results_in_input_order():
    assert sample_all(["cpu", "mem", "disk"]) == [3, 3, 4]


def test_empty():
    assert sample_all([]) == []


def test_handles_many():
    result = sample_all([str(i) * i for i in range(1, 6)])
    assert result == [1, 2, 3, 4, 5]


def test_uses_executor_map():
    import ast
    import inspect
    import solution_user
    tree = ast.parse(inspect.getsource(solution_user))
    has_map_call = False
    for n in ast.walk(tree):
        if isinstance(n, ast.Attribute) and n.attr == "map":
            has_map_call = True
            break
    assert has_map_call, "Utilise `ex.map(...)`."
