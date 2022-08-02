import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.employee_information import EmployeeInformation
from pages.login import LoginPage
from tests import CHROME_DRIVER


class TableSort(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path=CHROME_DRIVER)
        self.browser.get("http://hrm-online.portnov.com/")
        self.browser.maximize_window()
        self.login_page = LoginPage(self.browser)
        self.login_page.go_to_page()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_sort_by_first_middle_name(self):
        self.login_page.login()
        emp_info_page = EmployeeInformation(self.browser)
        emp_info_page.sort_table_by_first_middle_name()
        row_count = emp_info_page.get_table_row_count()
        previous_name = ""
        for row_number in range(row_count):
            name = emp_info_page.get_first_middle_name_from_row(row_number + 1).lower()
            self.assertLessEqual(previous_name, name)
            # print(previous_name, " is less or equal to ", name)
            previous_name = name

        pass


if __name__ == '__main__':
    unittest.main()
