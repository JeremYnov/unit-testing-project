
import pytest
# Basic examples to understand parameterizing
# Let's have `add` function to test with int, string and float ? 
def add(x, y):
    '''
    >>> add(7, 3)
    10
    >>> add('Hello', ' World')
    'Hello World'
    >>> add(10.5, 24.5)
    35.0
    '''
    return x + y

# Au passage, je rappelle du mécanisme du doctest ? 
# python -m doctest -v test_parameter.py


def test_add_int():
    assert add(7, 3) == 10

def test_add_string():
    assert add('Hello', ' World') == 'Hello World'

def test_add_float():
    assert add(10.5, 24.5) == 35

# Exemple d'un test erroné
def test_add_int_error():
    assert math_func.add(7, 3) == 10


# Cmnt économiser les 3 tests en un et un seul test ? 
# 1è sol : On peut mettre plusieurs assert (mais ce n'est pas la sol la plus élégante)
def test_add_naif():
    assert add(7, 3) == 10
    assert add('Hello', ' World') == 'Hello World'
    assert add(10.5, 24.5) == 35   

# 2è sol (efficace) : paramétrer le test
# Les diff param sont indiqués ds une string et les diff values sont stockées ds une liste de tuples
@pytest.mark.parametrize('x, y, result', [(7, 3, 10), ('Hello', ' World', 'Hello World'), (10.5, 24.5, 35)])
def test_add_param(x, y, result):
    assert add(x, y) == result