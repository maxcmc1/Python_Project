import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class NewUser(unittest.TestCase):
    def setUp(self) -> None:
        options = Options()
        options.add_argument("start-maximized")
        self.browser = webdriver.Chrome(
            executable_path='C://Users//maksym.seliukov//PycharmProjects//Python_Automation//browsers//chromedriver.exe', options=options)
        self.browser.get("http://hrm-online.portnov.com/")

    def tearDown(self) -> None:
        self.browser.quit()

    def test_create_user(self):
        browser = self.browser
        wait = WebDriverWait(browser, 3)
        # Login
        self.login()
        # Click Add
        browser.find_element(By.ID, "btnAdd").click()
        # Enter employee name
        wait.until(expected_conditions.presence_of_element_located([By.ID, "firstName"])).send_keys("Emily")
        browser.find_element(By.ID, "lastName").send_keys("Jones")
        emp_id = browser.find_element(By.ID, "employeeId").get_attribute("value")
        browser.find_element(By.ID, "chkLogin").click()
        # create employee creds
        wait.until(expected_conditions.visibility_of_element_located([By.ID, "user_name"])).send_keys("ms" + emp_id)
        browser.find_element(By.ID, "user_password").send_keys("password")
        browser.find_element(By.ID, "re_password").send_keys("password")
        page_url = browser.current_url
        # Save
        browser.find_element(By.ID, "btnSave").click()
        wait.until(expected_conditions.url_changes(page_url))
        # Logout
        browser.find_element(By.ID, "welcome").click()
        wait.until(expected_conditions.visibility_of_element_located([By.LINK_TEXT, "Logout"])).click()
        # Login back
        browser.find_element(By.ID, "txtUsername").send_keys("ms" + emp_id)
        browser.find_element(By.ID, "txtPassword").send_keys("password")
        browser.find_element(By.ID, "btnLogin").click()
        actual_message = browser.find_element(By.ID, "welcome").text
        self.assertTrue("Welcome Emily", actual_message)

    def login(self, username, password):
        browser = self.browser
        browser.find_element(By.ID, "txtUsername").send_keys(username)
        browser.find_element(By.ID, "txtPassword").send_keys(password)
        browser.find_element(By.ID, "btnLogin").click()
        WebDriverWait(browser, 3).until(expected_conditions.presence_of_element_located(
            [By.CSS_SELECTOR, "#empsearch_employee_name_empName.inputFormatHint"])).click()


if __name__ == '__main__':
    unittest.main()
