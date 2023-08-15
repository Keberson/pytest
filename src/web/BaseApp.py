from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome


class BasePage:
    """
    Базовый класс для работы с WebDriver Chrome
    """

    def __init__(self, driver: Chrome):
        self.driver: Chrome = driver
        self.base_url = "https://www.saucedemo.com/"

    def go_to(self, url=''):
        """
        Переход по начальному URL
        """
        self.driver.get(url if url != '' else self.base_url)

    def find_element(self, locator, time=10):
        """
        Поиск элемента на странице по локатору в течение заданного времени.
        Если элемент не найден, то будет выброшено исключение
        :param locator: локатор элемента для поиска
        :param time: время, в течение которого осуществляется поиск, по умолчанию 10 секунд
        :return: искомый элемент
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        """
        Поиск всех элементов на странице по локатору в течение заданного времени.
        Если элементы не найдены, то будет выброшено исключение
        :param locator: локатор элементов для поиска
        :param time: время, в течение которого осуществляется поиск, по умолчанию 10 секунд
        :return: искомые элементы
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def enter_text(self, locator, text):
        """
        Метод для ввода текста в элемент по локатору
        :param locator: локатор элемента
        :param text: вводимый текст
        :return: элемент с введенным текстом
        """
        field = self.find_element(locator)
        field.click()
        field.send_keys(text)

        return field

    def click_on_the_button(self, locator):
        """
        Метод для нажатия на элемент по локатору
        :param locator: локатор элемента
        """
        self.find_element(locator).click()

    def check_element(self, locator) -> bool:
        """
        Метод для проверки наличия элемента с заданным локатором на странице
        :param locator: локатор элемента
        :return: True - если элемент найден, False - не найден
        """
        try:
            self.find_element(locator, time=2)
        except TimeoutException:
            return False

        return True
