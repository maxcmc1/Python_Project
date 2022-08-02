import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class FrameDemo(unittest.TestCase):
    def setUp(self) -> None:
        options = Options()
        options.add_argument("start-maximized")
        self.browser = webdriver.Chrome(
            executable_path='', options=options)
        self.browser.get("https://skryabin.com/webdriver/html/sample.html")

    def tearDown(self) -> None:
        self.browser.quit()

    def test_frame_fields(self):
        browser = self.browser
        # outside of frame
        browser.switch_to.frame(browser.find_element(By.NAME, "additionalInfo"))
        # inside of frame
        browser.find_element(By.ID, "contactPersonName").send_keys("some text")
        self.assertEqual("Contact Person Phone", browser.find_element(By.XPATH, "//*[@id='contactPersonPhone']/preceding::label[1]").text)
        browser.switch_to.default_content()
        # outside of frame again
        self.assertTrue(browser.find_element(By.ID, "samplePageForm").is_displayed())
        pass


if __name__ == '__main__':
    unittest.main()
