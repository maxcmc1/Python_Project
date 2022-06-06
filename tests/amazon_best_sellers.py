import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class AmazonBestSellerExample(unittest.TestCase):
    def setUp(self) -> None:
        options = Options()
        options.add_argument("start-maximized")
        self.browser = webdriver.Chrome(
            executable_path='C://Users//maksym.seliukov//PycharmProjects//Python_Automation//browsers//chromedriver.exe', options=options)
        self.browser.get("https://www.amazon.com/")

    def tearDown(self) -> None:
        self.browser.quit()

    def test_find_headphones(self):
        browser = self.browser
        browser.find_element(By.ID, "twotabsearchtextbox").send_keys("headphones" + Keys.ENTER)
        # # OR
        # browser.find_element(By.ID, "twotabsearchtextbox").send_keys("headphones")
        # browser.find_element(By.NAME, "site-search").submit()
        # # OR
        # browser.find_element(By.ID, "twotabsearchtextbox").send_keys("headphones")
        # browser.find_element(By.CSS_SELECTOR, "input.nav-input[value='Go']").click()
        best_sellers_list = browser.find_elements(By.CSS_SELECTOR, "span.a-badge-label[data-a-badge-color='sx-orange'] span.a-badge-text[data-a-badge-color='sx-cloud']")  # By CSS
        # best_sellers_list = browser.find_elements(By.XPATH, "//span[@class="a-badge-label"][@data-a-badge-color="sx-orange"]//span[@class="a-badge-text"][@data-a-badge-color="sx-cloud"]")  # By Xpath
        best_sellers_list[0].find_element(By.XPATH, "./ancestor::div[@class='a-section']/div//a").send_keys(Keys.CONTROL + Keys.ENTER)
        pass


if __name__ == '__main__':
    unittest.main()
