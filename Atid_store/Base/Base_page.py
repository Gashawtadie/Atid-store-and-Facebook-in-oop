import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from Atid_store.Locators.All_LocatorPaths.locatores_paths import Locatores
from urllib3.exceptions import MaxRetryError
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as e_c
from selenium.webdriver.support.wait import WebDriverWait


class BaseFunctions(Locatores):

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def find(self, by, locate) -> WebElement:
        return self.driver.find_element(by, locate)

    def insert(self, by, locate, content):
        self.driver.find_element(by, locate).send_keys(content)

    def click(self, by, locate):
        self.wait_until_element_is_visible(locate)
        self.find(by, locate).click()

    def wait_until_element_is_visible(self, locate, time: int = 20):
        wait = WebDriverWait(self.driver, time)
        wait.until(e_c.visibility_of_element_located((By.XPATH, locate)))

    def message(self, error):
        self.wait_until_element_is_visible(error)
        return self.find(By.XPATH, error).text

    def check_product(self, error_path):
        self.wait_until_element_is_visible(error_path)
        return self.find(By.XPATH, error_path).text

    def setup(self):
        self.driver.get(self.home_path)
        self.driver.maximize_window()
        return self.driver

    def tear_down(self):
        if self.driver == True:
            self.driver.quit()
            self.driver.close()





