from time import sleep
from math import log, sin


def step3():
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    # Открыть страницу http://suninjuly.github.io/wait1.html
    link = "http://suninjuly.github.io/wait1.html"

    bro = webdriver.Chrome()
    bro.maximize_window()
    bro.implicitly_wait(5)

    try:
        bro.get(link)
    # Нажать на кнопку "Verify"
        
        bro.find_element(By.CSS_SELECTOR, "button.btn").click()
        assert "successful" in bro.find_element(By.ID, "verify_message").text, "Всё плохо!"

    except Exception as ex:
        print(ex)
    finally:
        
        sleep(5)
        bro.close()
        bro.quit()
    # Проверить, что появилась надпись "Verification was successful!"
# step3()

def step_6():
    #Какую ошибку вы увидите в консоли, если попытаетесь выполнить команду browser.find_element(By.ID, "button") \
    # после открытия страницы http://suninjuly.github.io/cats.html?
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    bro = webdriver.Chrome()
    link = "http://suninjuly.github.io/cats.html?"
    bro.get(link)
    bro.find_element(By.ID, "button")
    sleep(2)
    bro.quit()

# step_6()

def step_7():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait2.html")

    

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    button.click()

    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

    sleep(3)
    browser.quit()

# step_7()

def calc(x):
    return log(abs(12*sin(x)))

def step_8():
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium import webdriver

    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    bro = webdriver.Chrome()
    bro.implicitly_wait(5)
    bro.get("http://suninjuly.github.io/explicit_wait2.html")

# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(bro, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
# Нажать на кнопку "Book"
    # button = WebDriverWait(bro, 5).until(
    #     EC.element_to_be_clickable((By.ID, "book"))
    # )
    # button.click()
    bro.find_element(By.ID, "book").click()

    x = calc(int(bro.find_element(By.ID, "input_value").text))
    bro.find_element(By.ID, "answer").send_keys(x)

    bro.find_element(By.ID, "solve").click()

    sleep(10)

    bro.quit()

# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
step_8()
    

