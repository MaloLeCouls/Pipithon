"""Ce code numérote des tâches avec le grand classique non-pythonique
`for i in range(len(...))`.

Refactor `numbered` :
- même sortie exactement,
- utilise enumerate (start=1), en une list comprehension,
- ni range(), ni indexation tasks[i].
"""


def numbered(tasks: list[str]) -> list[str]:
    out = []
    for i in range(len(tasks)):
        out.append(f"{i + 1}. {tasks[i]}")
    return out
