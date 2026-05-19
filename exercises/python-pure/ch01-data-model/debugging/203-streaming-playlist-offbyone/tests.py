from solution_user import Playlist

TRACKS = ["Intro", "Verse", "Bridge", "Outro"]


def test_first_element():
    assert Playlist(TRACKS)[0] == "Intro"


def test_last_element():
    assert Playlist(TRACKS)[3] == "Outro"


def test_len_correct():
    assert len(Playlist(TRACKS)) == 4


def test_iteration_complete_and_ordered():
    assert list(Playlist(TRACKS)) == TRACKS


def test_negative_index():
    assert Playlist(TRACKS)[-1] == "Outro"


def test_single_track_playlist():
    # edge : avec 1 seul morceau, les deux off-by-one se voyaient cruellement
    p = Playlist(["Solo"])
    assert len(p) == 1
    assert p[0] == "Solo"
    assert list(p) == ["Solo"]
