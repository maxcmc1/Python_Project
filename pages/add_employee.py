from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage


@property
def PAGE_URI(self):
    return "/pim/addEmployee"


class AddEmployeePage(BasePage):
    def enter_employee_first(self, first):
        self.wait.until(
            expected_conditions.presence_of_element_located([By.ID, "firstName"])).send_keys(first)

    def enter_employee_last(self, last):
        self.wait.until(
            expected_conditions.presence_of_element_located([By.ID, "lastName"])).send_keys(last)

    def enter_employee_middle(self, middle):
        self.wait.until(
            expected_conditions.presence_of_element_located([By.ID, "middleName"])).send_keys(middle)

    def get_employee_id(self):
        return self.browser.find_element(By.ID, "employeeId").get_attribute("value")

    def enter_employee_name(self, first, last, middle=None):
        self.enter_employee_first(first)
        self.enter_employee_first(last)
        if middle:
            self.enter_employee_first(middle)
        return self.get_employee_id()

    def enter_employee_credentials(self, username, password, repeat_password=None):
        self.browser.find_element(By.ID, "chkLogin").click()
        # create employee creds
        self.wait.until(expected_conditions.visibility_of_element_located([By.ID, "user_name"])).send_keys(username)
        self.browser.find_element(By.ID, "user_password").send_keys(password)
        repassword = repeat_password if repeat_password else password
        self.browser.find_element(By.ID, "re_password").send_keys(repassword)
        page_url = self.browser.current_url
        # Save
        self.browser.find_element(By.ID, "btnSave").click()
        self.wait.until(expected_conditions.url_changes(page_url))