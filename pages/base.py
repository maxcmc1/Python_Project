from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests import BASE_URL


# @property
# def PAGE_URI(self):
#     return ""

PAGE_URI = ""


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)
        self.long_wait = WebDriverWait(self.browser, 15)

    def get_title(self) -> str:
        return self.browser.find_element(By.CSS_SELECTOR, ".head h1").text

    def go_to_page(self):
        self.browser.get(BASE_URL + "/symfony/web/index.php")