"""Choix de design (correctif) :
- Une exception remontant du bloc `with` est *injectée* au point du `yield`
  dans le générateur décoré. Sans `try/finally` autour du yield, tout ce
  qui suit le yield est sauté.
- Le contrat des CMs étant *« cleanup garanti »*, le `try/finally` est
  obligatoire — c'est la version @contextmanager du `__exit__` toujours
  appelé par le `with`.
"""
from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager


class Session:
    def __init__(self, session_id: str) -> None:
        self.session_id = session_id
        self.state: str = "idle"


@contextmanager
def inference_window(session: Session) -> Iterator[Session]:
    session.state = "active"
    try:
        yield session
    finally:
        session.state = "idle"
