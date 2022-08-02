from selenium.webdriver.common.by import By

from pages.base import BasePage


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.PAGE_URI = "/auth/login"

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

