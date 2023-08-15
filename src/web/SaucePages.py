from src.web.BaseApp import BasePage
from selenium.webdriver.common.by import By


class LoginLocators:
    """
     Класс для хранения необходимых локаторов страницы Авторизации
     """
    LOCATOR_CONTAINER = (By.CLASS_NAME, "login_container")
    LOCATOR_USERNAME = (By.ID, "user-name")
    LOCATOR_PASSWORD = (By.ID, "password")
    LOCATOR_SUBMIT = (By.ID, "login-button")
    LOCATOR_ERROR = (By.CLASS_NAME, "error")


class CatalogLocators:
    """
    Класс для хранения необходимых локаторов страницы Каталога
    """
    LOCATOR_CONTAINER = (By.CLASS_NAME, "page_wrapper")
    LOCATOR_BURGER_BTN = (By.ID, "react-burger-menu-btn")
    LOCATOR_LOGOUT = (By.LINK_TEXT, "Logout")


class LoginHelper(BasePage):
    LOGIN_STANDARD = "standard_user"
    LOGIN_LOCKED = "locked_out_user"
    PASSWORD = "secret_sauce"

    def auth_standard(self) -> None:
        """
        Метод для аутентификация под стандартным пользователем
        """
        self.enter_text(LoginLocators.LOCATOR_USERNAME,
                        self.LOGIN_STANDARD)
        self.enter_text(LoginLocators.LOCATOR_PASSWORD,
                        self.PASSWORD)
        self.click_on_the_button(LoginLocators.LOCATOR_SUBMIT)

    def auth_locked(self) -> None:
        """
        Метод для аутентификации под заблокированным пользователем
        """
        self.enter_text(LoginLocators.LOCATOR_USERNAME,
                        self.LOGIN_LOCKED)
        self.enter_text(LoginLocators.LOCATOR_PASSWORD,
                        self.PASSWORD)
        self.click_on_the_button(LoginLocators.LOCATOR_SUBMIT)

    def logout(self) -> None:
        """
        Метод для выхода из системы
        """
        self.find_element(CatalogLocators.LOCATOR_BURGER_BTN).click()
        self.find_element(CatalogLocators.LOCATOR_LOGOUT).click()
