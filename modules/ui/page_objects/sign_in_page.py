# import the created parent class from a file
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None: 
        # call the base class to initialize the browser driver
        super().__init__()       

    # according to the task in the SignInPage() class there is no method to open the page by URL
    def go_to(self):
    # but I need it for further tests
        # open page
        self.driver.get(SignInPage.URL) 

    def try_login(self, username, password):
        # We find the field in which we will enter the incorrect username or email address
        login_elem = self.driver.find_element(By.ID, "login_field")

        login_elem.send_keys(username)

        # We find the field in which we will enter the incorrect password
        pass_elem = self.driver.find_element(By.ID, "password")

        pass_elem.send_keys(password)

        # Find the sign in button
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Emulate a left mouse click
        btn_elem.click()

    def goto_forgot_password_page(self):
        url_elem = self.driver.find_element(By.ID, "forgot-password")
        url_elem.click()

    def goto_create_account_page(self):
        url_elem = self.driver.find_element(By.TAG_NAME, "A")
        url_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title

