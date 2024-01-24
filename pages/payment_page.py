import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


class OrderCartPage(Base):
    """Страница оформления заказа"""
    url = "https://afinabags.ru/order/"

    # Locators

    first_name = "//input[@name='ORDER_PROP_1']"
    last_name = "//input[@name='ORDER_PROP_2']"
    email_name = "//input[@name='ORDER_PROP_3']"
    phone_number = "//input[@name='ORDER_PROP_4']"
    city_spb = "//div[@class='big-city '][1]"
    city_msk = "//div[@class='big-city '][2]"
    delivery_courier = "//label[contains(@class,'checkout-content')][1]"
    delivery_sdek = "//label[contains(@class,'checkout-content')][2]"
    adress_sdek = "//p[@id='PVZ_MSK77']"
    sdek_button_pvz = "//a[@id='SDEK_button']"
    search_pvz = "//div[@id='SDEK_looper']"
    name_search_pvz = "//input[@class='ymaps-2-1-79-searchbox-input__input']"
    button_search_input = "//ymaps[@class='ymaps-2-1-79-searchbox-button-text']"
    pvz_msk = "//ymaps[text()='Москва']"
    payment_method_cash = "//div[text()='Оплата при получении']"
    payment_method_card = "//div[text()='Оплата онлайн']"
    street_name = "//input[@id='street']"
    house_name = "//input[@name='ORDER_PROP_18']"
    order_button = "//a/button[@type='submit']"


    # Getters

    def get_first_name(self):
        """Получить элемент для поля 'Имя'."""
        return self.element_is_clickable((By.XPATH, self.first_name))

    def get_last_name(self):
        """Получить элемент для поля 'Фамилия'."""
        return self.element_is_clickable((By.XPATH, self.last_name))

    def get_email_name(self):
        """Получить элемент для поля 'Email'."""
        return self.element_is_clickable((By.XPATH, self.email_name))

    def get_phone_number(self):
        """Получить элемент для поля 'Номер телефона'."""
        return self.element_is_clickable((By.XPATH, self.phone_number))

    def get_city_spb(self):
        """Получить элемент для кнопки города "Санкт-Петербург"""
        return self.element_is_clickable((By.XPATH, self.city_spb))

    def get_city_msk(self):
        """Получить элемент для кнопки города "Москва"""
        return self.element_is_clickable((By.XPATH, self.city_msk))

    def get_delivery_courier(self):
        """Получить элемент для выбора доставки курьером."""
        return self.element_is_clickable((By.XPATH, self.delivery_courier))

    def get_delivery_sdek(self):
        """Получить элемент для выбора доставки СДЭК."""
        return self.element_is_clickable((By.XPATH, self.delivery_sdek))

    def get_select_adress_sdek(self):
        """Получить элемент для выбора пункта самовывоза СДЭК."""
        return self.element_is_clickable((By.XPATH, self.adress_sdek))

    def get_sdek_button_pvz(self):
        """Получить элемент для выбора пункта самовывоза СДЭК."""
        return self.element_is_clickable((By.XPATH, self.sdek_button_pvz))
    def get_search_pvz(self):
        """Получить элемент для кнопки поиска пункта самовывоза СДЭК."""
        return self.element_is_clickable((By.XPATH, self.search_pvz))

    def get_name_search_pvz(self):
        """Получить элемент для поиска пункта самовывоза СДЭК."""
        return self.element_is_clickable((By.XPATH, self.name_search_pvz))

    def get_button_search_input(self):
        """Получить элемент для кнопки Найти."""
        return self.element_is_clickable((By.XPATH, self.button_search_input))

    def get_pvz_msk(self):
        "Получить пвз МОСКВА из списка"
        return self.element_is_clickable((By.XPATH, self.pvz_msk))


    def get_payment_method_cash(self):
        """Получить элемент для выбора метода оплаты 'Оплата при получении'."""
        return self.element_is_clickable((By.XPATH, self.payment_method_cash))

    def get_payment_method_card(self):
        """Получить элемент для выбора метода оплаты 'Оплата онлайн'."""
        return self.element_is_clickable((By.XPATH, self.payment_method_card))

    def get_street_name(self):
        """Получить элемент для поля 'Улица'."""
        return self.element_is_clickable((By.XPATH, self.street_name))

    def get_house_name(self):
        """Получить элемент для поля 'Дом'."""
        return self.element_is_clickable((By.XPATH, self.house_name))


    def get_order_button(self):
        """Получить элемент для кнопки оформления заказа."""
        return self.element_is_clickable((By.XPATH, self.order_button))

    # Actions

    def input_first_name(self, first_name):
        """Ввод данных для поля Имя."""
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        """Ввод данных для поля Фамилия."""
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_email_name(self, email_name):
        """Ввод данных для поля Почта."""
        self.get_email_name().send_keys(email_name)
        print("Input email_name")

    def input_phone_number(self, phone_number):
        """Ввод данных для поля Телефон"""
        self.get_phone_number().send_keys(phone_number)
        print("Input phone_number")

    def select_city_spb(self):
        """Выполнить выбор города Санкт-Петербург'"""
        self.get_city_spb().click()
        print("Select city_spb")

    def select_city_msk(self):
        """Выполнить выбор города Москва'"""
        self.get_city_msk().click()
        print("Select city_msk")


    def scroll_to_delivery_1_and_select(self):
        """Прокрутить страницу до элемента и выбор способа доставки Курьером"""
        self.action_move_to_element(self.get_delivery_courier())
        self.get_delivery_courier().click()
        print("Select delivery_courier")

    def scroll_to_delivery_2_and_select(self):
        """Прокрутить страницу до элемента и выбор способа доставки СДЭК"""
        self.action_move_to_element(self.get_delivery_sdek())
        self.get_delivery_sdek().click()
        print("Select delivery_sdek")

    def select_adress_sdek(self):
        """Выбор адреса ПВЗ"""
        self.element_is_clickable((By.XPATH, self.adress_sdek))
        print("Select adress_sdek")


    def click_adress_sdek(self):
        """Клик по адресу Сдэк"""
        self.element_is_clickable((By.XPATH, self.adress_sdek))
        print("Click adress_sdek")


    def click_sdek_button_pvz(self):
        """Клик по кнопке "Выбрать"""
        self.element_is_clickable((By.XPATH, self.sdek_button_pvz))
        print("Click sdek_button_pvz")

    def click_search_pvz(self):
        """Клик по кнопке "Поиск"""
        self.element_is_clickable((By.XPATH, self.search_pvz))
        print("Click search_pvz")

    def click_name_search_pvz(self):
        """Клик по полю "Адрес или объект"""
        self.element_is_clickable((By.XPATH, self.name_search_pvz))
        print("Click search_pvz")

    def input_name_search_pvz(self, name_search_pvz):
        """Ввод данных в поле Улица"""
        self.get_name_search_pvz().send_keys(name_search_pvz)
        print("Input_name_search_pvz")

    def click_button_search_input(self):
        """Клик по кнопке Найти"""
        self.element_is_clickable((By.XPATH, self.button_search_input))
        print("Click button_search_input")

    def select_pvz_msk(self):
        """Выбор ПВЗ Москва из списка """
        self.get_pvz_msk().click()
        print("select_pvz_msk")


    def input_street_name(self, street_name):
        """Ввод данных в поле Улица"""
        self.get_street_name().send_keys(street_name)
        print("Input_street_name")

    def input_house_name(self, house_name):
        """Ввод данных в поле Дом"""
        self.get_house_name().send_keys(house_name)
        print("Input_house_name")

    def scroll_to_payment_card(self):
        """Прокрутить страницу до элемента оплата Картой"""
        self.action_move_to_element(self.get_payment_method_card())
        print("Select payment_method")

    def click_payment_method_cash(self):
        """Выполнить клик по кнопке 'Оплата при получении'"""
        self.get_payment_method_cash().click()
        print("Select payment_method Cash")

    def click_order_button(self):
        """Выполнить клик по кнопке 'Оформить заказ'"""
        self.get_order_button().click()
        print("Click order_button")


    # Methods
    def order_cart_1(self):
        """Оформлению заказа c доставкой курьером и оплатой наличными."""
        with allure.step("order_cart_1"):
            Logger.add_start_step(method="order_cart_1")
            self.get_current_url()  # Текущий URL
            self.assert_url("https://afinabags.ru/order/")  # Проверка URL
            self.input_first_name("Test")  # Ввод данных для поля "Имя"
            self.input_last_name("Testovich")  # Ввод данных для поля "Фамилия"
            self.input_email_name("123@test.ru")  # Ввод данных для поля "Почта"
            self.input_phone_number("0000000000")  # Ввод данных для поля "Телефон"
            self.select_city_spb()  # Выбор города "Санкт-Петербург"
            self.scroll_to_delivery_1_and_select()  # Прокрутить страницу до элемента и выбор способа доставки Курьером
            self.input_street_name("test_street")  # Ввод данных в поле Улица
            self.input_house_name("test_home")  # Ввод данных в поле Улица
            self.scroll_to_payment_card()  # Прокрутить страницу до элемента "Оплата Картой"
            self.click_payment_method_cash()  # Клик по кнопке "Оплата при получении"
            # self.click_order_button()  # Клик по кнопке "Оформить заказ"
            # self.assert_text_on_page("Ваш заказ")  # Проверка отображения текста на странице
            # self.assert_text_on_page("Оплата при получении") # Проверка отображения текста на странице
            Logger.add_end_step(url=self.driver.current_url, method="order_cart_1")

    def order_cart_2(self):
        """Оформлению заказа c доставкой сдэка и оплатой наличными."""
        with allure.step("order_cart_2"):
            Logger.add_start_step(method="order_cart_2")
            self.get_current_url()  # Текущий URL
            self.assert_url("https://afinabags.ru/order/")  # Проверка URL
            self.input_first_name("Test")  # Ввод данных для поля "Имя"
            self.input_last_name("Testovich")  # Ввод данных для поля "Фамилия"
            self.input_email_name("123@test.ru")  # Ввод данных для поля "Почта"
            self.input_phone_number("0000000000")  # Ввод данных для поля "Телефон"
            self.select_city_msk()  # Выбор города "Москва"
            self.scroll_to_delivery_2_and_select()  # Прокрутить страницу до элемента и выбор способа доставки СДЭК
            self.click_adress_sdek()  # Выбор адреса ПВЗ MSK77
            self.click_sdek_button_pvz()  # Клик по кнопке "Выбрать"
            # self.click_search_pvz()
            # self.click_name_search_pvz()
            # self.input_name_search_pvz("Выбранный пункт: пер. Товарищеский , 1, стр. 2")
            # self.click_button_search_input()
            # self.select_pvz_msk()
            self.scroll_to_payment_card()    # Прокрутить страницу до элемента "Оплата Картой"
            self.click_payment_method_cash()    # Клик по кнопке "Оплата при получении"
            # self.click_order_button()  # Клик по кнопке "Оформить заказ"
            # self.assert_text_on_page("Ваш заказ")  # Проверка отображения текста на странице
            # self.assert_text_on_page("Оплата при получении") # Проверка отображения текста на странице

            Logger.add_end_step(url=self.driver.current_url, method="order_cart_2")




