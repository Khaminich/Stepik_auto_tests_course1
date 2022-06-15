import math
def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
  link = 'http://suninjuly.github.io/math.html'
  browser = webdriver.Chrome()
  browser.get(link)

  x_element = browser.find_element(By.ID, value = 'input_value')
  x = x_element.text
  y = calc(x)
  answer_element = browser.find_element(By.ID, value = 'answer')
  answer_element.send_keys(y)

  check_element = browser.find_element(By.ID, value = 'robotCheckbox')
  check_element.click()

  radio_element = browser.find_element(By.ID, value = 'robotsRule')
  radio_element.click()

  submit_element = browser.find_element(By.CLASS_NAME, value = 'btn.btn-default')
  submit_element.click()
finally:
  time.sleep(10)
  browser.quit()



