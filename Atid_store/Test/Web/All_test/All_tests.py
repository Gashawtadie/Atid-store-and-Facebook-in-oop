import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from Atid_store.Page.Selected_pro import SelectPro

@pytest.mark.atidstore
@allure.description("test store from atid store ")
@allure.severity(allure.severity_level.CRITICAL)

class TestsAllChoice(SelectPro):
    def obj(self):
        testall = TestsAllChoice()
        return testall

    @pytest.mark.atidstore
    @pytest.mark.store
    @allure.description("test store from atid store ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_store(self):
        # self.obj().setup()
        self.obj().store_menu()

    @pytest.mark.atidstore
    @pytest.mark.men
    @allure.description("test men from atid store ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_men(self):
        # self.obj().setup()
        self.obj().men_menu()

    @pytest.mark.atidstore
    @pytest.mark.sanity
    @allure.description("test women from atid store ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_women(self):
        # self.obj().setup()
        self.obj().women_menu()

    @pytest.mark.atidstore
    @pytest.mark.sanity
    @allure.description("test accessories from atid store ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_accessories(self):
        # self.obj().setup()
        self.obj().accessories_menu()
