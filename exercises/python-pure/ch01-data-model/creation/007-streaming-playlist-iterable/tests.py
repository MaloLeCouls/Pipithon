from solution_user import Playlist

TRACKS = ["Intro", "Verse", "Bridge", "Outro"]


def test_len():
    assert len(Playlist(TRACKS)) == 4


def test_int_index_returns_element():
    assert Playlist(TRACKS)[1] == "Verse"


def test_iteration_works_without_iter():
    assert list(Playlist(TRACKS)) == TRACKS


def test_in_works_without_contains():
    p = Playlist(TRACKS)
    assert "Bridge" in p
    assert "Nope" not in p


def test_slice_returns_playlist_not_list():
    sub = Playlist(TRACKS)[1:3]
    assert isinstance(sub, Playlist)
    assert list(sub) == ["Verse", "Bridge"]


def test_reversed_works_for_free():
    # edge case : reversed() marche aussi via len + getitem
    assert list(reversed(Playlist(TRACKS))) == ["Outro", "Bridge", "Verse", "Intro"]
