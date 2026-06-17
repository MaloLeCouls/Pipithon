from solution_user import batch_hashes, hash_job


def test_results_in_order():
    payloads = ["a", "ab", "abc"]
    expected = [hash_job(p) for p in payloads]
    assert batch_hashes(payloads) == expected


def test_empty_input():
    assert batch_hashes([]) == []


def test_single_payload():
    assert batch_hashes(["x"]) == [hash_job("x")]


def test_uses_processpool():
    import ast
    import inspect
    import solution_user
    tree = ast.parse(inspect.getsource(solution_user))
    has_ppe = any(
        isinstance(n, ast.Name) and n.id == "ProcessPoolExecutor"
        for n in ast.walk(tree)
    )
    assert has_ppe, "Utilise `ProcessPoolExecutor`, pas ThreadPool."
