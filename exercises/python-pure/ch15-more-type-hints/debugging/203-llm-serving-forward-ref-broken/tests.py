from solution_user import BatchBuffer, inspect_buffer_hints


def test_inspect_does_not_raise():
    """Le starter lève NameError ici."""
    inspect_buffer_hints()


def test_items_hint_resolved():
    hints = inspect_buffer_hints()
    assert "items" in hints


def test_class_still_usable():
    b = BatchBuffer([1, 2, 3])
    assert b.items == [1, 2, 3]


def test_hint_is_a_list_type():
    """Vérifie que items est typé comme un list-like."""
    hints = inspect_buffer_hints()
    items_hint = hints["items"]
    # Avec PEP 585, list[int] est un GenericAlias — son origine est `list`.
    import typing
    origin = typing.get_origin(items_hint)
    assert origin is list
