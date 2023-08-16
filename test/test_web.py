import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from src.web.Locators import *
from src.web.SaucePages import LoginHelper, ProductHelper
from src.web.Info import Product


@pytest.fixture(scope="session", autouse=True)
def browser():
    """
    Фикстура для работы с драйвером
    """
    driver = webdriver.Chrome()
    yield driver
    driver.close()


@pytest.fixture(scope="class")
def logged_product(browser):
    """
    Фикстура с залогининым пользователем
    :param browser: фикстура драйвера
    """
    product_page = ProductHelper(browser)
    yield product_page


@pytest.fixture(scope="function")
def clear_logged(logged_product):
    """
    Фикстура для работы с чистыми страницами (пустая корзина)
    :param logged_product: фикстура залогининого пользователя
    """
    logged_product.driver.execute_script('window.localStorage.clear();')
    logged_product.go_to_url("https://www.saucedemo.com/inventory.html")
    yield logged_product


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
        'product_name, locator_add',
        Product.get_name_add()
    )
    def test_purchase(self, clear_logged, product_name, locator_add):
        clear_logged.click_on_the(locator_add)
        clear_logged.click_on_the(CatalogLocators.LOCATOR_CART)

        assert clear_logged.check_element(CartLocators.LOCATOR_LIST)
        assert clear_logged.find_element(CartLocators.LOCATOR_ITEM_NAME).text == product_name
        assert clear_logged.check_element(CartLocators.LOCATOR_CHECKOUT)

        clear_logged.click_on_the(CartLocators.LOCATOR_CHECKOUT)

        assert clear_logged.check_element(PurchaseLocators.LOCATOR_CONTAINER)
        assert clear_logged.check_element(PurchaseLocators.LOCATOR_CONTINUE)

        clear_logged.fill_information()

        assert clear_logged.check_element(PurchaseLocators.LOCATOR_FINISH)

        clear_logged.click_on_the(PurchaseLocators.LOCATOR_FINISH)

        assert clear_logged.check_element(CompleteLocators.LOCATOR_COMPLETE)
        assert clear_logged.check_element(CompleteLocators.LOCATOR_BACK)

        clear_logged.click_on_the(CompleteLocators.LOCATOR_BACK)

        assert clear_logged.check_element(CatalogLocators.LOCATOR_CONTAINER)

    @pytest.mark.parametrize(
        'payload',
        [
            Product.get_add_remove(),
            [],
            Product.get_add_remove()[:3]
        ]
    )
    def test_basket(self, clear_logged, payload):

        expect = len(payload)

        for row in payload:
            locator_add = row[0]
            clear_logged.click_on_the(locator_add)

        assert clear_logged.get_cart_counter() == expect

        for row in payload:
            locator_remove = row[1]
            clear_logged.click_on_the(locator_remove)

        assert clear_logged.get_cart_counter() == 0

    @pytest.mark.parametrize(
        'sort_type, reverse',
        [
            ('Name (A to Z)', False),
            ('Name (Z to A)', True),
            ('Price (low to high)', False),
            ('Price (high to low)', True),
        ]
    )
    def test_sort(self, clear_logged, sort_type, reverse):
        select = Select(clear_logged.find_element(CatalogLocators.LOCATOR_SELECT))
        select.select_by_visible_text(sort_type)

        assert clear_logged.find_element(CatalogLocators.LOCATOR_ACTIVE_SELECT).text == sort_type

        all_items = clear_logged.find_elements(CatalogLocators.LOCATOR_ITEM)
        sorted_items = []
        prototype = []

        if 'Name' in sort_type:
            sorted_items = [item.text.split('\n')[0] for item in all_items]
            prototype = sorted(Product.PRODUCTS_NAME, reverse=reverse)
        elif 'Price' in sort_type:
            sorted_items = [float(item.text.split('\n')[2].removeprefix('$')) for item in all_items]
            prototype = sorted(Product.PRODUCTS_PRICE, reverse=reverse)

        assert sorted_items == prototype
