import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Login(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path='C://Users//maksym.seliukov//PycharmProjects//Python_Automation//browsers//chromedriver.exe')
        self.browser.get("http://hrm-online.portnov.com/")

    def tearDown(self) -> None:
        self.browser.quit()

    def test_valid_login(self):
        browser = self.browser
        browser.find_element(By.ID, "txtUsername").send_keys("admin")
        browser.find_element(By.ID, "txtPassword").send_keys("password")
        browser.find_element(By.ID, "btnLogin").click()
        time.sleep(3)
        url = browser.current_url
        welcome_message = browser.find_element(By.ID, "welcome").text
        self.assertTrue(url.endswith("viewEmployeeList"))
        self.assertEqual("Welcome Admin", welcome_message)  # add assertion here


if __name__ == '__main__':
    unittest.main()
