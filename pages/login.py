from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pages.base import BasePage


@property
def PAGE_URI(self):
    return "/auth/login"


class LoginPage(BasePage):
    def login(self, username='admin', password='password'):
        browser = self.browser
        browser.find_element(By.ID, "txtUsername").send_keys(username)
        browser.find_element(By.ID, "txtPassword").send_keys(password)
        browser.find_element(By.ID, "btnLogin").click()
        # WebDriverWait(browser, 3).until(expected_conditions.presence_of_element_located(
        #     [By.CSS_SELECTOR, "#empsearch_employee_name_empName.inputFormatHint"])).click()

    def click_social_media_icon(self, icon_name):
        social_icon = f"//a[contains(@href, '{icon_name}')]"
        self.browser.find_element(By.XPATH, social_icon)

    def click_page_footer_link(self):
        footer = "#footer a"
        self.browser.find_element(By.CSS_SELECTOR, footer).click()

    def get_title(self) -> str:
        return self.browser.find_element(By.ID, "logInPanelHeading").text

    def logout(self):
        self.browser.find_element(By.ID, "welcome").click()
        self.wait.until(expected_conditions.visibility_of_element_located([By.LINK_TEXT, "Logout"])).click()

    def get_welcome_message(self):
        return self.wait.until(expected_conditions.presence_of_element_located([By.ID, "welcome"])).text

