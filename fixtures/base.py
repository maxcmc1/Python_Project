import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.login import LoginPage
from tests import CHROME_DRIVER


class BaseFixture(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path=CHROME_DRIVER)
        self.browser.get("http://hrm-online.portnov.com/")
        self.browser.maximize_window()
        self.login_page = LoginPage(self.browser)
        self.login_page.go_to_page()
        self.wait = WebDriverWait(self.browser, 3)

    def tearDown(self) -> None:
        self.browser.quit()