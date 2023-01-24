from selenium.webdriver.common.by import By
from Faceebok.Base.base_pagesFB import BaseFunctions
from Faceebok.Locatores.locatores import LocatorsFb
import allure
from allure_commons.types import AttachmentType
# from Faceebok.Test.Base.base import BaseTestFacebook

@allure.severity(allure.severity_level.NORMAL)
class Tests(BaseFunctions, LocatorsFb):
    @allure.severity(allure.severity_level.NORMAL)
    def positive_login_page(self):
        self.setup_facebook()
        self.insert(By.XPATH, self.USERNAME_FIELD, "0526162719")
        self.insert(By.XPATH, self.PASSWORD_FIELD, "Gasaki86")
        self.click(By.XPATH, self.BTN_LOCATOR)
        assert self.assert_product(By.XPATH, self.ASSERTERROR) == "Welcome to Facebook, Gashu"
        self.tear_down()

    @allure.severity(allure.severity_level.NORMAL)
    def invalid_user_name(self):
        self.setup_facebook()
        self.insert(By.XPATH, self.USERNAME_FIELD, "0123456789")
        self.insert(By.XPATH, self.PASSWORD_FIELD, "Gasaki86")
        self.click(By.XPATH, self.BTN_LOCATOR)
        assert self.assert_product(By.XPATH, self.NEXT_PAGE) == "Continue as Gashu?"
        self.click(By.CSS_SELECTOR, self.INVALID_USERNAME_NOTYOU_CSSSELECTOR)
        assert self.assert_product(By.CSS_SELECTOR,
                                   self.ERROR_MESSAGE_LOCATOR_INVALIDUSERNAME) == "We couldn't find an account that matches what you entered, but we've found one that closely matches."

        self.tear_down()

    def invalid_password(self):
        self.setup_facebook()
        self.insert(By.XPATH, self.USERNAME_FIELD, "0526162719")
        self.insert(By.XPATH, self.PASSWORD_FIELD, "123456abc")
        self.click(By.XPATH, self.BTN_LOCATOR)
        assert self.assert_product(By.CSS_SELECTOR, self.ERROR_MESSAGE_INVALIPASSWORD) == "The password that you've entered is incorrect.Forgotten password? "
        self.tear_down()

    def invalid_user_pass(self):
        self.setup_facebook()
        self.insert(By.XPATH, self.USERNAME_FIELD, "incorrect")
        self.insert(By.XPATH, self.PASSWORD_FIELD, "incorrect")
        self.click(By.XPATH, self.BTN_LOCATOR)
        assert self.assert_product(By.TAG_NAME, self.TEST_INVALID_USER_PASS_ERROR_LOCATOR) == "Facebook helps you connect and share with the people in your life."
        self.tear_down()
    # forgot password
    def forgot_password(self):
        self.setup_facebook()
        self.insert(By.XPATH, self.USERNAME_FIELD, "0526162719")
        self.insert(By.XPATH, self.PASSWORD_FIELD, "123456789")
        self.click(By.XPATH, self.BTN_LOCATOR)
        self.click(By.XPATH, self.FORGOT_PASSWORD_LINK)
        self.click(By.XPATH, self.NOT_YOU_LOCATOR)
        self.insert(By.XPATH, self.ACCOUNT_KEY_LOCATOR, "gashumec@gmail.com")
        self.click(By.NAME, self.SUBMIT_LOCATOR)
        self.click(By.XPATH, self.CLICK_BTN_LOCATR)
        self.click(By.TAG_NAME, self.CON_LOC)
        self.insert(By.XPATH, self.ENTER_LOC, "129102 ")
        self.click(By.XPATH, self.CONFIRM_LOC)
        self.tear_down()

    def invalid_email(self):
        self.setup_facebook()
        self.insert(By.XPATH, self.USERNAME_FIELD, "0526162719")
        self.insert(By.XPATH, self.PASSWORD_FIELD, "123456789")
        self.click(By.XPATH, self.BTN_LOCATOR)
        self.click(By.LINK_TEXT, self.forgot_password)
        self.click(By.XPATH, self.NOT_YOU_LOCATOR)
        self.insert(By.XPATH, self.ACCOUNT_KEY_LOCATOR, "abcd@gmail.com")
        self.click(By.NAME, self.SUBMIT_LOCATOR)
        self.click(By.XPATH, self.INCORRECT_EMAIL_LOC)
        self.insert(By.XPATH, self.FILL_MAIL_LOC, "abcd@gmail.com")
        self.tear_down()

    # ******************************************* Register ********************************
    def create_account(self):
        self.setup_facebook()
        self.click(By.XPATH, self.SIGN_UP_LOCATOR)
        self.insert(By.NAME, self.NAME_FIELD_LOCATOR, "gashu")
        self.insert(By.NAME, self.SURE_NAME_LOCATOR, "tade")
        self.insert(By.NAME, self.EMAIL_PHONE_LOCATOR, "kirubel12922@gmail.com")
        self.insert(By.NAME, self.CONFRIRMATION_EMAIL_LOCATOR, "kirubel12922@gmail.com")
        self.insert(By.XPATH, self.INSERT_PASSWORD_LOCATOR, "Gasaki86")
        self.selector(By.XPATH, self.SELECT_DATE_LOCAT, "7")
        self.selector(By.XPATH, self.MONTH_SELECTOR, "Sep")
        self.selector(By.XPATH, self.YEAR_SELECTOR, "1992")
        self.click(By.XPATH, self.GENDER_SELECTOR)
        self.click(By.TAG_NAME, self.SIGN_UP_BUTTON)



    def create_wrong_email(self):
        self.setup_facebook()
        self.click(By.XPATH, self.SIGN_UP_LOCATOR)
        self.insert(By.NAME, self.NAME_FIELD_LOCATOR, "gashu")
        self.insert(By.NAME, self.SURE_NAME_LOCATOR, "tade")
        self.insert(By.NAME, self.EMAIL_PHONE_LOCATOR, "Abcd123@gmail.com")
        self.insert(By.NAME, self.CONFRIRMATION_EMAIL_LOCATOR, "Abcd123@gmail.com")
        self.insert(By.XPATH, self.INSERT_PASSWORD_LOCATOR, "Gasaki86")
        self.selector(By.XPATH, self.SELECT_DATE_LOCAT, "7")
        self.selector(By.XPATH, self.MONTH_SELECTOR, "Sep")
        self.selector(By.XPATH, self.YEAR_SELECTOR, "1992")
        self.click(By.XPATH, self.GENDER_SELECTOR)
        self.click(By.TAG_NAME, self.BUTTON_SELECTOR)
        assert self.assert_product(By.TAG_NAME,
                                   self.WRONG_EMAIL_SELECT) == "Sorry, we are not able to process your registration."

    def invalid_password_insert(self):
        self.setup_facebook()
        self.click(By.XPATH, self.SIGN_UP_LOCATOR)
        self.insert(By.NAME, self.NAME_FIELD_LOCATOR, "Gman")
        self.insert(By.NAME, self.SURE_NAME_LOCATOR, "Gasa")
        self.insert(By.NAME, self.EMAIL_PHONE_LOCATOR, "Abcd123@gmail.com")
        self.insert(By.NAME, self.CONFRIRMATION_EMAIL_LOCATOR, "Abcd123@gmail.com")
        self.insert(By.XPATH, self.INSERT_PASSWORD_LOCATOR, "ab")
        self.selector(By.XPATH, self.SELECT_DATE_LOCAT, "7")
        self.selector(By.XPATH, self.MONTH_SELECTOR, "Sep")
        self.selector(By.XPATH, self.YEAR_SELECTOR, "1992")
        self.click(By.XPATH, self.GENDER_SELECTOR)
        self.click(By.TAG_NAME, self.BUTTON_SELECTOR)
        assert self.assert_product(By.TAG_NAME,
                                   self.ERROR_MESSAGE_PASSWORD) == "Sorry, we are not able to process your registration."

    def email_verification(self):
        self.setup_facebook()
        self.click(By.XPATH, self.SIGN_UP_LOCATOR)
        self.insert(By.NAME, self.NAME_FIELD_LOCATOR, "Gman")
        self.insert(By.NAME, self.SURE_NAME_LOCATOR, "Gasa")
        self.insert(By.NAME, self.EMAIL_PHONE_LOCATOR, "Abcd123@gmail.com")
        self.insert(By.NAME, self.CONFRIRMATION_EMAIL_LOCATOR, "Abcd123@gmail.com")
        self.insert(By.XPATH, self.INSERT_PASSWORD_LOCATOR, "ab")
        self.selector(By.XPATH, self.SELECT_DATE_LOCAT, "7")
        self.selector(By.XPATH, self.MONTH_SELECTOR, "Sep")
        self.selector(By.XPATH, self.YEAR_SELECTOR, "1992")
        self.click(By.XPATH, self.GENDER_SELECTOR)
        self.click(By.TAG_NAME, self.BUTTON_SELECTOR)
        self.insert(By.TAG_NAME, self.ERROR_MESSAGE_CODE, "12922")
        self.click(By.XPATH, self.SEND_EMAIL_SELECTOR)


    def already_logedin(self):
        self.setup_facebook()
        self.click(By.XPATH, self.SIGN_UP_LOCATOR)
        self.insert(By.NAME, self.NAME_FIELD_LOCATOR, "Gman")
        self.insert(By.NAME, self.SURE_NAME_LOCATOR, "Gasa")
        self.insert(By.NAME, self.EMAIL_PHONE_LOCATOR, "Abcd123@gmail.com")
        self.insert(By.NAME, self.CONFRIRMATION_EMAIL_LOCATOR, "Abcd123@gmail.com")
        self.insert(By.XPATH, self.INSERT_PASSWORD_LOCATOR, "ab")
        self.selector(By.XPATH, self.SELECT_DATE_LOCAT, "7")
        self.selector(By.XPATH, self.MONTH_SELECTOR, "Sep")
        self.selector(By.XPATH, self.YEAR_SELECTOR, "1992")
        self.click(By.XPATH, self.GENDER_SELECTOR)
        self.click(By.TAG_NAME, self.BUTTON_SELECTOR)
        self.insert(By.TAG_NAME, self.ERROR_MESSAGE_CODE, "12922")
        self.click(By.XPATH, self.SEND_EMAIL_SELECTOR)
        assert self.assert_product(By.XPATH, self.EMAIL_ALREADY_USE) == "That number was used too recently"
