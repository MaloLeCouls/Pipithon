from solution_user import create_task


def test_default_tags_is_empty_list():
    t = create_task("write report")
    assert t["tags"] == []


def test_explicit_tags_preserved():
    t = create_task("ship feature", tags=["urgent", "backend"])
    assert t["tags"] == ["urgent", "backend"]


def test_two_calls_do_not_share_tag_list():
    # le coeur du chapitre : deux appels sans tags ne doivent PAS partager.
    a = create_task("a")
    b = create_task("b")
    a["tags"].append("leaked")
    assert b["tags"] == []


def test_title_is_kept():
    assert create_task("urgent fix")["title"] == "urgent fix"


def test_caller_list_not_aliased():
    # edge case : muter la liste appelante ne doit pas polluer la tâche.
    src = ["a"]
    t = create_task("x", tags=src)
    src.append("b")
    assert t["tags"] == ["a"]
