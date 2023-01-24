import time

import pytest
from selenium import webdriver
from urllib3.exceptions import NewConnectionError, MaxRetryError

from Atid_store.Locators.All_LocatorPaths.locatores_paths import *
from Atid_store.Locators.All_LocatorPaths.locatores_paths import Locatores
from Atid_store.Test.Base_test.Base import BaseTest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep


class TestNegative(BaseTest, Locatores):
    driver = webdriver.Chrome()
    def Setup(self):
        self.driver.get(self.home_path)
        self.driver.maximize_window()
        return self.driver

    def tear_down(self):
        if self.driver == True:
            self.driver.quit()
            self.driver.close()

    def test_Negative(self):

        driver = self.Setup()
        # sleep()
        # Test that the search button is functional when the search field is filled with an invalid search query.
        clc_btn = driver.find_element(By.XPATH, self.search_btn_locator)

        clc_btn.click()

        search_pro_no = driver.find_element(By.TAG_NAME,  self.Insert_product_locator)
        search_pro_no.clear()
        search_pro_no.send_keys("abcdef")

        click_pro = driver.find_element(By.XPATH,  self.search_product_locator)
        click_pro.click()

        check_result = driver.find_element(By.XPATH,  self.check_results)

        result = check_result.text
        assert result == "Search Results for: abcdef"
        sleep(2)
        super().tear_down()

    def test_mix_upperandlower(self):
        driver = self.Setup()
        # sleep()
        # Test that the search button is functional when the search field has a mix of upper and lower case characters
        clc_btn = driver.find_element(By.XPATH,  self.search_btn_locator)

        clc_btn.click()

        search_pro_no = driver.find_element(By.TAG_NAME,  self.Insert_product_locator)
        search_pro_no.clear()
        search_pro_no.send_keys("ANCHOR BRaceleT")
        sleep(2)

        click_pro = driver.find_element(By.XPATH,  self.search_product_locator)
        click_pro.click()

        check_result = driver.find_element(By.TAG_NAME,  self.error_check)

        result = check_result.text
        assert result == "Sorry, but nothing matched your search terms. Please try again with some different keywords."
        super().tear_down()

    def test_withCharacters(self):
        driver = self.Setup()
        # sleep()
        # Test that the search button is functional when the search field has special characters.
        clc_btn = driver.find_element(By.XPATH,  self.search_btn_locator)

        clc_btn.click()

        search_pro_no = driver.find_element(By.TAG_NAME,  self.Insert_product_locator)
        search_pro_no.clear()
        search_pro_no.send_keys("@anchor bracelet!")
        sleep(2)

        click_pro = driver.find_element(By.XPATH,  self.search_product_locator)

        click_pro.click()

        check_result = driver.find_element(By.ID, "primary")
        check_li = check_result.find_elements(By.XPATH,  self.error_compare)

        for n in check_li:
            if n == "Sorry, but nothing matched your search terms. Please try again with some different keywords.":
                break

    def test_spaces(self):
        driver = self.Setup()
        # Test that the search button is functional when the search field has a mix of alphabetic and numeric characters.
        clc_btn = driver.find_element(By.XPATH,  self.search_btn_locator)
        clc_btn.click()
        search_pro_no = driver.find_element(By.TAG_NAME,  self.Insert_product_locator)
        search_pro_no.clear()
        search_pro_no.send_keys("ATID1 Green2 Tshirt3")
        sleep(2)
        click_pro = driver.find_element(By.XPATH,  self.search_product_locator)
        click_pro.click()
        check_result = driver.find_element(By.ID, "primary")
        check_li = check_result.find_elements(By.XPATH, self.error_compare)

        for n in check_li:
            if n == "Sorry, but nothing matched your search terms. Please try again with some different keywords.":
                break

    def test_multiplewords(self):
        driver = self.Setup()
        # sleep()
        # Test that the search button is functional when the search field has multiple words or phrases.
        clc_btn = driver.find_element(By.XPATH,  self.search_btn_locator)
        clc_btn.click()
        search_pro_no = driver.find_element(By.TAG_NAME,  self.Insert_product_locator)
        search_pro_no.clear()
        search_pro_no.send_keys("ATID Greengreeen Tshirt")
        sleep(2)
        click_pro = driver.find_element(By.XPATH,  self.search_product_locator)
        click_pro.click()
        check_result = driver.find_element(By.ID, "primary")
        check_li = check_result.find_elements(By.XPATH, self.error_compare)

        for n in check_li:
            if n == "Sorry, but nothing matched your search terms. Please try again with some different keywords.":
                break
        self.tear_down()





