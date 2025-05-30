from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.search_page import SearchRozetkaPage
import pytest

@pytest.mark.ui
def test_check_incorrect_username_page_object():
    sign_in_page = SignInPage()

    # Since according to the task in the SignInPage() class there is no method to open
    # page by URL, so we do it here.
    sign_in_page.driver.get("https://github.com/login")

    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    sign_in_page.close()
# ------------------------------------------------------ add
@pytest.mark.ui
def test_check_goto_forgot_password_page_object():
    sign_in_page = SignInPage()

    sign_in_page.go_to()

    sign_in_page.goto_forgot_password_page()

    assert sign_in_page.check_title("Forgot your password? · GitHub")

    sign_in_page.close()

@pytest.mark.ui
def test_check_goto_create_account_page_object():
    sign_in_page = SignInPage()

    sign_in_page.go_to()

    sign_in_page.goto_create_account_page()

    assert sign_in_page.check_title("Sign up to GitHub · GitHub")

    sign_in_page.close()

@pytest.mark.ui
def test_rozetka_bad_search_page_object():
    search_page = SearchRozetkaPage()

    search_page.go_to()

    search_page.search_for_text("")

    assert search_page.check_title("Інтернет-магазин ROZETKA™: офіційний сайт онлайн-гіпермаркету Розетка в Україні")
    
    search_page.close()

@pytest.mark.ui
def test_rozetka_good_search_page_object():
    search_page = SearchRozetkaPage()

    search_page.go_to()

    search_page.search_for_text("куртка")

    assert search_page.check_title('ROZETKA — Результати пошуку: "куртка" | Пошук')
    
    search_page.close()
