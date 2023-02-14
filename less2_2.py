# Открыть страницу https://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from time import sleep

# link = "https://suninjuly.github.io/selects2.html"

# try:
#     bro = webdriver.Chrome()
#     bro.get(link)
#     select = Select(bro.find_element(By.TAG_NAME, "select"))

#     n1 = int(bro.find_element(By.ID, "num1").text)
#     n2 = int(bro.find_element(By.ID, "num2").text)
#     sel = bro.find_element(By.CSS_SELECTOR, "#num1 + span").text

#     if sel == "+" or sel.lower() == "и":
#         res = n1 + n2
#     elif sel == "-":
#         res = n1 - n2
#     elif sel == "*":
#         res = n1 * n2
#     elif sel == "/":
#         res = n1 / n2
    
#     # bro.find_element(By.TAG_NAME, "select").click()
#     # bro.find_element(By.CSS_SELECTOR, f"[value='{res}']").click()
#     # bro.find_element(By.TAG_NAME, "select").click()
#     select.select_by_value(f"{res}")
    
#     bro.find_element(By.CSS_SELECTOR, "button.btn").click()

# finally:
#     sleep(4)
#     bro.quit()

# Можно использовать еще два метода:
# select.select_by_visible_text("text") 
# и select.select_by_index(index).
# Первый способ ищет элемент по видимому тексту, например,
# select.select_by_visible_text("Python") найдёт "Python" для нашего примера.


#=========================================================================

# from selenium import webdriver
# from time import sleep
# browser = webdriver.Chrome()
# # browser.execute_script("alert('Robots at work');")
# # browser.execute_script("document.title='Script executing';")
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
# sleep(4)
# browser.quit()

#=========================================================================

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# button.click()

#==========================================================================

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep

# link = "https://SunInJuly.github.io/execute_script.html"

# browser = webdriver.Chrome()
# browser.get(link)

# # button = browser.find_element_by_tag_name("button")
# button = browser.find_element(By.TAG_NAME, "button")
# sleep(1)
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
# # button.click()

# sleep(5)
# browser.quit()
#=========================================================================

# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from time import sleep
# from math import log, sin

# def calc(x):
#     return log(abs(12*sin(x)))

# link = "http://SunInJuly.github.io/execute_script.html"

# try:
#     bro = webdriver.Chrome()
#     bro.get(link)
#     x = calc(int(bro.find_element(By.ID, "input_value").text))
#     bro.find_element(By.ID, "answer").send_keys(x)
#     bro.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
#     butt = bro.find_element(By.CSS_SELECTOR, "button.btn")
#     footer = bro.find_element(By.TAG_NAME, "footer")
    
#     # bro.execute_script("window.scrollBy(0, 100);") # промотать на сто пикселей
#     bro.execute_script('arguments[0].style.visibility = \'hidden\'', footer) # скрыть объект
#     # bro.execute_script("return arguments[0].scrollIntoView(true);", butt) # переместить объект вверх видимой части страници
#     # Еще в глобальном смысле мотнуть в самый верх или самый низ страницы можно и питоном для тега body
#     # from selenium.webdriver.common.keys import Keys
#     # browser.find_element_by_tag_name('body').send_keys(Keys.END) #или Home если наверх

#     bro.find_element(By.ID, "robotsRule").click()
#     butt.click()

# finally:
#     sleep(5)
#     bro.quit()

#========================================================================================

# import os
# # получаем путь к дирректории исполняемого файла:
# current_dir = os.path.abspath(os.path.dirname(__file__))
# print(current_dir)
# #добавляем к пути имя файла:
# file_path = os.path.join(current_dir, "file.txt")
# print(file_path)
# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))
# print(os.path.abspath(os.path.dirname(__file__)))
# # отправляем файл на страницу:
# # element.send_keys(file_path)

# Подробнее о методах модуля os можете почитать самостоятельно в документации: https://docs.python.org/3/library/os.path.html.

#========================================================================================
# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from os.path import abspath, dirname, join



link = "http://suninjuly.github.io/file_input.html"

file = join(abspath(dirname(__file__)), "file.txt")

try:
    bro = webdriver.Chrome()
    bro.maximize_window()
    bro.get(link)
    inp_list = bro.find_elements(By.TAG_NAME, "input")
    lst_value = ['Name', 'Last Name', 'email@g.com', file]
    for inp, val in zip(inp_list, lst_value):
        inp.send_keys(val)
    
    bro.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    sleep(5)
    bro.quit()




#========================================================================================



