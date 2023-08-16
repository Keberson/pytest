from selenium.common import TimeoutException
from src.web.BaseApp import BasePage
from src.web.Locators import *


class LoginHelper(BasePage):
    LOGIN_STANDARD = "standard_user"
    LOGIN_LOCKED = "locked_out_user"
    PASSWORD = "secret_sauce"

    def auth_standard(self) -> None:
        """
        Метод для аутентификация под стандартным пользователем
        """
        self.enter_text(LoginLocators.LOCATOR_USERNAME, self.LOGIN_STANDARD)
        self.enter_text(LoginLocators.LOCATOR_PASSWORD, self.PASSWORD)
        self.click_on_the(LoginLocators.LOCATOR_SUBMIT)

    def auth_locked(self) -> None:
        """
        Метод для аутентификации под заблокированным пользователем
        """
        self.enter_text(LoginLocators.LOCATOR_USERNAME, self.LOGIN_LOCKED)
        self.enter_text(LoginLocators.LOCATOR_PASSWORD, self.PASSWORD)
        self.click_on_the(LoginLocators.LOCATOR_SUBMIT)

    def logout(self) -> None:
        """
        Метод для выхода из системы
        """
        self.find_element(CatalogLocators.LOCATOR_BURGER_BTN).click()
        self.find_element(CatalogLocators.LOCATOR_LOGOUT).click()


class ProductHelper(LoginHelper):
    FIRST_NAME = 'Maksim'
    LAST_NAME = 'Kuzov'
    ZIP = '127015'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auth_standard()

    def product_add_to_cart(self, locator):
        """
        Метод для добавление в корзину товара по локатору его кнопки
        :param locator: локатор элемента
        """
        self.find_element(locator).click()

    def get_cart_counter(self) -> int:
        """
        Метод для получения счетчика у корзины
        :return: количество товаров в корзине
        """
        try:
            element = self.find_element(CatalogLocators.LOCATOR_CART_BADGE, time=2)
            badge = int(element.text)
        except TimeoutException:
            badge = 0

        return badge

    def fill_information(self):
        """
        Метод для заполнения полей с информации при оформлении заказа
        """
        self.enter_text(PurchaseLocators.LOCATOR_FIRST_NAME, self.FIRST_NAME)
        self.enter_text(PurchaseLocators.LOCATOR_LAST_NAME, self.LAST_NAME)
        self.enter_text(PurchaseLocators.LOCATOR_ZIP, self.ZIP)
        self.click_on_the(PurchaseLocators.LOCATOR_CONTINUE)

