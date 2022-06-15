import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    button = browser.find_element(By.CLASS_NAME, value='btn.btn-primary')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    chislo = browser.find_element(By.ID, value='input_value')
    x = chislo.text
    y = calc(x)

    answer = browser.find_element(By.ID, value='answer')
    answer.send_keys(y)

    submit = browser.find_element(By.CLASS_NAME, value='btn.btn-primary')
    submit.click()
finally:
    time.sleep(10)
    browser.quit()

