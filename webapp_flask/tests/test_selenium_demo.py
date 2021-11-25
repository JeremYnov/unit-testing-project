import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import webbrowser
import time
import random

###################################################################################
# Quelques options pour accélerer le webdriver
###################################################################################

# Si vs rencontrez ce bug lors du lancement du driver chrome, ajoutez les options suivantes : 
# crbug.com/1216328: Checking Bluetooth availability started. Please report if there is no report that this ends.
# https://stackoverflow.com/questions/69441767/error-using-selenium-chrome-webdriver-with-python
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

###################################################################################
# Selenium seul (sans pytest)
###################################################################################

# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
# driver. get('https://www.python.org')
# assert "Python" in driver.title
# search_bar = driver.find_element_by_id("id-search-field")
# search_bar.clear()
# search_bar.send_keys("pycon")
# time.sleep(round(random.uniform(3, 5), 1))
# search_bar.send_keys(Keys.ENTER)
# time.sleep(round(random.uniform(3, 5), 1))
# assert "No results found." not in driver.page_source
# driver.close()
# driver.quit()

###################################################################################
# Selenium avec pytest
###################################################################################

# def test_search_bar_accepts_post_request():
#     driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
#     driver. get('https://www.python.org')
#     assert "Python" in driver.title
#     search_bar = driver.find_element_by_id("id-search-field")
#     search_bar.clear()
#     search_bar.send_keys("pycon")
#     time.sleep(round(random.uniform(3, 5), 1))
#     search_bar.send_keys(Keys.ENTER)
#     time.sleep(round(random.uniform(3, 5), 1))
#     assert "No results found." not in driver.page_source
#     driver.close()
#     driver.quit()

###################################################################################
# Selenium avec pytest + fixtures
###################################################################################

# pytest -vs --disable-warnings --capture sys -rF -rP --html=../test_report.html --self-contained-html test_selenium_demo.py

# Bonne pratique pour créer un bon rapport de test : 
# --self-contained-html => css, html, image, ... tout en un pour le partage du rapport aux collègues
# --capture sys -rF -rP => capturer les sorties du pytest ds le rapport HTML ; -rF (pr les tests failed) ; -rP (pr les tests passed)
# https://stackoverflow.com/questions/58769701/how-to-capture-the-log-details-on-pytest-html-as-well-as-writing-in-to-console


driver = None
@pytest.fixture()
def setUp():
    print("=> *** I am a fixture")    
    print('\n1) initiating chrome driver ...')
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(executable_path=ChromeDriverManager(log_level=0, cache_valid_range=7, print_first_line=False).install(), options=options)
    driver.implicitly_wait(10)
    driver.get('https://www.python.org')
    driver.minimize_window()
    
    yield
    print('\n dernière étape) tear down ...')
    # driver.close()
    driver.quit()


def test_title_fixt(setUp):
    print("2) test to verify title...")
    assert "Python" in driver.title

def test_search_bar_fixt(setUp):
    print("3) test to verify content on the page...")
    search_bar = driver.find_element_by_id("id-search-field")
    search_bar.clear()
    search_bar.send_keys("pycon")
    time.sleep(round(random.uniform(3, 5), 1))
    search_bar.send_keys(Keys.ENTER)
    time.sleep(round(random.uniform(3, 5), 1))
    assert "No results found." not in driver.page_source

def test_fail_fixt(setUp):
    print("4) test fail...")
    assert "Java" in driver.title
