from selenium.webdriver.common.by import By


class LoginLocators:
    """
     Класс для хранения локаторов страницы Авторизации
     """
    LOCATOR_CONTAINER = (By.CLASS_NAME, "login_container")
    LOCATOR_USERNAME = (By.ID, "user-name")
    LOCATOR_PASSWORD = (By.ID, "password")
    LOCATOR_SUBMIT = (By.ID, "login-button")
    LOCATOR_ERROR = (By.CLASS_NAME, "error")


class CatalogLocators:
    """
    Класс для хранения локаторов страницы Каталога
    """
    LOCATOR_CONTAINER = (By.CLASS_NAME, "page_wrapper")
    LOCATOR_BURGER_BTN = (By.ID, "react-burger-menu-btn")
    LOCATOR_LOGOUT = (By.LINK_TEXT, "Logout")
    LOCATOR_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    LOCATOR_CART = (By.CLASS_NAME, "shopping_cart_link")


class CartLocators:
    """
    Класс для хранения локаторов страницы Корзина
    """
    LOCATOR_LIST = (By.CLASS_NAME, "cart_list")
    LOCATOR_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    LOCATOR_CHECKOUT = (By.ID, "checkout")


class PurchaseLocators:
    """
    Класс для хранения локаторов для страниц Оформление
    """
    LOCATOR_CONTAINER = (By.ID, "checkout_info_container")
    LOCATOR_CONTINUE = (By.ID, "continue")
    LOCATOR_FINISH = (By.ID, "finish")
    LOCATOR_FIRST_NAME = (By.ID, "first-name")
    LOCATOR_LAST_NAME = (By.ID, "last-name")
    LOCATOR_ZIP = (By.ID, "postal-code")


class CompleteLocators:
    """
    Класс для хранения локаторов для страницы Завершение заказа
    """
    LOCATOR_COMPLETE = (By.CLASS_NAME, "complete-header")
    LOCATOR_BACK = (By.ID, "back-to-products")
