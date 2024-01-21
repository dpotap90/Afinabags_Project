import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Order_cart_page(Base):

    # Locators

    first_name = "//input[@name='ORDER_PROP_1']"
    last_name = "//input[@name='ORDER_PROP_2']"
    email_name = "//input[@name='ORDER_PROP_3']"
    phone_number = "//input[@name='ORDER_PROP_4']"
    city_1 = "//div[@class='big-city '][1]"
    delivery_courier = "//label[contains(@class,'checkout-content')][1]"
    payment_method_1 = "//div[text()='Оплата при получении']"
    street_name = "//input[@name='ORDER_PROP_17']"
    house_name = "//input[@name='ORDER_PROP_18']"
    # order_button = "//a/button[@type='submit']"


    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_email_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_name)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_city_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_1)))

    def get_delivery_courier(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_courier)))

    def get_payment_method_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_method_1)))

    def get_street_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.street_name)))

    def get_house_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.house_name)))


    # def get_order_button(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))

    # Actions

    def input_first_name(self, first_name):
        """Получить элемент поля Имя."""
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        """Получить элемент поля Фамилия."""
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_email_name(self, email_name):
        """Получить элемент поля Почта."""
        self.get_email_name().send_keys(email_name)
        print("Input email_name")

    def input_phone_number(self, phone_number):
        """Получить элемент поля Телефон."""
        self.get_phone_number().send_keys(phone_number)
        print("Input phone_number")

    def select_city_1(self):
        """Выполнить выбор города 1'"""
        self.get_city_1().click()
        print("Select city_1")

    def scroll_to_delivery_1_and_select(self):
        """Прокрутить страницу до элемента  и выбор способа доставки"""
        action = ActionChains(self.driver)
        action.move_to_element(self.get_delivery_courier()).perform()
        self.get_delivery_courier().click()
        print("Select delivery_courier")

    def input_street_name(self):
        """Ввод данныз в поле Улица"""
        # action = ActionChains(self.driver)
        # action.move_to_element(self.get_payment_method_1()).perform()
        self.get_street_name().send_keys("test")
        print("Input_house_name")

    def input_house_name(self):
        """Ввод данныз в поле Дом"""
        # action = ActionChains(self.driver)
        # action.move_to_element(self.get_payment_method_1()).perform()
        self.get_house_name().send_keys("test")
        print("Input_house_name")

    def scroll_to_payment_method_1_and_select(self):
        """Прокрутить страницу до элемента  и выбор способа оплаты 1"""
        action = ActionChains(self.driver)
        action.move_to_element(self.get_payment_method_1()).perform()
        self.get_payment_method_1().click()
        print("Select payment_method")


    # def click_order_button(self):
    """Выполнить клик по кнопке 'Оформить заказ'"""
    #     self.get_order_button().click()
    #     print("Click order_button")


    # Methods
    def order_cart(self):
        """Выполнить действия по оформлению заказа."""
        with allure.step("order_cart"):
            Logger.add_start_step(method="cart_and_checkout_products_692")
            self.get_current_url()
            self.assert_url("https://afinabags.ru/order/")
            self.input_first_name("Test")
            self.input_last_name("Testovich")
            self.input_email_name("123@test.ru")
            self.input_phone_number("0000000000")
            self.select_city_1()
            self.scroll_to_delivery_1_and_select()
            self.input_street_name()
            self.input_house_name()
            self.scroll_to_payment_method_1_and_select()
            # self.click_order_button()
            # self.get_screenshot()
            "cart_and_checkout_products_692"
            Logger.add_end_step(url=self.driver.current_url, method="cart_and_checkout_products_692")




