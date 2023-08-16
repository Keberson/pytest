import pytest
from selenium import webdriver

from src.web.Locators import *
from src.web.SaucePages import LoginHelper, ProductHelper


@pytest.fixture(scope="session", autouse=True)
def browser():
    """
    Фикстура для работы с драйвером
    """
    driver = webdriver.Chrome()
    yield driver
    driver.close()


@pytest.fixture()
def logged_product(browser):
    """
    Фикстура с залогининым пользователем
    :param browser: фикстура драйвера
    """
    product_page = ProductHelper(browser)
    yield product_page


class TestWeb:
    def test_login(self, browser):
        login_page = LoginHelper(browser)
        login_page.auth_standard()

        assert login_page.check_element(CatalogLocators.LOCATOR_BURGER_BTN)

        login_page.logout()

        assert login_page.check_element(LoginLocators.LOCATOR_CONTAINER)

    def test_locked(self, browser):
        login_page = LoginHelper(browser)
        login_page.auth_locked()

        assert login_page.check_element(LoginLocators.LOCATOR_CONTAINER)
        assert login_page.check_element(LoginLocators.LOCATOR_ERROR)

    @pytest.mark.parametrize(
        'add_button_class_name',
        [
            'add-to-cart-sauce-labs-backpack',
            'add-to-cart-sauce-labs-bike-light',
            'add-to-cart-sauce-labs-fleece-jacket',
            'add-to-cart-sauce-labs-bolt-t-shirt',
            'add-to-cart-sauce-labs-onesie',
            'add-to-cart-test.allthethings()-t-shirt-(red)'
        ]
    )
    def test_purchase(self, add_button_class_name, logged_product):
        logged_product.go_to_url("https://www.saucedemo.com/inventory.html")
        logged_product.click_on_the((By.ID, add_button_class_name))

        assert logged_product.get_cart_counter() == 1

        logged_product.click_on_the(CatalogLocators.LOCATOR_CART)

        assert logged_product.check_element(CartLocators.LOCATOR_LIST)
        assert logged_product.check_element(CartLocators.LOCATOR_CHECKOUT)

        logged_product.click_on_the(CartLocators.LOCATOR_CHECKOUT)

        assert logged_product.check_element(PurchaseLocators.LOCATOR_CONTAINER)
        assert logged_product.check_element(PurchaseLocators.LOCATOR_CONTINUE)

        logged_product.fill_information()

        assert logged_product.check_element(PurchaseLocators.LOCATOR_FINISH)

        logged_product.click_on_the(PurchaseLocators.LOCATOR_FINISH)

        assert logged_product.check_element(CompleteLocators.LOCATOR_COMPLETE)
        assert logged_product.check_element(CompleteLocators.LOCATOR_BACK)

        logged_product.click_on_the(CompleteLocators.LOCATOR_BACK)

        assert logged_product.check_element(CatalogLocators.LOCATOR_CONTAINER)

    def test_basket(self):
        pass

    def test_sort(self):
        pass
