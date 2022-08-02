from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage


class EmployeeInformation(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.PAGE_URI = "/pim/viewEmployeeList"

    def sort_table_by_first_middle_name(self):
        browser = self.browser
        browser.find_element(By.XPATH, "//th/a[text()='First (& Middle) Name']").click()
        wait = WebDriverWait(self.browser, 5)
        wait.until(expected_conditions.url_contains("sortField=firstMiddleName"))

    def get_first_middle_name_from_row(self, row_number) -> str:
        return self.browser.find_element(By.XPATH, f"//tbody/tr[{row_number}]/td[3]").text

    def get_table_row_count(self):
        return len(self.browser.find_elements(By.XPATH, "//tbody/tr"))

