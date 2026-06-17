from typing import get_overloads

from solution_user import decode


def test_behavior_decode_int():
    assert decode(1) == "the"
    assert decode(2) == "cat"


def test_behavior_decode_list():
    assert decode([1, 2, 3]) == ["the", "cat", "sat"]


def test_behavior_decode_empty_list():
    assert decode([]) == []


def test_form_two_overloads_registered():
    assert len(get_overloads(decode)) >= 2
