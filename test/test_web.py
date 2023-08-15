import time

import pytest
from selenium import webdriver

from src.web.SaucePages import LoginHelper, LoginLocators, CatalogLocators


@pytest.fixture(scope="session", autouse=True)
def browser():
    """
    Фикстура для работы с драйвером
    """
    driver = webdriver.Chrome()
    yield driver
    driver.close()


class TestWeb:
    def test_login(self, browser):
        login_page = LoginHelper(browser)
        login_page.go_to()
        login_page.auth_standard()

        assert login_page.check_element(CatalogLocators.LOCATOR_CONTAINER)

        login_page.logout()

        assert login_page.check_element(LoginLocators.LOCATOR_CONTAINER)

    def test_locked(self, browser):
        login_page = LoginHelper(browser)
        login_page.go_to()
        login_page.auth_locked()

        assert login_page.check_element(LoginLocators.LOCATOR_CONTAINER)
        assert login_page.check_element(LoginLocators.LOCATOR_ERROR)

    def test_product(self):
        pass

    def test_basket(self):
        pass

    def test_sort(self):
        pass
