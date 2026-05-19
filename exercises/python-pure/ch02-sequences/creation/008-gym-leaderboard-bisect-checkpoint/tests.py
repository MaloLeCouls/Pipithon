import ast
import inspect

from solution_user import Leaderboard, grade


def test_grade_boundaries():
    assert grade(0) == "F"
    assert grade(59) == "F"
    assert grade(60) == "E"
    assert grade(69) == "E"
    assert grade(70) == "D"
    assert grade(85) == "C"
    assert grade(99) == "B"
    assert grade(100) == "A"
    assert grade(250) == "A"


def test_grade_uses_bisect_not_if_chain():
    tree = ast.parse(inspect.getsource(grade))
    ifs = [n for n in ast.walk(tree) if isinstance(n, ast.If)]
    assert not ifs, "grade() doit utiliser une table + bisect, pas des if/elif"


def test_leaderboard_keeps_sorted():
    lb = Leaderboard()
    for s in (50, 90, 10, 70, 30):
        lb.add(s)
    assert lb.scores() == [10, 30, 50, 70, 90]


def test_top_count():
    lb = Leaderboard()
    for s in (10, 30, 50, 70, 90):
        lb.add(s)
    assert lb.top_count(50) == 2   # 70, 90
    assert lb.top_count(90) == 0
    assert lb.top_count(5) == 5


def test_scores_returns_defensive_copy():
    lb = Leaderboard()
    lb.add(42)
    lb.scores().append(999)
    assert lb.scores() == [42]


def test_duplicates_and_empty():
    # edge : doublons gardés, classement vide cohérent
    lb = Leaderboard()
    assert lb.scores() == []
    assert lb.top_count(0) == 0
    lb.add(50)
    lb.add(50)
    assert lb.scores() == [50, 50]
    assert lb.top_count(49) == 2
    assert lb.top_count(50) == 0
