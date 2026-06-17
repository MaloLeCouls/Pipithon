from solution_user import (
    download_robust,
    download_sequential,
    download_threaded,
)


CLEAN = ["A", "BB", "CCC", "DDDD"]


def test_sequential_clean():
    assert download_sequential(CLEAN) == (4, [])


def test_threaded_clean():
    assert download_threaded(CLEAN) == (4, [])


def test_robust_clean():
    assert download_robust(CLEAN) == (4, [])


def test_sequential_with_errors():
    success, failed = download_sequential(["A", "BROKEN", "B"])
    assert success == 2
    assert failed == ["BROKEN"]


def test_robust_with_errors():
    success, failed = download_robust(["A", "BROKEN", "B"])
    assert success == 2
    assert failed == ["BROKEN"]


def test_robust_with_multiple_errors():
    success, failed = download_robust(["A", "BROKEN", "B", "BROKEN", "C"])
    assert success == 3
    assert sorted(failed) == ["BROKEN", "BROKEN"]


def test_all_three_agree_on_clean_input():
    seq = download_sequential(CLEAN)
    thr = download_threaded(CLEAN)
    rob = download_robust(CLEAN)
    assert seq == thr == rob


def test_empty_inputs():
    assert download_sequential([]) == (0, [])
    assert download_threaded([]) == (0, [])
    assert download_robust([]) == (0, [])


def test_robust_uses_as_completed_and_exception():
    import ast
    import inspect
    src = inspect.getsource(download_robust)
    tree = ast.parse(src)
    has_as_completed = any(
        isinstance(n, ast.Name) and n.id == "as_completed" for n in ast.walk(tree)
    )
    has_exception = any(
        isinstance(n, ast.Attribute) and n.attr == "exception" for n in ast.walk(tree)
    )
    assert has_as_completed, "download_robust doit utiliser as_completed."
    assert has_exception, "download_robust doit utiliser fut.exception()."
