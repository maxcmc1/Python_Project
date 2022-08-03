import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.add_employee import enter_employee_name
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
        self.login_page.go_to_page()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_create_user(self):
        browser = self.browser
        # Login
        self.login_page.login()
        # Click Add
        EmployeeInformation(browser).goto_add_employee_page()
        # Enter employee name
        # self.func_name("james", height=129, size='small', married='True', pet='dog')
        emp_id = enter_employee_name(self.browser, "Emily", "Jones", "K")
        # OR
        # emp_id = self.enter_employee_name(last="Jones", middle="K", first="Emily")
        browser.find_element(By.ID, "chkLogin").click()
        # create employee creds
        self.wait.until(expected_conditions.visibility_of_element_located([By.ID, "user_name"])).send_keys("ms" + emp_id)
        browser.find_element(By.ID, "user_password").send_keys("password")
        browser.find_element(By.ID, "re_password").send_keys("password")
        page_url = browser.current_url
        # Save
        browser.find_element(By.ID, "btnSave").click()
        self.wait.until(expected_conditions.url_changes(page_url))
        # Logout
        browser.find_element(By.ID, "welcome").click()
        self.wait.until(expected_conditions.visibility_of_element_located([By.LINK_TEXT, "Logout"])).click()
        # Login back
        # browser.find_element(By.ID, "txtUsername").send_keys("ms" + emp_id)
        # browser.find_element(By.ID, "txtPassword").send_keys("password")
        # browser.find_element(By.ID, "btnLogin").click()
        self.login_page.login(f'ms{emp_id}')   # we supply only username because password is the same as initial in login function
        actual_message = browser.find_element(By.ID, "welcome").text
        self.assertTrue("Welcome Emily", actual_message)

    # def func_name(self, name, dob=None, **kwargs):
    #     example_dict = {
    #         'Key': 'value',
    #         'age': 12,
    #         'speed': 36.5
    #     }
    #     # this is what would happen to the passed in params
    #     # kwargs = {'height':129, 'size': 'small', 'married': True, pet: 'dog'}
    #
    #     for item in kwargs.keys():
    #         print(kwargs.get(item))
    #
    #     if 'height' in kwargs.keys():
    #         print(f"your height is {kwargs.get('height')}")


if __name__ == '__main__':
    unittest.main()
