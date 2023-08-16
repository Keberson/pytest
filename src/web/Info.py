from selenium.webdriver.common.by import By


class Product:
    """
    Класс для хранения информации о товарах
    """
    PRODUCTS_NAME = [
        'Sauce Labs Backpack',
        'Sauce Labs Bike Light',
        'Sauce Labs Fleece Jacket',
        'Sauce Labs Bolt T-Shirt',
        'Sauce Labs Onesie',
        'Test.allTheThings() T-Shirt (Red)',
    ]

    PRODUCTS_PRICE = [
        29.99,
        9.99,
        49.99,
        15.99,
        7.99,
        15.99,
    ]

    PRODUCTS_ADD = [
        'add-to-cart-sauce-labs-backpack',
        'add-to-cart-sauce-labs-bike-light',
        'add-to-cart-sauce-labs-fleece-jacket',
        'add-to-cart-sauce-labs-bolt-t-shirt',
        'add-to-cart-sauce-labs-onesie',
        'add-to-cart-test.allthethings()-t-shirt-(red)',
    ]

    PRODUCTS_REMOVE = [
        'remove-sauce-labs-backpack',
        'remove-sauce-labs-bike-light',
        'remove-sauce-labs-fleece-jacket',
        'remove-sauce-labs-bolt-t-shirt',
        'remove-sauce-labs-onesie',
        'remove-test.allthethings()-t-shirt-(red)',
    ]

    @staticmethod
    def get_locator_list(to_convert: list[str], locator_type: str):
        """
        Метод для конвертации списка названий в список локаторов
        :param to_convert: список для конвертации
        :param locator_type: тип локатора
        :return: список локаторов
        """
        return [(locator_type, item) for item in to_convert]

    @staticmethod
    def get_name_add():
        """
        Метод для получения списка кортежей каждого товара вида: (Имя, локатор кнопки добавления)
        :return: список кортежей
        """
        return list(zip(Product.PRODUCTS_NAME, Product.get_locator_list(Product.PRODUCTS_ADD, By.ID)))

    @staticmethod
    def get_add_remove():
        """
        Метод для получения списка кортежей каждого товара вида: (локатор кнопки добавления, локатор кнопки удаления)
        :return: список кортежей
        """
        return list(zip(Product.get_locator_list(Product.PRODUCTS_ADD, By.ID),
                        Product.get_locator_list(Product.PRODUCTS_REMOVE, By.ID)))
