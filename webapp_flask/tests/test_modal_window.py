# https://stackoverflow.com/questions/46853377/how-to-switch-to-a-modal-in-python-using-selenium
# https://stackoverflow.com/questions/54939227/how-to-click-the-close-button-within-a-modal-window-through-selenium-and-python


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft  import EdgeChromiumDriverManager

import pytest
import time

url = 'https://tailspin-spacegame-web.azurewebsites.net/'

@pytest.fixture(params=["chrome"], scope='class')    # , "firefox" 
def init__driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        web_driver = webdriver.Chrome(ChromeDriverManager(log_level=0, cache_valid_range=7, print_first_line=False).install(), options=options)
        web_driver.implicitly_wait(10)
    # if request.param == "firefox":
    #     web_driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager((log_level=0, cache_valid_range=7, print_first_line=False).install())
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("init__driver")
class BaseTest:
    pass


class Test_modal_window(BaseTest):

    def test_modal_window_title(self):
        self.driver.get(url)
        # Identifier le downloader_btn et cliquer dessus
        wait = WebDriverWait(self, 20)
        wait.until(EC.element_to_be_clickable((By.ID, 'download-btn'))).click()

        # downloader_btn = self.driver.find_element_by_id()
        # downloader_btn.click()
        # time.sleep(2)
        # Identifier window modal
        modal_window = self.driver.find_element_by_xpath("//div[@id='pretend-modal']//div[2]")
        time.sleep(2)
        modal_window.click()
        assert 'This link is for example purposes and goes nowhere' in modal_window.text
        # div[id='pretend-modal'] div:nth-child(2)


# driver.get(url)
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'download-btn')))