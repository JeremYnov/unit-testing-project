## Voici le scénario suivant :

# Relancer un test sur Chrome, FireFox et Edge pour être sûr que le site soit compatible avec ces browsers ?
# L'idée est de créer autant de fixture que de browser ; le fixt a un scope class.

# pytest -vs --disable-warnings --capture sys -rF -rP --html=../test_report.html --self-contained-html test_selenium_fixture_classes_demo.py

# Exécuter les tests en mode parallèle ? 
# pytest -n 2 -vs --disable-warnings --capture sys -rF -rP --html=test_report.html --self-contained-html test_selenium_fixture_classes_demo.py

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft  import EdgeChromiumDriverManager
import pytest

@pytest.fixture(scope='class')
def setUp_Chrome(request):
    print("=> *** I am a fixture qui lance Chrome ; mon périmitère est class !")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=ChromeDriverManager(log_level=0, cache_valid_range=7, print_first_line=False).install(), options=options)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    
    yield
    print('\n dernière étape) tear down ...')
    driver.close()
    driver.quit()


@pytest.fixture(scope='class')
def setUp_Edge(request):
    print("=> *** I am a fixture qui lance Edge ; mon périmitère est class !")
    driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager(log_level=0, cache_valid_range=7, print_first_line=False).install())
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield
    print('\n dernière étape) tear down ...')
    driver.close()
    driver.quit()


@pytest.mark.usefixtures("setUp_Chrome")
class Base_Chrome_Test:
    pass

class Test_Google_Chrome(Base_Chrome_Test):
    def test_google_title_chrome(self):
        print("2) test to verify title title of the website on chrome ...")
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"



@pytest.mark.usefixtures("setUp_Edge")
class Base_Edge_Test:
    pass

class Test_Google_Edge(Base_Edge_Test):
    def test_google_title_edge(self):
        print("3) test to verify title of the website on Edge...")
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"