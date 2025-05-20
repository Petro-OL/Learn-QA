#
# імпорт створеного свого батьківського класу з файлу
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
# id / name / class name / link text / cssSelector / xpath expressions / dom
import time


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None: 
        # виклик базового класу для ініціаліззії драйвера браузера
        super().__init__()       

    # згідно завдання в класі SignInPage() немає методу, щоб відкрити сторінку за URL   
    def go_to(self):
    # але мені він потрібен для подальших тестів
        # відкрити сторінку
        self.driver.get(SignInPage.URL) 

    def try_login(self, username, password):
        # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Вводимо неправильне ім'я користувача або поштову адрІесу
        login_elem.send_keys(username)

        # Знаходимо поле, в яке будемо вводити неправильний пароль
        pass_elem = self.driver.find_element(By.ID, "password")

        # Вводимо неправильний пароль
        pass_elem.send_keys(password)

        # Знаходимо кнопку sign in
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Емулюємо клік лівою кнопкою мишки
        btn_elem.click()

    # додано для власного тесту ----------------------
    def goto_forgot_password_page(self):
        url_elem = self.driver.find_element(By.ID, "forgot-password")
        url_elem.click()

    # def goto_create_account_page(self):
    #     url_elem = self.driver.find_element(By.TAG_NAME, "A")
    #     url_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title


class SearchRozetkaPage(BasePage):
    URL = 'https://rozetka.com.ua/'

    def __init__(self) -> None: 
        # виклик базового класу для ініціаліззії драйвера браузера
        super().__init__()       

    def go_to(self):
        # відкрити сторінку
        self.driver.get(SearchRozetkaPage.URL) 

    def search_for_text(self, text_for_search):
        # Знаходимо поле, в яке будемо вводити текст
        search_elem = self.driver.find_element(By.NAME, "search")
        
        # Тиснем прямо в полі
        search_elem.click()
        time.sleep(5)

        # Вводимо текст для пошуку
        search_elem.send_keys(text_for_search)
        #search_elem.click()
        
        # Знаходимо кнопку Знайти
        btn_elem = self.driver.find_element(By.CLASS_NAME, "button_color_green")
        # Емулюємо клік лівою кнопкою мишки
        btn_elem.click()

    def check_title(self, expected_title):
        # print(self.driver.title)
        return self.driver.title == expected_title



