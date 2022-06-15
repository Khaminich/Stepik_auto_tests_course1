import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/execute_script.html')
chislo = browser.find_element(By.ID, value='input_value')
x = chislo.text
y = calc(x)

answer = browser.find_element(By.ID, value = 'answer')
answer.send_keys(y)

check = browser.find_element(By.ID, value = 'robotCheckbox')
check.click()
radio_robot = browser.find_element(By.ID, value = 'robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", radio_robot)
radio_robot.click()
submit = browser.find_element(By.CLASS_NAME, value = 'btn.btn-primary')
submit.click()

time.sleep(10)
browser.quit()