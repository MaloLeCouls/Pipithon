"""Le serveur d'inférence coupe son stream de tokens dès qu'il croise le
token EOS (`end-of-sequence`). C'est fait à la main avec une boucle + un
`return` à l'intérieur — ça marche, mais `itertools.takewhile` exprime
exactement cette intention en une ligne.

Refactor `gen_until_eos(stream, eos_id)` :
- conserve la signature et le comportement (stop avant le token EOS).
- remplace la boucle + return par un appel à `itertools.takewhile`.
- la fonction n'a plus besoin de `yield` : elle retourne directement
  l'iterator produit par `takewhile`."""
from __future__ import annotations

from collections.abc import Iterable, Iterator

from pymistral import Token


def gen_until_eos(stream: Iterable[Token], eos_id: int) -> Iterator[Token]:
    for tok in stream:
        if tok.id == eos_id:
            return
        yield tok
