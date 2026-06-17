import pytest

from solution_user import Task


def test_default_format():
    assert format(Task("Ship MVP", "doing")) == "Ship MVP [doing]"


def test_short_format():
    assert format(Task("Ship MVP", "doing"), "short") == "Ship MVP"


def test_full_format():
    assert format(Task("Ship MVP", "doing"), "full") == "Ship MVP (DOING)"


def test_unknown_spec_raises():
    with pytest.raises(ValueError, match="Unknown format spec"):
        format(Task("X", "todo"), "bogus")


def test_works_in_f_string():
    t = Task("Refactor", "done")
    assert f"{t:short}" == "Refactor"
    assert f"{t:full}" == "Refactor (DONE)"


def test_str_delegates_to_format():
    assert str(Task("A", "todo")) == "A [todo]"
