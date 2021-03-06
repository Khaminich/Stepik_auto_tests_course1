import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    magic = browser.find_element(By.CLASS_NAME, value='trollface.btn.btn-primary')
    magic.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    number = browser.find_element(By.ID, value='input_value')
    x = number.text
    y = calc(x)
    answer = browser.find_element(By.ID, value='answer')
    answer.send_keys(y)
    submit = browser.find_element(By.CLASS_NAME, value='btn.btn-primary')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()