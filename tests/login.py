import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from parameterized import parameterized


class Login(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path='C://Users//maksym.seliukov//PycharmProjects//Python_Automation//browsers//chromedriver.exe')
        self.browser.get("http://hrm-online.portnov.com/")

    def tearDown(self) -> None:
        self.browser.quit()

    @parameterized.expand([
        ("valid_credentials", "admin", "password", "viewEmployeeList", "Welcome Admin", True),
        ("bad_password", "admin", "PASSWORD", "validateCredentials", "Invalid credentials", False),
        ("empty_password", "", "password", "/auth/login", "Username cannot be empty", False),
        ("white_space_username_password", " ", " ", "validateCredentials", "Invalid credentials", False)
    ])
    def test_login(self, test_name, username, password, url_ending, expected_message, positive):
        browser = self.browser
        browser.find_element(By.ID, "txtUsername").send_keys(username)
        browser.find_element(By.ID, "txtPassword").send_keys(password)
        browser.find_element(By.ID, "btnLogin").click()
        time.sleep(3)
        url = browser.current_url
        if positive:
            actual_message = browser.find_element(By.ID, "welcome").text
        else:
            actual_message = browser.find_element(By.ID, "spanMessage").text
        # self.assertTrue(url.endswith(url_ending), "The page url '{0}' did not end with the expected value of '{1}'".format(url, url_ending))
        self.assertTrue(url.endswith(url_ending), f"The page url '{url}' did not end with the expected value of '{url_ending}'")
        self.assertEqual(expected_message, actual_message)

    # def test_valid_login(self):
    #     browser = self.browser
    #     browser.find_element(By.ID, "txtUsername").send_keys("admin")
    #     browser.find_element(By.ID, "txtPassword").send_keys("password")
    #     browser.find_element(By.ID, "btnLogin").click()
    #     time.sleep(3)
    #     url = browser.current_url
    #     welcome_message = browser.find_element(By.ID, "welcome").text
    #     self.assertTrue(url.endswith("viewEmployeeList"))
    #     self.assertEqual("Welcome Admin", welcome_message)
    #
    # def test_invalid_password(self):
    #     browser = self.browser
    #     browser.find_element(By.ID, "txtUsername").send_keys("admin")
    #     browser.find_element(By.ID, "txtPassword").send_keys("PASSWORD")
    #     browser.find_element(By.ID, "btnLogin").click()
    #     time.sleep(1)
    #     url = browser.current_url
    #     welcome_message = browser.find_element(By.ID, "spanMessage").text
    #     self.assertTrue(url.endswith("validateCredentials"))
    #     self.assertEqual("Invalid credentials", welcome_message)


if __name__ == '__main__':
    unittest.main()
