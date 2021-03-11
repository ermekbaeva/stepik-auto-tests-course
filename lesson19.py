from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'),'100'))
    button = browser.find_element_by_id('book').click()

    value = browser.find_element_by_id('input_value')
    x = value.text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(y))

    button = browser.find_element_by_id('solve').click()

finally:
    time.sleep(10)
    browser.quit()
