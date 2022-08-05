from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.add_employee import PAGE_URI as add_employee_page_uri
from pages.base import BasePage


# @property
# def PAGE_URI(self):
#     return "/pim/viewEmployeeList"

PAGE_URI = "/pim/viewEmployeeList"


class EmployeeInformation(BasePage):
    def sort_table_by_first_middle_name(self):
        browser = self.browser
        browser.find_element(By.XPATH, "//th/a[text()='First (& Middle) Name']").click()
        self.wait.until(expected_conditions.url_contains("sortField=firstMiddleName"))

    def get_first_middle_name_from_row(self, row_number) -> str:
        return self.browser.find_element(By.XPATH, f"//tbody/tr[{row_number}]/td[3]").text

    def get_table_row_count(self):
        return len(self.browser.find_elements(By.XPATH, "//tbody/tr"))

    def goto_add_employee_page(self):
        self.browser.find_element(By.ID, "btnAdd").click()
        self.wait.until(expected_conditions.url_contains(add_employee_page_uri))
        # self.browser.find_element(By.ID, "lastName")


