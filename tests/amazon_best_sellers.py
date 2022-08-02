import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests import CHROME_DRIVER


class AmazonBestSellerExample(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path=CHROME_DRIVER)
        self.browser.get("https://www.amazon.com/")
        self.browser.maximize_window()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_find_headphones(self):
        search_keyword = "tablet"
        browser = self.browser
        wait = WebDriverWait(browser, 5)
        browser.find_element(By.ID, "twotabsearchtextbox").send_keys(search_keyword + Keys.ENTER)
        # # OR
        # browser.find_element(By.ID, "twotabsearchtextbox").send_keys("headphones")
        # browser.find_element(By.NAME, "site-search").submit()
        # # OR
        # browser.find_element(By.ID, "twotabsearchtextbox").send_keys("headphones")
        # browser.find_element(By.CSS_SELECTOR, "input.nav-input[value='Go']").click()
        best_sellers_list = browser.find_elements(By.CSS_SELECTOR, "span.a-badge-label[data-a-badge-color='sx-orange'] span.a-badge-text[data-a-badge-color='sx-cloud']")  # By CSS
        # best_sellers_list = browser.find_elements(By.XPATH, "//span[@class='a-badge-label'][@data-a-badge-color='sx-orange']//span[@class='a-badge-text'][@data-a-badge-color='sx-cloud']/ancestor::div[contains(@class,'s-list-col-left')]//a[contains(@class,'s-no-outline')]")  # By Xpath
        # best_sellers_list[0].find_element(By.XPATH, "./ancestor::div[@class='a-section']/div//a").send_keys(Keys.CONTROL + Keys.ENTER)
        for best_sellers_banner in best_sellers_list:
            best_sellers_banner.find_element(By.XPATH, "./ancestor::div[contains(@class,'s-list-col-left')]//a[contains(@class,'s-no-outline')]").send_keys(
                Keys.CONTROL + Keys.ENTER)
        wait.until(expected_conditions.number_of_windows_to_be(len(best_sellers_list) + 1)) # +1 is stands for orignal (current) window
        handles = browser.window_handles
        for j in range(1, len(handles)):
            browser.switch_to.window(handles[j])
            wait.until(expected_conditions.presence_of_element_located([By.ID, "add-to-cart-button"])).click()
            a_list = browser.find_elements(By.ID, "a-popover-3") # creating list in order if statement doesn't fail if it will not find an element in HTML
            if a_list and a_list[0].is_displayed():
                browser.find_element(By.CSS_SELECTOR, "#a-popover-3 .a-button-close").click()
        pass


if __name__ == '__main__':
    unittest.main()
