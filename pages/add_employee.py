from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage


class AddEmployeePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.PAGE_URI = "/pim/addEmployee"
        self.wait = WebDriverWait(self.browser, 5)

    def enter_employee_first(self, first):
        WebDriverWait(self.browser, 3).until(
            expected_conditions.presence_of_element_located([By.ID, "firstName"])).send_keys(first)

    def enter_employee_last(self, last):
        WebDriverWait(self.browser, 3).until(
            expected_conditions.presence_of_element_located([By.ID, "lastName"])).send_keys(last)

    def enter_employee_middle(self, middle):
        WebDriverWait(self.browser, 3).until(
            expected_conditions.presence_of_element_located([By.ID, "middleName"])).send_keys(middle)

    def get_employee_id(self):
        return self.browser.find_element(By.ID, "employeeId").get_attribute("value")

    def enter_employee_name(self, first, last, middle=None):
        self.enter_employee_first(first)
        self.enter_employee_first(last)
        if middle:
            self.enter_employee_first(middle)
        return self.get_employee_id()