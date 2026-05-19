import ast
import inspect

from solution_user import total_pages


def test_sum_pages():
    books = [{"title": "A", "pages": 100}, {"title": "B", "pages": 250}]
    assert total_pages(books) == 350


def test_single_book():
    assert total_pages([{"title": "X", "pages": 42}]) == 42


def test_empty_library_is_zero():
    assert total_pages([]) == 0


def test_uses_generator_not_list_comp():
    # idiome : sum(genexp), pas sum([listcomp]) ni boucle accumulateur
    tree = ast.parse(inspect.getsource(total_pages))
    assert not any(isinstance(n, ast.ListComp) for n in ast.walk(tree)), \
        "pas de list comprehension : passe une generator expression à sum()"
    assert any(isinstance(n, ast.GeneratorExp) for n in ast.walk(tree)), \
        "utilise une generator expression"


def test_large_input():
    # edge : doit rester correct et lazy sur beaucoup de livres
    books = [{"title": str(i), "pages": 1} for i in range(10_000)]
    assert total_pages(books) == 10_000
