from solution_user import assign, new_board


def test_board_has_right_number_of_lanes():
    assert new_board(3) == [[], [], []]


def test_assign_adds_to_target_lane():
    b = new_board(3)
    assign(b, 0, "deploy")
    assert b[0] == ["deploy"]


def test_lanes_are_independent():
    # cœur du piège : les voies ne doivent PAS partager la même liste
    b = new_board(3)
    assign(b, 0, "deploy")
    assert b[1] == []
    assert b[2] == []


def test_multiple_assignments():
    b = new_board(2)
    assign(b, 0, "spec")
    assign(b, 0, "code")
    assign(b, 1, "review")
    assert b == [["spec", "code"], ["review"]]


def test_two_boards_are_independent():
    # edge : deux boards distincts ne partagent rien
    a = new_board(2)
    b = new_board(2)
    assign(a, 0, "x")
    assert b == [[], []]


def test_zero_lanes():
    # edge : board sans voie = liste vide, pas d'erreur
    assert new_board(0) == []
