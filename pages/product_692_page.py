import allure
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


class Product_692_page(Base):

    """Страница продукта 692 на Afinabags.ru"""

    url = "https://afinabags.ru/"

    # Locators

    cart = "//button[@class='item-card__control-btn-cart']"
    checkout_button = "//a[contains(@class, 'item-card__control-btn-cart-color')]"


    # Getters


    def get_cart(self):
        """Получить элемент кнопки 'В корзину'."""
        return self.element_is_clickable((By.XPATH, self.cart))

    def get_checkout_button(self):
        """Получить элемент кнопки 'Оформить заказ'."""
        return self.element_is_clickable((By.XPATH, self.checkout_button))


    # Actions

    def click_cart(self):
        """Выполнить клик по элементу 'Добавить в корзину"."""
        self.get_cart().click()
        print("Click cart")

    def scroll_checkout_button(self):
        """Прокрутить страницу до элемента."""
        self.driver.execute_script("window.scrollTo(0, 500);")
        print("Scroll checkout_button")

    def click_checkout_button(self):
        """Выполнить клик по элементу 'Перейти в корзину'"""
        self.get_checkout_button().click()
        print("Click checkout_button")

    # Methods

    def cart_and_checkout_products_692(self):
        """Выполнить действия по добавлению продукта в корзину и оформлению заказа."""
        with allure.step("cart_and_checkout_products_692"):
            Logger.add_start_step(method="cart_and_checkout_products_692")
            self.get_current_url()
            self.click_cart()
            self.scroll_checkout_button()
            self.click_checkout_button()
            self.assert_url("https://afinabags.ru/order/")
            # self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="cart_and_checkout_products_692")

