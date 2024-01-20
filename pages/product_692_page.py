import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Product_692_page(Base):

    url = "https://afinabags.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    cart = "//button[@class='item-card__control-btn-cart']"
    checkout_button = "//a[contains(@class, 'item-card__control-btn-cart-color')]"


    # Getters

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    # Actions

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def scroll_checkout_button(self):
        self.driver.execute_script("window.scrollTo(0, 500);")
        print("Scroll checkout_button")

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout_button")

    # Methods

    def cart_and_checkout_products_692(self):
        with allure.step("cart_and_checkout_products_692"):
            Logger.add_start_step(method="cart_and_checkout_products_692")
            self.get_current_url()
            self.click_cart()
            self.scroll_checkout_button()
            self.click_checkout_button()
            self.assert_url("https://afinabags.ru/order/")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="cart_and_checkout_products_692")

