from solution_user import Chair


def test_tags_are_per_instance():
    a = Chair("A")
    b = Chair("B")
    a.add_tag("oak")
    assert a.tags == ["oak"]
    assert b.tags == [], "B doit avoir SA propre liste (vide)."


def test_two_instances_have_distinct_lists():
    a = Chair("A")
    b = Chair("B")
    assert a.tags is not b.tags, "Les listes doivent être des objets distincts."


def test_form_no_class_level_tags_list():
    """Le starter a `tags = []` au niveau classe ; la solution non."""
    # On vérifie que Chair.__dict__ ne contient PAS de `tags` (= attribut classe).
    assert "tags" not in Chair.__dict__, \
        "Plus de `tags` au niveau classe — l'init doit créer une liste par instance."


def test_add_tag_works():
    c = Chair("X")
    c.add_tag("metal")
    c.add_tag("steel")
    assert c.tags == ["metal", "steel"]
