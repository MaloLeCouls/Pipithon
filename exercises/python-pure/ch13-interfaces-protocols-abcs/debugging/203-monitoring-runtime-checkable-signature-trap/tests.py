from solution_user import BadProbe, Probe, sample


def test_isinstance_passes():
    # Avec runtime_checkable, on a un faux positif sur le starter (signature mauvaise)
    # mais isinstance reste True dans les deux cas.
    assert isinstance(BadProbe(), Probe)


def test_sample_returns_a_float():
    """Le starter lève TypeError ici (missing 'source')."""
    result = sample(BadProbe())
    assert isinstance(result, float)


def test_sample_value_is_42():
    # Choix arbitraire de la solution, mais marque l'alignement avec le Protocol.
    assert sample(BadProbe()) == 42.0


def test_can_pass_to_sample_with_no_extra_args():
    """Confirme que la signature `read(self) -> float` est respectée."""
    bp = BadProbe()
    bp.read()  # ne doit PAS lever TypeError
