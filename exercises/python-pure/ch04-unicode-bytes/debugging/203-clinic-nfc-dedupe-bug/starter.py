"""count_unique doit compter les patients distincts. Il surcompte : le
même nom saisi avec un 'é' précomposé dans un système et décomposé dans
un autre est vu comme deux patients.
Corrige en chirurgie, sans changer la signature.
"""


def count_unique(names: list[str]) -> int:
    return len(set(names))
