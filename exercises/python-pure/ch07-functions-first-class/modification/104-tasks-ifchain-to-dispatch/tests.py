import ast
import inspect

import pytest

from solution_user import apply_action


def test_close_action():
    assert apply_action({"title": "fix"}, "close") == "closed:fix"


def test_reopen_action():
    assert apply_action({"title": "bug"}, "reopen") == "reopened:bug"


def test_tag_action():
    assert apply_action({"title": "feat"}, "tag") == "tagged:feat"


def test_unknown_action_raises_keyerror():
    with pytest.raises(KeyError):
        apply_action({"title": "x"}, "burn")


def test_no_if_elif_chain_on_action():
    # le coeur du refactor : plus de comparaisons sur `action` dans le corps.
    src = inspect.getsource(apply_action)
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            # quelques `if` triviaux peuvent rester ; on n'autorise pas un
            # if/elif qui compare action == "...".
            test = node.test
            if isinstance(test, ast.Compare):
                for cmp in [test.left, *test.comparators]:
                    if isinstance(cmp, ast.Name) and cmp.id == "action":
                        raise AssertionError("plus de comparaisons sur `action` (utilise un dict)")
