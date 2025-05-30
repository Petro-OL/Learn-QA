from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# (pip install -U webdriver_manager)
# comment, becose used old version Grome


class BasePage:
    PATH = r"C:\tmp\Rob\QA\Prometeus\Learn-QA"
    DRIVER_NAME = "\chromedriver.exe"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
            )
    # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # comment, becose used old version Grome

    def close(self):
        self.driver.close()
