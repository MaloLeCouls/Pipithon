from solution_user import Trackable, is_trackable


class Package:
    def track(self) -> str:
        return "in_transit"


class Letter:
    def track(self) -> str:
        return "delivered"


class Garbage:
    """Pas de méthode `track` — ne satisfait pas le protocol."""

    def label(self) -> str:
        return "trash"


def test_is_trackable_true_for_package():
    assert is_trackable(Package()) is True


def test_is_trackable_true_for_letter():
    assert is_trackable(Letter()) is True


def test_is_trackable_false_for_garbage():
    assert is_trackable(Garbage()) is False


def test_is_trackable_false_for_builtin_int():
    assert is_trackable(42) is False


def test_protocol_is_runtime_checkable():
    # Si Trackable n'est pas runtime_checkable, isinstance lèverait TypeError.
    isinstance(object(), Trackable)  # ne doit PAS lever


def test_isinstance_only_checks_presence_not_signature():
    """Piège du chapitre : signature ignorée."""

    class FakeTracker:
        def track(self) -> int:  # mauvais type, mais runtime_checkable l'accepte
            return 0

    assert is_trackable(FakeTracker()) is True
