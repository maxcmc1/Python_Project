import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from fixtures.base import BaseFixture


class Search(BaseFixture):
    def test_search_by_job_title(self):
        browser = self.browser
        browser.find_element(By.ID, "txtUsername").send_keys("admin")
        browser.find_element(By.ID, "txtPassword").send_keys("password")
        browser.find_element(By.ID, "btnLogin").click()
        wait = WebDriverWait(browser, 3)
        wait.until(expected_conditions.presence_of_element_located([By.CSS_SELECTOR, "#empsearch_employee_name_empName.inputFormatHint"])).click() # explicit wait
        Select(browser.find_element(By.ID, "empsearch_job_title")).select_by_visible_text("QA Manager") # select webdriver object
        # OR below
        #browser.find_element(By.XPATH, "//option[text()='QA Manager']").click()
        browser.find_element(By.ID, "searchBtn").click()
        wait.until(expected_conditions.element_located_to_be_selected([By.XPATH, "//option[text()='QA Manager']"]))
        # OR below
        # qa_manager_option = browser.find_element(By.XPATH, "//option[text()='QA Manager']")
        # wait.until(expected_conditions.element_to_be_selected(qa_manager_option))
        list_of_rows = browser.find_elements(By.XPATH, "//tbody/tr//td[5]")
        for single_row in list_of_rows:
            actual_job_title = single_row.text
            self.assertEqual("QA Manager", actual_job_title)

        # OR (another method of looping)
        # for j in range(1, len(list_of_rows) + 1): # '+1' because the actual loop starts from 0 however, there is no
        #     actual_job_title = browser.find_element(By.XPATH, f"//tbody/tr[{j}]/td[5]").text
        #     self.assertEqual("QA Manager", actual_job_title)


if __name__ == '__main__':
    unittest.main()
