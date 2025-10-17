from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import easyocr
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options  
)

driver.set_window_size(1000, 600)
driver.implicitly_wait(time_to_wait=2)  

#변경가능
url = 'https://ticket.melon.com/performance/index.htm?prodId=211981'
driver.get(url)

driver.find_element(By.LINK_TEXT,'로그인').click()
driver.find_element(By.CSS_SELECTOR, 'button[title="카카오계정 로그인"]').click()
time.sleep(5)