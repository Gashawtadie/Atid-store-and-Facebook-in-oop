import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Atid_store.Locators.All_LocatorPaths.locatores_paths import Locatores
from Atid_store.Base.Base_page import BaseFunctions
from selenium.webdriver.support import expected_conditions as e_c


# from Atid_store.Test.Base_test.Base import BaseTest


class SelectPro(BaseFunctions, Locatores):

    def store_menu(self):
        self.setup()
        self.click(By.XPATH, self.hm_str_pth)
        self.click(By.XPATH, self.str_pro_path)
        assert self.check_product(self.pro_name_path) == "ATID Yellow Shoes"
        self.click(By.XPATH, self.str_btn_path)
        assert self.check_product(self.price_str_path) == '120.00 ₪'
        self.click(By.XPATH, self.cpn_str_path)
        self.insert(By.XPATH, self.store_cpn_field, "123456")
        self.click(By.XPATH, self.store_apply_path)
        assert self.message(self.error_xpath) == 'Coupon "123456" does not exist!'
        self.tear_down()

    def men_menu(self):
        # self.wait_until_function_finish(self.women_menu())
        self.setup()
        self.click(By.XPATH, self.hm_men_pth)
        self.click(By.XPATH, self.men_pro_path)
        # wait.until(e_c.visibility_of_element_located(self.pro_name_men_path))
        assert self.check_product(self.pro_name_men_path) == "ATID Green Tshirt"
        self.click(By.XPATH, self.men_btn_path)
        #assert self.check_product(self.price_men_path) == "190.00 ₪"
        self.click(By.XPATH, self.cpn_men_path)
        self.insert(By.XPATH, self.men_cpn_field, '123456')
        self.click(By.XPATH, self.men_apply_path)
        assert self.message(self.error_xpath) == 'Coupon "123456" does not exist!'
        self.tear_down()

    def women_menu(self):
        # self.wait_until_function_finish(self.accessories_menu())
        self.setup()
        self.click(By.XPATH, self.hm_wmn_pth)
        self.click(By.XPATH, self.mwn_pro_path)
        assert self.check_product(self.pro_name_path_wmn) == "Blue Denim Shorts"
        self.click(By.XPATH, self.str_btn_path_wmn)
        #assert self.check_product(self.price_wmn_path) == "130.00 ₪"
        self.click(By.XPATH, self.cpn_wmn_crt_path)
        self.insert(By.XPATH, self.wmn_cpn_field, '123456')
        self.click(By.XPATH, self.wmn_apply_path)
        assert self.message(self.error_xpath) == 'Coupon "123456" does not exist!'
        self.tear_down()

    def accessories_menu(self):
        self.setup()
        self.click(By.XPATH, self.hm_acc_pth)
        self.click(By.XPATH, self.acc_pro_path)
        assert self.check_product(self.pro_name_path_acc) == "Boho Bangle Bracelet"
        self.click(By.XPATH, self.str_btn_path_acc)
        #assert self.check_product(self.price_acc_path) == "45.00 ₪"
        self.click(By.XPATH, self.cpn_acc_crt_path)
        self.insert(By.XPATH, self.wmn_cpn_field, '123456')
        self.click(By.XPATH, self.wmn_apply_path)
        assert self.message(self.error_xpath) == 'Coupon "123456" does not exist!'
        self.tear_down()

    # def wait_until_function_finish(self, meth):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(e_c.new_window_is_opened(meth))
