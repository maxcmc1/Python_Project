import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.add_employee import AddEmployeePage
from pages.employee_information import EmployeeInformation
from pages.login import LoginPage
from tests import CHROME_DRIVER


class NewUser(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path=CHROME_DRIVER)
        self.browser.get("http://hrm-online.portnov.com/")
        self.browser.maximize_window()
        self.login_page = LoginPage(self.browser)
        self.wait = WebDriverWait(self.browser, 3)
        self.employee_info_page = EmployeeInformation(self.browser)
        self.add_employee_page = AddEmployeePage(self.browser)
        #self.login_page.go_to_page()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_create_user(self):
        self.login_page.login()
        self.employee_info_page.goto_add_employee_page()
        emp_id = self.add_employee_page.enter_employee_name(last="Jones", middle="K", first="Emily")
        self.add_employee_page.enter_employee_credentials(f'ms{emp_id}', "password")
        self.login_page.logout()
        self.login_page.login(f'ms{emp_id}')
        actual_message = self.login_page.get_welcome_message()
        self.assertTrue("Welcome Emily", actual_message)


if __name__ == '__main__':
    unittest.main()
