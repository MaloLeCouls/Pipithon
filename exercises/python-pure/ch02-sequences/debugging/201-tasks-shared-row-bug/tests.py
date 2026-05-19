from solution_user import assign, new_board


def test_board_shape():
    assert new_board(3) == [[], [], []]


def test_assign_isolated_to_one_lane():
    b = new_board(3)
    assign(b, 0, "deploy")
    assert b[0] == ["deploy"]
    assert b[1] == []
    assert b[2] == []


def test_independent_lanes_multiple_assigns():
    b = new_board(3)
    assign(b, 0, "a")
    assign(b, 2, "b")
    assert b == [["a"], [], ["b"]]


def test_lanes_are_distinct_objects():
    b = new_board(3)
    assert b[0] is not b[1]


def test_zero_and_one_lane_edge():
    # edge : 0 voie -> [] ; 1 voie -> reste isolée
    assert new_board(0) == []
    b = new_board(1)
    assign(b, 0, "x")
    assert b == [["x"]]
