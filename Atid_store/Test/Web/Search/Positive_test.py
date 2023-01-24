
import pytest
from selenium import webdriver
from Atid_store.Locators.All_LocatorPaths.locatores_paths import *
from Atid_store.Locators.All_LocatorPaths.locatores_paths import Locatores
from Atid_store.Base.Base_page import BaseFunctions
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


class TestPositive(Locatores):
    driver = webdriver.Chrome()
    def Setup(self):
        self.driver.get(self.home_path)
        self.driver.maximize_window()
        return self.driver

    def tear_down(self):
        if self.driver == True:
            self.driver.quit()
            self.driver.close()
    def test_positive_search_products(self):
        driver = self.Setup()
        src = driver.find_element(By.XPATH, self.search_btn_locator)
        src.click()
        enter_pro = driver.find_element(By.TAG_NAME, self.Insert_product_locator)
        enter_pro.clear()
        enter_pro.send_keys("Anchor Bracelet")
        time.sleep(2)
        search_btn = driver.find_element(By.XPATH, self.search_product_locator)
        search_btn.click()
        check_name = driver.find_element(By.XPATH, self.positive_pro_name)
        check = check_name.text
        assert check == "Anchor Bracelet"


    def test_positive_pro(self):
        driver = self.Setup()
        search = driver.find_element(By.XPATH, self.search_btn_locator)
        search.click()

        search_pro = driver.find_element(By.TAG_NAME, self.Insert_product_locator)
        search_pro.clear()
        search_pro.send_keys("ATID Blue Shoes")

        serch_button = driver.find_element(By.XPATH, self.search_product_locator)
        serch_button.click()

        check_name = driver.find_element(By.XPATH, self.check_locator)
        check = check_name.text
        assert check == "ATID Blue Shoes"



