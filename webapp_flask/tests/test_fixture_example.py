
import pytest

## Voici le scénario suivant (amazon website) :

# 1) Open the shop homepage, 2) Log in with “testuser” and “testpassword”, 3) go to the “/laptop” page, 4) Add an item, 5) Wait for page to load with reccomended accessories, 6) Add an accessory, 7) Click on the “Buy now”, 8) Free delivery is offered (because customer order two or more item), 9) Remove one item, 11) Free delivery now is not offered (because customer order just one item), 11) Cancel the payment and 12) finally logout

## Ns ns intéressons plus particulièrement à tester : 4) Add an item, 5) Wait for page to load with reccomended accessories, 6) Add an accessory, 7) Click on the “Buy now”, 8) Free delivery is offered (because customer order two or more item), 9) Cancel the payment, 10) remove the items

# Les pré-étapes 1), 2) et 3) doivent être définies dans une fixture ! 
# Log out est une post étape et doit être définie dans la même fixture !

# pytest -s test_fixture_example.py
# -s (Show Output) permet d'afficher les msg des print ; parcq le comportement par défaut de pytest est de ne pas les afficher


@pytest.fixture(scope="session")
def setUp():
    print('=> *** I am a fixture : ')
    print("1) setUp : Open the shop homepage ... => Successful ! ")   # AKA Lanch browser ; create App 
    print("2) setUp : Login  ... => Successful ! ")                    # AKA go to the “/login” page
    print("3) setUp : go to the “/laptop” page ... => Successful !\n\n") # AKA browse product page
    yield
    print("9) tearDown : Logoff")
    print("10) test end et cleanUp")


def test_add_laptop(setUp):
    print("Test : Add laptop Successful")
    assert 'laptop' == 'laptop'

def test_reccomended_accessories_page(setUp):
    print("Test : Load reccomended accessories to the specific laptop Successful\n\n")
    assert 'accessoire' == 'accessoire'


def test_add_accessory(setUp):
    print("Test : Add accessory Successful\n\n")
    assert 'accessoire add' == 'accessoire add'

def test_buy_now(setUp):
    print("Test : Item cart page load Successful and Free delivery is offered Successful\n\n")
    assert 'Free delivery' == 'Free delivery'

def test_remove_item(setUp):
    print("Test : Remove Item Successful and Free delivery is not offered Successful\n\n")
    assert 'item removed' == 'item removed'
    
def test_cancel_payment(setUp):
    print("Test : Cancel payment  Successful")
    assert 'payment canceled' == 'payment canceled'
