import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        options = Options()
        options.add_argument("start-maximized")
        self.browser = webdriver.Chrome(
            executable_path='C://Users//maksym.seliukov//PycharmProjects//Python_Automation//browsers//chromedriver.exe', options=options)
        self.browser.get("http://hrm-online.portnov.com/")

    def tearDown(self) -> None:
        self.browser.quit()

    def test_something(self):
        browser = self.browser
        browser.find_element(By.ID, "txtUsername").send_keys("admin")
        browser.find_element(By.ID, "txtPassword").send_keys("password")
        browser.find_element(By.ID, "btnLogin").click()
        WebDriverWait(browser, 3).until(expected_conditions.presence_of_element_located([By.ID, "empsearch_job_title"])).click()
        # browser.find_element(By.ID, "empsearch_job_title").click()
        browser.find_element(By.XPATH, "//option[text()='QA Manager']").click()
        browser.find_element(By.ID, "searchBtn").click()
        time.sleep(3)
        list_of_rows = browser.find_elements(By.XPATH, "//tbody/tr//td[5]")
        for single_row in list_of_rows:
            actual_job_title = single_row.text
            self.assertEqual("QA Manager", actual_job_title)
        # OR (another method of looping)
        for j in range(1, len(list_of_rows) + 1):
            actual_job_title = browser.find_element(By.XPATH, f"//tbody/tr[{j}]/td[5]").text
            self.assertEqual("QA Manager", actual_job_title)


if __name__ == '__main__':
    unittest.main()
