# pytest -n 4 -vs --disable-warnings --capture sys -rF -rP --html=test_report.html --self-contained-html test_selenium_fixt_params.py

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft  import EdgeChromiumDriverManager


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init__driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        web_driver = webdriver.Chrome(ChromeDriverManager(log_level=0, cache_valid_range=7, print_first_line=False).install(), options=options)
    if request.param == "firefox":
        web_driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager(log_level=0, cache_valid_range=7, print_first_line=False).install())
    request.cls.driver = web_driver
    yield
    web_driver.close()

@pytest.mark.usefixtures("init__driver")
class BaseTest:
    pass


class Test_Google(BaseTest):

    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"


    def test_google_url(self):
        self.driver.get("http://www.google.com")
        assert self.driver.current_url == "https://www.google.com/?gws_rd=ssl"