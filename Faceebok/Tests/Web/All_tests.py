import time
import allure
import requests
from allure_commons.types import AttachmentType
import pytest
from Faceebok.Pages.All_pages import Tests


class TestFinal(Tests):

    def Object(self):
        final = TestFinal()
        return final

    @pytest.mark.login
    @pytest.mark.valid
    @allure.description("Login correctly with valid username and password")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self):
        self.Object().positive_login_page()

    @allure.description("Login valid username and invalid password")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_username(self):
        self.Object().invalid_user_name()

    @allure.description("Login correctly with username and invalid password")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_password(self):
        self.Object().invalid_password()

    @allure.description("Login incorrectly valid username and password")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_both_invalid(self):
        self.Object().invalid_user_pass()
        time.sleep(5)
    # forgot password
    @pytest.mark.login
    @pytest.mark.valid
    @allure.description("Test with the forgot password")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_forgot_password(self):
        self.Object().forgot_password()

    @pytest.mark.login
    @pytest.mark.valid
    @allure.description("Test with invalid email password ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_email_password(self):
        self.Object().invalid_email()
    # create account
    @pytest.mark.login
    @pytest.mark.valid
    @allure.description("Test with create account or sign up registration ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_account(self):
        self.Object().create_account()

    @pytest.mark.login
    @pytest.mark.valid
    @allure.description("Test with wrong email account")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_wrong_email_account(self):
        self.Object().create_wrong_email()

    @pytest.mark.login
    @pytest.mark.valid
    @allure.description("Test with the invalid password insert")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_password_insert(self):
        self.Object().invalid_password_insert()

    @pytest.mark.login
    @pytest.mark.valid
    @allure.description("Test with email verification")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_email_verification(self):
        self.Object().email_verification()

    @pytest.mark.login
    @pytest.mark.valid
    @allure.description("Test already logged in ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_already_loggedin(self):
        self.Object().already_logedin()


