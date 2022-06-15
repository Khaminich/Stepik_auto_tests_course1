import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

first = browser.find_element(By.NAME, value='firstname')
first.send_keys('Nik')

second = browser.find_element(By.NAME, value='lastname')
second.send_keys('Ham')

email = browser.find_element(By.NAME, value='email')
email.send_keys('G')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)


submit = browser.find_element(By.CLASS_NAME, value = 'btn.btn-primary')
submit.click()

time.sleep(10)
browser.quit()