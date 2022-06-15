import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')

first_element = browser.find_element(By.ID, value='num1')
x = first_element.text
second_element = browser.find_element(By.ID, value='num2')
y = second_element.text
num1 = int(x)
num2 = int(y)
sum_el = num1 + num2
select = Select(browser.find_element(By.ID, value='dropdown'))
select.select_by_visible_text('%s' % sum_el)
submit = browser.find_element(By.CLASS_NAME, value='btn.btn-default')
submit.click()

time.sleep(10)
browser.quit()

