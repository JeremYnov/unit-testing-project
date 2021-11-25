# pip install pytest-cov

# pytest --cov=test_cov --cov-report html
#  --cov-branch

import module_cov

def test_add():
    assert module_cov.add(2, 3) == 5

def test_area():
    assert module_cov.area(2, 3) == 6
    assert module_cov.area(-2, 3) == None

def test_fib():
    assert module_cov.fib(1) == 1        