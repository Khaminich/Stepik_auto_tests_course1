from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    #required_elements = browser.find_elements(By.XPATH, value = "//input[@placeholder='Input your first name']" )
    #for element in required_elements:
            #element.send_keys('required')
    #and "//input[@placeholder='Input your last name']" and "//input[@placeholder='Input your email']"
    required_elements = browser.find_element(By.XPATH, value="//input[@placeholder='Input your first name']")
    required_elements.send_keys('required')
    required_elements2 = browser.find_element(By.XPATH, value="//input[@placeholder='Input your last name']")
    required_elements2.send_keys('required')
    required_elements3 = browser.find_element(By.XPATH, value="//input[@placeholder='Input your email']")
    required_elements3.send_keys('required')



    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

