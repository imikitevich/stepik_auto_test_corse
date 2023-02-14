# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep

# try:
#     bro = webdriver.Chrome()
#     bro.maximize_window()
#     bro.execute_script("alert('Htsdjhdgf');")
#     sleep(1)
#     # alert = bro.switch_to.alert
#     # print(alert.text)
#     # alert.accept()
#     confirm = bro.switch_to.alert
#     confirm.accept()
#     # confirm.dismiss() # для отказа

#     # prompt = bro.switch_to.alert
#     # prompt.send_keys("my text")
#     # prompt.accept() 

         
# except Exception as ex:
#     print(ex)
# finally:
#     sleep(5)
#     bro.quit()

# ==============================================================
def lesson_2_3_step4():
    # from selenium import webdriver
    # from selenium.webdriver.common.by import By
    # from time import sleep
    # from math import log, sin

    def calc(x):
        return log(abs(12*sin(x)))

    link = "http://suninjuly.github.io/alert_accept.html"

    try:
# Открыть страницу http://suninjuly.github.io/alert_accept.html
        # открываем страницу
        bro = webdriver.Chrome()
        bro.maximize_window()
        bro.get(link)
# Нажать на кнопку
        bro.find_element(By.TAG_NAME, "button").click()
# Принять confirm
        alert = bro.switch_to.alert
        alert.accept()
# На новой странице решить капчу для роботов, чтобы получить число с ответом
        x = calc(int(bro.find_element(By.ID, "input_value").text))
        bro.find_element(By.ID, "answer").send_keys(x)
        bro.find_element(By.CSS_SELECTOR, "button.btn").click()

    except Exception as ex:
        print(ex)
    finally:
        sleep(6)
        bro.quit()
        
# lesson_2_3_step4()
# ==============================================================

# Переход на новую вкладку браузера
# При работе с веб-приложениями приходится переходить по ссылкам, которые открываются в новой вкладке браузера. WebDriver может работать только с одной вкладкой браузера. При открытии новой вкладки WebDriver продолжит работать со старой вкладкой. Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти. Это делается с помощью команды switch_to.window:

# browser.switch_to.window(window_name)
# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:

# new_window = browser.window_handles[1]
# Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:

# first_window = browser.window_handles[0]
# После переключения на новую вкладку поиск и взаимодействие с элементами будут происходить уже на новой странице.

# ==============================================================
def lesson2_3_step6():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from time import sleep
    from math import log, sin

    def calc(x):
        return log(abs(12*sin(x)))

    # Открыть страницу http://suninjuly.github.io/redirect_accept.html

    link = "http://suninjuly.github.io/redirect_accept.html"

    try:
        bro = webdriver.Chrome()
        bro.get(link)
        bro.maximize_window()
    # Нажать на кнопку
        bro.find_element(By.CSS_SELECTOR, "button.btn").click()
    # Переключиться на новую вкладку
        bro.switch_to.window(bro.window_handles[1])
    # Пройти капчу для робота и получить число-ответ
        x = calc(int(bro.find_element(By.ID, "input_value").text))
        bro.find_element(By.ID, "answer").send_keys(x)
        bro.find_element(By.CSS_SELECTOR, "button.btn").click()

    except Exception as ex:
        print(ex)
    finally:
        sleep(50)
        bro.close()
        bro.quit()
        
lesson2_3_step6()
# ==============================================================
