import ast
import inspect

from solution_user import batch_hashes, hash_payload


def test_behavior_results_correct():
    payloads = ["a", "ab", "abc"]
    expected = [hash_payload(p) for p in payloads]
    assert batch_hashes(payloads) == expected


def test_behavior_empty():
    assert batch_hashes([]) == []


def test_form_uses_processpool():
    src = inspect.getsource(batch_hashes)
    tree = ast.parse(src)
    has_ppe = any(
        isinstance(n, ast.Name) and n.id == "ProcessPoolExecutor"
        for n in ast.walk(tree)
    )
    assert has_ppe, "Utilise `ProcessPoolExecutor` pour CPU-bound."


def test_form_no_threadpool():
    src = inspect.getsource(batch_hashes)
    tree = ast.parse(src)
    for n in ast.walk(tree):
        if isinstance(n, ast.Name):
            assert n.id != "ThreadPoolExecutor", "Plus de ThreadPool — CPU-bound = ProcessPool."
