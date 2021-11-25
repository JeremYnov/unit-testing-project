## Execute PyTests from command Line ? 
    # Run all tests : pytest -v
    # Disable Warnings (non recomandé) : pytest --disable-warnings -v 

# Run tests and generate report
# pytest --disable-warnings -v --capture sys -rF --capture sys -rP --html=test_report.html --self-contained-html test_example.py


# En CLI, le résultat est plus parlant (comparativement à l'extension VSCode) : 
# -s (Show Output) permet d'afficher les msg des print ; parcq le comportement par défaut de pytest est de ne pas les afficher
# pytest -vs --disable-warnings test_routes.py::test_index_fixt
# pytest -vs --disable-warnings test_routes.py::test_home_fixt
# -k (key word) permet de sélectionner les tests dont le noms matche avec un pattern
# pytest --disable-warnings -vsk "_fixt"


###################################################################################
# Basic Example 1
###################################################################################
import pytest
# pytest --disable-warnings -v test_example.py::test_success
def test_success():
	x=5
	y=6
	assert x+1 == y     #  "test successful"

# pytest --disable-warnings -v test_example.py::test_fail
def test_fail():
	x=5
	y=6
	assert x == y       # "test failed"


###################################################################################
# Basic Example 2
###################################################################################

def add(x, y):
    return x + y

def test_add_int():
    assert add(7, 3) == 10

def test_add_string():
    assert add('Hello', ' World') == 'Hello World'

def test_add_float():
    assert add(10.5, 24.5) == 35

# Exemple d'un test erroné
def test_add_int_error():
    assert math_func.add(7, 3) == 10