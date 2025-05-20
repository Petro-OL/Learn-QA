#
# імпорт створеного свого класу з файлу
from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.sign_in_page import SearchRozetkaPage
import pytest
import time

@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # створення об'єкту сторінки
    sign_in_page = SignInPage()

    # # відкриваємо сторінку https://github.com/login 
    # sign_in_page.go_to()

    # Оскільки згідно завдання в класі SignInPage() немає методу, щоб відкрити 
    # сторінку за URL, тому робимо це тут !!!
    sign_in_page.driver.get("https://github.com/login")

    # виконуємо спробу увійти в систему GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Закриваємо браузер
    sign_in_page.close()

# ------------------------------------------------------ add

@pytest.mark.ui
def test_check_goto_forgot_password_page_object():
    # створення об'єкту сторінки
    sign_in_page = SignInPage()

    # відкриваємо сторінку https://github.com/login 
    sign_in_page.go_to()

    # Знаходимо посилання і переходимо на відповідну сторінку
    sign_in_page.goto_forgot_password_page()

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Forgot your password? · GitHub")

    # Закриваємо браузер
    sign_in_page.close()

# @pytest.mark.ui
# def test_check_goto_create_account_page_object():
#     # створення об'єкту сторінки
#     sign_in_page = SignInPage()

#     # відкриваємо сторінку https://github.com/login 
#     sign_in_page.go_to()

#     # Знаходимо посилання і переходимо на відповідну сторінку
#     sign_in_page.goto_create_account_page()

#     # Перевіряємо, що назва сторінки така, яку ми очікуємо
#     assert sign_in_page.check_title("Sign up to GitHub · GitHub")

#     # Закриваємо браузер
#     sign_in_page.close()

# Інтернет-магазин ROZETKA™: офіційний сайт онлайн-гіпермаркету Розетка в Україні
@pytest.mark.ui
def test_rozetka_bad_search_page_object():
     # створення об'єкту сторінки
    search_page = SearchRozetkaPage()

    # відкриваємо сторінку https://github.com/login 
    search_page.go_to()

    # Знаходимо поле і шукаємо "порожній текст"
    search_page.search_for_text("")
    time.sleep(3)

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert search_page.check_title("Інтернет-магазин ROZETKA™: офіційний сайт онлайн-гіпермаркету Розетка в Україні")
    
    # Закриваємо браузер
    search_page.close()

@pytest.mark.ui
def test_rozetka_good_search_page_object():
     # створення об'єкту сторінки
    search_page = SearchRozetkaPage()

    # відкриваємо сторінку https://github.com/login 
    search_page.go_to()

    # Знаходимо поле і шукаємо "порожній текст"
    search_page.search_for_text("куртка")
    time.sleep(20)

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert search_page.check_title('ROZETKA — Результати пошуку: "куртка" | Пошук')
    
    # Закриваємо браузер
    search_page.close()
