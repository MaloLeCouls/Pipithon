from solution_user import add_tags_safely


def test_returns_new_tuple_with_concatenated_tags():
    t = (42, ["urgent"])
    result = add_tags_safely(t, ["backend"])
    assert result == (42, ["urgent", "backend"])


def test_original_ticket_unchanged():
    t = (42, ["urgent"])
    add_tags_safely(t, ["backend"])
    assert t == (42, ["urgent"])


def test_original_inner_list_unchanged():
    original_tags = ["urgent"]
    t = (42, original_tags)
    add_tags_safely(t, ["backend"])
    assert original_tags == ["urgent"]


def test_returned_list_is_distinct():
    t = (42, ["urgent"])
    result = add_tags_safely(t, ["backend"])
    assert result[1] is not t[1]


def test_empty_new_tags():
    t = (1, ["x"])
    result = add_tags_safely(t, [])
    assert result == (1, ["x"])
    assert result[1] is not t[1]  # toujours une nouvelle liste
