import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# або: from webdriver_manager.chrome import ChromeDriverManager
# (pip install -U webdriver_manager)
from selenium.webdriver.common.by import By
# id / name / class name / link text / cssSelector / xpath expressions / dom
import time


@pytest.mark.ui
def test_check_incorrect_username():
    # Створення об'єкту для керування бразуером
    driver = webdriver.Chrome(
        service=Service(r"C:\tmp\Rob\QA\Prometeus\Learn-QA" + "\chromedriver.exe")
        )
    # або:
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # відкриваємо сторінку https://github.com/login 
    driver.get("https://github.com/login")

    # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    # Вводимо неправильне ім'я користувача або поштову адрІесу
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")

    # Знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # Вводимо неправильний пароль
    pass_elem.send_keys("wrong password")

    # Знаходимо кнопку sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    # Емулюємо клік лівою кнопкою мишки
    btn_elem.click()
    time.sleep(2)

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"

    # Закриваємо браузер
    driver.close()
