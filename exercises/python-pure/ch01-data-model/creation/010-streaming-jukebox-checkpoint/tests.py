import random

from solution_user import Jukebox, Track

TRACKS = [
    Track("Intro", "Aphex"),
    Track("Bridge", "Boards"),
    Track("Outro", "Zomby"),
]


def test_track_is_namedtuple_like():
    t = Track("X", "Y")
    assert t.title == "X" and t.artist == "Y"
    assert tuple(t) == ("X", "Y")


def test_len():
    assert len(Jukebox(TRACKS)) == 3


def test_indexing_and_negative_index():
    jb = Jukebox(TRACKS)
    assert jb[0].title == "Intro"
    assert jb[-1].title == "Outro"


def test_iteration_for_free():
    assert [t.title for t in Jukebox(TRACKS)] == ["Intro", "Bridge", "Outro"]


def test_contains_for_free():
    jb = Jukebox(TRACKS)
    assert Track("Bridge", "Boards") in jb
    assert Track("Ghost", "Nobody") not in jb


def test_reversed_for_free():
    jb = Jukebox(TRACKS)
    assert [t.title for t in reversed(jb)] == ["Outro", "Bridge", "Intro"]


def test_sorted_and_random_choice_for_free():
    jb = Jukebox(TRACKS)
    assert [t.title for t in sorted(jb)] == ["Bridge", "Intro", "Outro"]
    random.seed(0)
    assert random.choice(jb) in TRACKS


def test_no_manual_iter_or_contains_defined():
    # edge/checkpoint : l'enjeu du chapitre est de NE PAS écrire ces dunders
    assert "__iter__" not in Jukebox.__dict__
    assert "__contains__" not in Jukebox.__dict__
    assert "__reversed__" not in Jukebox.__dict__
