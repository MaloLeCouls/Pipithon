import solution_user
from solution_user import compute_total


def test_basic_correct():
    assert compute_total(100, 0.2) == 80.0


def test_cache_attributes_present():
    assert hasattr(compute_total, "cache_info")
    assert hasattr(compute_total, "cache_clear")


def test_no_manual_cache_dict_module_level():
    # le coeur du refactor : pas de _CACHE qui traîne.
    module_attrs = {n for n in dir(solution_user) if not n.startswith("__")}
    assert "_CACHE" not in module_attrs, "supprime le dict _CACHE"


def test_memoization_works():
    compute_total.cache_clear()
    compute_total(100, 0.1)
    compute_total(100, 0.1)
    compute_total(200, 0.1)
    info = compute_total.cache_info()
    assert info.hits == 1
    assert info.misses == 2
