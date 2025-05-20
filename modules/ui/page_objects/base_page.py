from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# або: from webdriver_manager.chrome import ChromeDriverManager
# (pip install -U webdriver_manager)

class BasePage:
    # PATH = r"/home/sbutenko/repos/LnD/Become QA Auto/"
    PATH = r"C:\tmp\Rob\QA\Prometeus\Learn-QA"
    DRIVER_NAME = "\chromedriver.exe"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
            )
    # або:
    # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def close(self):
        self.driver.close()
