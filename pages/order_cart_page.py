import time
import allure
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger

class OrderForm(Base):
    """Класс для работы с формой оформления заказа."""
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://afinabags.ru/order/"

    # Locators
    first_name = "//input[@name='ORDER_PROP_1']"
    last_name = "//input[@name='ORDER_PROP_2']"
    email_name = "//input[@name='ORDER_PROP_3']"
    phone_number = "//input[@name='ORDER_PROP_4']"
    street_name = "//input[@id='street']"
    house_name = "//input[@name='ORDER_PROP_18']"

    # Actions
    def input_first_name(self, first_name):
        """Ввод данных для поля Имя"""
        self.element_is_clickable((By.XPATH, self.first_name)).send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        """Ввод данных для поля Фамилия"""
        self.element_is_clickable((By.XPATH, self.last_name)).send_keys(last_name)
        print("Input last name")

    def input_email_name(self, email_name):
        """Ввод данных для поля Почта"""
        self.element_is_clickable((By.XPATH, self.email_name)).send_keys(email_name)
        print("Input email_name")

    def input_phone_number(self, phone_number):
        """Ввод данных для поля Телефон"""
        self.element_is_clickable((By.XPATH, self.phone_number)).send_keys(phone_number)
        print("Input phone_number")

    def input_street_name(self, street_name):
        """Ввод данных в поле Улица"""
        self.element_is_clickable((By.XPATH, self.street_name)).send_keys(street_name)
        print("Input_street_name")

    def input_house_name(self, house_name):
        """Ввод данных в поле Дом"""
        self.element_is_clickable((By.XPATH, self.house_name)).send_keys(house_name)
        print("Input_house_name")


class OrderOptions(Base):
    """Класс для выбора опций оформления заказа."""

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    city_spb = "//div[@class='big-city '][1]"
    city_msk = "//div[@class='big-city '][2]"
    delivery_courier = "//label[contains(@class,'checkout-content')][1]"
    delivery_sdek = "//label[contains(@class,'checkout-content')][2]"
    payment_method_cash = "//div[text()='Оплата при получении']"
    payment_method_card = "//div[text()='Оплата онлайн']"
    adress_sdek = "//p[@id='PVZ_MSK77']"
    sdek_button_pvz = "//a[@id='SDEK_button']"
    search_pvz = "//div[@id='SDEK_looper']"
    name_search_pvz = "//input[@class='ymaps-2-1-79-searchbox-input__input']"
    button_search_input = "//ymaps[@class='ymaps-2-1-79-searchbox-button-text']"
    pvz_msk = "//ymaps[text()='Москва']"

    def select_city_spb(self):
        """Выполнить выбор города 'Санкт-Петербург'"""
        self.element_is_clickable((By.XPATH, self.city_spb)).click()
        print("Select city_spb")

    def select_city_msk(self):
        """Выполнить выбор города 'Москва'"""
        self.element_is_clickable((By.XPATH, self.city_msk)).click()
        print("Select city_msk")

    def scroll_to_delivery_courier_and_select(self):
        """Прокрутить страницу до элемента и выбор способа доставки Курьером"""
        self.action_move_to_element(self.element_is_clickable((By.XPATH, self.delivery_courier)))
        self.element_is_clickable((By.XPATH, self.delivery_courier)).click()
        print("Select delivery_courier")

    def scroll_to_delivery_sdek_and_select(self):
        """Прокрутить страницу до элемента и выбор способа доставки СДЭК"""
        self.action_move_to_element(self.element_is_clickable((By.XPATH, self.delivery_sdek)))
        self.element_is_clickable((By.XPATH, self.delivery_sdek)).click()
        print("Select delivery_sdek")

    def select_adress_sdek(self):
        """Выбрать адрес пвз Сдэк"""
        self.element_is_clickable((By.XPATH, self.adress_sdek)).click()
        print("Select adress_sdek")

    def click_sdek_button_pvz(self):
        """Клик по кнопке "Выбрать пвз"""
        self.element_is_clickable((By.XPATH, self.sdek_button_pvz)).click()
        print("Сlick sdek_button_pvz")

    def scroll_to_payment_cash_and_select(self):
        """Прокрутить страницу до элемента и выбор способа оплаты 'Оплата при получении' """
        self.action_move_to_element(self.element_is_clickable((By.XPATH, self.payment_method_cash)))
        self.element_is_clickable((By.XPATH, self.payment_method_cash)).click()
        print("Select payment_method_cash")

    def scroll_to_payment_card_and_select(self):
        """Прокрутить страницу до элемента и выбор способа оплаты 'Оплата онлайн' """
        self.action_move_to_element(self.element_is_clickable((By.XPATH, self.payment_method_card)))
        self.element_is_clickable((By.XPATH, self.payment_method_card)).click()
        print("Select payment_method_cash")


class OrderCartPage(OrderForm, OrderOptions):
    """Страница оформления заказа"""
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    order_button = "//a/button[@type='submit']"

    # Getters
    def get_order_button(self):
        """Получить элемент для кнопки оформления заказа"""
        return self.element_is_clickable((By.XPATH, self.order_button))

    # Actions
    def click_order_button(self):
        """Выполнить клик по кнопке 'Оформить заказ'"""
        self.get_order_button().click()
        print("Click order_button")

class OrderTest(OrderCartPage):
    """Тестовый класс для процесса оформления заказа в Корзине"""
    def __init__(self, driver):
        super().__init__(driver)

    # Test_Methods
    def order_cart_1(self):
        """Оформление заказа с доставкой курьером и оплатой наличными."""
        with allure.step("order_cart_1"):
            Logger.add_start_step(method="order_cart_1")
            self.load_page_and_maximize(self.url)  # Загрузить страницу и максимизировать окно браузера
            self.input_first_name("Test")  # Ввод данных для поля "Имя"
            self.input_last_name("Testovich")  # Ввод данных для поля "Фамилия"
            self.input_email_name("123@test.ru")  # Ввод данных для поля "Почта"
            self.input_phone_number("0000000000")  # Ввод данных для поля "Телефон"
            self.select_city_spb()  # Выбор города "Москва"
            self.scroll_to_delivery_courier_and_select()  # Прокрутить страницу до элемента и выбрать способ доставки 'Курьером'
            self.input_street_name("test_street")  # Ввод данных в поле Улица
            self.input_house_name("test_home")  # Ввод данных в поле Дом
            self.scroll_to_payment_cash_and_select()  # Прокрутить страницу до элемента и выбрать "Оплата при получении"
            # self.click_order_button()  # Клик по кнопке "Оформить заказ"
            # self.assert_text_on_page("Ваш заказ")  # Проверка отображения текста "Ваш заказ" на странице
            # self.assert_text_on_page("Оплата при получении") # Проверка отображения текста "Оплата при получении" на странице
            Logger.add_end_step(url=self.driver.current_url, method="order_cart_1")

    def order_cart_2(self):
        """Оформление заказа с доставкой СДЭК и оплатой наличными."""
        with allure.step("order_cart_2"):
            Logger.add_start_step(method="order_cart_2")
            self.load_page_and_maximize(self.url)  # Загрузить страницу и максимизировать окно браузера
            self.input_first_name("Test")  # Ввод данных для поля "Имя"
            self.input_last_name("Testovich")  # Ввод данных для поля "Фамилия"
            self.input_email_name("123@test.ru")  # Ввод данных для поля "Почта"
            self.input_phone_number("0000000000")  # Ввод данных для поля "Телефон"
            self.select_city_msk()  # Выбор города "Москва"
            self.scroll_to_delivery_sdek_and_select()  # Прокрутить страницу до элемента и выбрать способ доставки 'Пункт выдачи (СДЭК)'
            self.select_adress_sdek()  # Выбор адреса ПВЗ"
            self.click_sdek_button_pvz()  # Клик по кнопке 'Выбрать пвз'"
            self.scroll_to_payment_cash_and_select()  # Прокрутить страницу до элемента и выбрать "Оплата при получении"
            self.assert_text_on_page("Выбранный пункт: пер. Товарищеский , 1, стр. 2")  # Проверка отображения выбранного пвз СДЭК
            # self.click_order_button()  # Клик по кнопке "Оформить заказ"
            # self.assert_text_on_page("Ваш заказ")
            # self.assert_text_on_page("Оплата при получении") # Проверка отображения текста "Оплата при получении" на странице

            Logger.add_end_step(url=self.driver.current_url, method="order_cart_2")
