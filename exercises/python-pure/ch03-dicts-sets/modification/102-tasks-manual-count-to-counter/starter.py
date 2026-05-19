"""Ce code compte les tags à la main.

Refactor `tag_counts` avec collections.Counter :
- même résultat (un mapping {tag: nombre}),
- plus de if/else de comptage manuel.
"""


def tag_counts(tasks: list[dict]) -> dict[str, int]:
    counts = {}
    for t in tasks:
        for tag in t["tags"]:
            if tag in counts:
                counts[tag] += 1
            else:
                counts[tag] = 1
    return counts
