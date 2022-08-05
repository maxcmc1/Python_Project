import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.login import LoginPage
from tests import CHROME_DRIVER, TEST_DIR
import os


class BaseFixture(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path=CHROME_DRIVER)
        self.browser.get("http://hrm-online.portnov.com/")
        self.browser.maximize_window()
        self.login_page = LoginPage(self.browser)
        self.login_page.go_to_page()
        self.wait = WebDriverWait(self.browser, 3)

    def tearDown(self) -> None:
        test_name = self._testMethodName
        result_dir = os.path.join(TEST_DIR, "test_screenshots")
        if not os.path.exists(result_dir):
            os.mkdir(result_dir)
        self.browser.save_screenshot(os.path.join(result_dir, f"{test_name}.png"))
        self.browser.quit()