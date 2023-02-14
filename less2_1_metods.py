# Ваша программа должна выполнить следующие шаги:

# Открыть страницу https://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from math import log as ln, sin

# link = "https://suninjuly.github.io/math.html"

# try:
#     bro = webdriver.Chrome()
#     bro.get(link)

#     x = str(bro.find_element(By.ID, "input_value").text)
#     func = bro.find_element(By.CSS_SELECTOR, "label .nowrap").text.strip().split()[2].strip(",").replace("x", x)
#     y = eval(func)

#     bro.find_element(By.ID, 'answer').send_keys(y)
#     bro.find_element(By.CSS_SELECTOR, "[for=robotCheckbox]").click()
#     bro.find_element(By.CSS_SELECTOR, "[for=robotsRule]").click()
#     bro.find_element(By.CSS_SELECTOR, 'button.btn').click()

# finally:
#     sleep(5)
#     bro.quit()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Ваша программа должна:

# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(log(abs(12*sin(int(x)))))
try:
    bro = webdriver.Chrome()
    bro.get(link)

    x = bro.find_element(By.TAG_NAME, "img").get_attribute("valuex")
    y = calc(x)

    bro.find_element(By.ID, "answer").send_keys(y)
    bro.find_element(By.ID, "robotCheckbox").click()
    bro.find_element(By.ID, "robotsRule").click()
    # bro.find_element(By.TAG_NAME, "button").click()
finally:
    sleep(50)
    bro.quit()


