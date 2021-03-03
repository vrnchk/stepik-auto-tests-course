from selenium import webdriver
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    book = browser.find_element_by_id("book")
    price = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book.click()
    x = int(browser.find_element_by_id("input_value").text)
    inp = browser.find_element_by_id("answer")
    inp.send_keys(calc(x))
    
    sub = browser.find_element_by_id("solve").click()
finally:
    time.sleep(7)
    browser.quit()