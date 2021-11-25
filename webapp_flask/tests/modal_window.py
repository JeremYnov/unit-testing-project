# https://stackoverflow.com/questions/46853377/how-to-switch-to-a-modal-in-python-using-selenium
# https://stackoverflow.com/questions/54939227/how-to-click-the-close-button-within-a-modal-window-through-selenium-and-python


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

url = 'https://tailspin-spacegame-web.azurewebsites.net/'


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager(log_level=0, cache_valid_range=7, print_first_line=False).install(), options=options)
# web_driver.implicitly_wait(10)
driver.get(url)
try:
    download_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'download-btn')))
    time.sleep(2)
    download_btn.click()
except:
    pass 
try:
    modal_window = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='pretend-modal']//div[2]")))
    time.sleep(2)
    # Si la modal est bien présente, je peux alors vérifier le texte dedans !
except:
    pass
try:
    modal_close = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='pretend-modal']//button[@type='button'][normalize-space()='×']"))) 
    modal_close.click()
except:
    pass

assert 'This link is for example purposes and goes nowhere' in modal_window.text

# driver.close()
# driver.quit()