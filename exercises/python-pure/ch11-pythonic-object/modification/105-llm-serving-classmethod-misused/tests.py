import inspect

from solution_user import TokenStats


def test_behavior_valid_id():
    assert TokenStats.validate_id(0) is True
    assert TokenStats.validate_id(42) is True
    assert TokenStats.validate_id(49_999) is True


def test_behavior_invalid_id():
    assert TokenStats.validate_id(-1) is False
    assert TokenStats.validate_id(50_000) is False


def test_form_is_staticmethod_not_classmethod():
    # staticmethod -> inspect.isfunction == True (pas de binding cls)
    # classmethod  -> inspect.ismethod == True
    assert inspect.isfunction(TokenStats.validate_id), \
        "validate_id doit être staticmethod (n'utilise pas cls)."
    assert not inspect.ismethod(TokenStats.validate_id), \
        "validate_id NE doit PAS être classmethod."


def test_form_callable_without_instance():
    # Sans instance, accessible via la classe directement.
    TokenStats.validate_id(10)
