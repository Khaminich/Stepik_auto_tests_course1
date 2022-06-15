import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')

picture_element = browser.find_element(By.ID, value = 'treasure')
x_element = picture_element.get_attribute('valuex')
x = x_element
y = calc(x)

answer = browser.find_element(By.ID, value = 'answer')
answer.send_keys(y)

check = browser.find_element(By.ID, value = 'robotCheckbox')
check.click()

radio_robot = browser.find_element(By.ID, value = 'robotsRule')
radio_robot.click()

submit = browser.find_element(By.CLASS_NAME, value = 'btn.btn-default')
submit.click()

time.sleep(10)
browser.quit()
