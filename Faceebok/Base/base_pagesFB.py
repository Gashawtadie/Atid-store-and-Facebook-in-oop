from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as e_c
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from Faceebok.Locatores.locatores import LocatorsFb


class BaseFunctions(LocatorsFb):
    driver = webdriver.Chrome()

    def find(self, Path, locate) -> WebElement:
        return self.driver.find_element(Path, locate)

    def insert(self, path, locate, content):
        self.driver.find_element(path, locate).send_keys(content)

    def click(self, path, locate):
        self.find(path, locate).click()


    def wait_until_element_is_visible(self, locate, time: int = 10):
        wait = WebDriverWait(self.driver, time)
        wait.until(e_c.visibility_of_element_located((By.XPATH, locate)))

    def message(self, error):
        self.wait_until_element_is_visible(error)
        return self.find(By.XPATH, error).text

    def assert_product(self, path, error_path):
        self.wait_until_element_is_visible(error_path)
        return self.find(path, error_path).text

    def selector(self, path, locate, choose):

        date = Select(self.find(path, locate))
        date.select_by_visible_text(choose)
        self.wait_until_element_is_visible(locate)

    def setup_facebook(self):
        self.driver.get(self.HOME_PAGE_FB)
        self.driver.maximize_window()
        return self.driver

    def tear_down(self):
        self.driver.quit()


