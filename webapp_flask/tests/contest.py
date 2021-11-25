# Ce document présente la notion de fixture
# https://docs.pytest.org/en/6.2.x/fixture.html?highlight=conftest#yield-fixtures

import pytest


class Fruit:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name

# apple = Fruit('apple')     


@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket

# 2è exemple avec utilisation de deux fixture (voir la doc offic)
# https://docs.pytest.org/en/stable/fixture.html#what-fixtures-are
# Le sénario est le suivant : j'achète un fruit, je le mets dans le panier (étape de setUp) et je teste si le fruit a bien été rajouté au panier ?

# class Fruit:
#     def __init__(self, name):
#         self.name = name

# @pytest.fixture
# def my_fruit():
#     return Fruit("apple")

# @pytest.fixture
# def fruit_basket(my_fruit):
#     return [Fruit("banana"), my_fruit]

# def test_my_fruit_in_basket(my_fruit, fruit_basket):
#     assert my_fruit in fruit_basket    