import inspect

from solution_user import driver_label


def test_string_driver_uppercased():
    assert driver_label("alice") == "ALICE"


def test_none_returns_unassigned():
    assert driver_label(None) == "unassigned"


def test_annotation_includes_none():
    sig = inspect.signature(driver_label)
    ann = str(sig.parameters["driver"].annotation)
    assert "None" in ann, f"annotation doit mentionner None ({ann})"
