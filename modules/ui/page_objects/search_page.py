from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchRozetkaPage(BasePage):
    URL = 'https://rozetka.com.ua/'

    def __init__(self) -> None: 
        super().__init__()       

    def go_to(self):
        self.driver.get(SearchRozetkaPage.URL) 

    def search_for_text(self, text_for_search):
        search_elem = self.driver.find_element(By.NAME, "search")
        
        search_elem.click()

        search_elem.send_keys(text_for_search)
        
        btn_elem = self.driver.find_element(By.CLASS_NAME, "button_color_green")
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title



