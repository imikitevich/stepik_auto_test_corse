# Поиск элементов с помощью Selenium
# find_element(By.ID, value) — поиск по уникальному атрибуту id элемента. Если ваши разработчики проставляют всем элементам в приложении уникальный id, то вам повезло, и вы чаще всего будет использовать этот метод, так как он наиболее стабильный;
# find_element(By.CSS_SELECTOR, value) — поиск элемента с помощью правил на основе CSS. Это универсальный метод поиска, так как большинство веб-приложений использует CSS для вёрстки и задания оформления страницам. Если find_element_by_id вам не подходит из-за отсутствия id у элементов, то скорее всего вы будете использовать именно этот метод в ваших тестах;
# find_element(By.XPATH, value) — поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;
# find_element(By.NAME, value) — поиск по атрибуту name элемента;
# find_element(By.TAG_NAME, value) — поиск элемента по названию тега элемента;
# find_element(By.CLASS_NAME, value) — поиск по значению атрибута class;
# find_element(By.LINK_TEXT, value) — поиск ссылки на странице по полному совпадению;
# find_element(By.PARTIAL_LINK_TEXT, value) — поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки.

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time



# link = "http://suninjuly.github.io/simple_form_find_task.html"

# value = 'city'
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     lst = ["Ivan", "Petrov", "Smolensk", "Russia"]
#     for i,v in enumerate(lst, 1):
#         inp = browser.find_element(By.CSS_SELECTOR, f".form-group:nth-child({i}) input")
        # inp.send_keys(v)

    # input1 = browser.find_element(By.TAG_NAME, "input")
    # input1.send_keys("Ivan")
    # input2 = browser.find_element(By.NAME, "last_name")
    # input2.send_keys("Petrov")

    # input3 = browser.find_element(By.CLASS_NAME, value)
    # input3.send_keys("Smolensk")

    # input4 = browser.find_element(By.ID, "country")
    # input4.send_keys("Russia")

#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
# finally:
#     time.sleep(3)
#     browser.quit()

# print(button)


# +++++++++=======================++++++++++++++++++++++++++++++++

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import math
# from time import sleep

# secret_link = str(math.ceil(math.pow(math.pi, math.e)*10000))
# link = "http://suninjuly.github.io/find_link_text"
# lst = ["Ivan", "Petrov", "Smolensk", "Russia"]

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)

#     lin_1 = browser.find_element(By.LINK_TEXT, secret_link)
#     lin_1.click()
    
#     sleep(1)
#     # browser.get()
#     # print(browser)

#     for i, v in enumerate(lst, 1):
#         temp = browser.find_element(By.CSS_SELECTOR, f".form-group:nth-child({i}) input")
#         temp.send_keys(v)

#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
# finally:
#     sleep(25)
#     browser.quit()

# ====================================+++++++++++++===+=++++++++++++++++


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep

# link = "http://suninjuly.github.io/huge_form.html"
# browser = webdriver.Chrome()
# browser.get(link)

# try:
#     print(browser.find_element(By.TAG_NAME, "input"))
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     print(*elements, sep="\n")
#     for el in elements:
#         print(el)
#         el.send_keys("Мой ответ")

#     browser.find_element(By.CSS_SELECTOR, "button").click()

# finally:
#     sleep(5)
#     browser.quit()

#=================================================================

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep

# link = " http://suninjuly.github.io/find_xpath_form"
# browser = webdriver.Chrome()
# browser.get(link)

# try:
#     print(browser.find_element(By.TAG_NAME, "input"))
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     print(*elements, sep="\n")
#     for el in elements:
#         print(el)
#         el.send_keys("Мой ответ")

#     browser.find_element(By.CSS_SELECTOR, "button").click()

# finally:
#     sleep(5)
#     browser.quit()

# ==============================================================

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from random import choices
# from string import ascii_lowercase


# link = "http://suninjuly.github.io/find_xpath_form"

# try:
#     bro = webdriver.Chrome()
#     bro.get(link)

#     for i in range(1,5):
#         temp = bro.find_element(By.CSS_SELECTOR, f".form-group:nth-child({i}) input")
#         temp.send_keys("".join(choices(ascii_lowercase, k=18)))

#     bro.find_element(By.XPATH, '//button[@type="submit"]').click()
# finally:
#     sleep(5)
#     bro.quit()
# ===============================================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    counter = 0

    # Ваш код, который заполняет обязательные поля
    list_label = browser.find_elements(By.TAG_NAME, "label")
    list_input = browser.find_elements(By.TAG_NAME, "input")
    for el, tx in zip(list_input, list_label):
        if "*" in tx.text:
            counter += 1
            el.send_keys("Это обязательное поле")
        
    time.sleep(1)
    
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
    assert "Congratulations! You have successfully registered!" == welcome_text and counter == 3

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()





