import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base
from utilities.logger import Logger


class CatalogPage(Base):

    """Страница каталога на Afinabags.ru"""
    url = "https://afinabags.ru/catalog/"

    # Locators
    filter_open = "//div[contains(@class,'js-filter-modal')]"
    filter_price_open = "//div[text()='Цена']"
    slider_price = "//span[@tabindex='0'][1]"
    button_slider_price = "//button[@id='modal_filter_btn']"
    select_product_692 = "//div[@id='good-5109']"
    mail_word = "//h1[@itemprop='name']"

    # Getters

    def get_filter_open(self):
        return self.element_is_clickable((By.XPATH, self.filter_open))

    def get_filter_price_open(self):
        """Получить элемент 'Открыть фильтр'."""
        return self.element_is_clickable((By.XPATH, self.filter_price_open))

    def get_slider_price(self):
        """Получить элемент слайдера цены."""
        return self.element_is_clickable((By.XPATH, self.slider_price))

    def get_button_slider_price(self):
        """Получить элемент кнопки слайдера цены."""
        return self.element_is_clickable((By.XPATH, self.button_slider_price))

    def get_select_product_692(self):
        """Получить элемент продукта 692"""
        return self.element_is_clickable((By.XPATH, self.select_product_692))

    def get_mail_word(self):
        """Получить элемент заголовка с информацией о продукте."""
        return self.element_is_clickable((By.XPATH, self.mail_word))

    # Actions

    def click_filter_open(self):
        """Выполнить клик по элементу фильтра."""
        self.get_filter_open().click()
        print("Click filter_open")

    def click_filter_price_open(self):
        """Выполнить клик по слайдеру цены"""
        self.get_filter_price_open().click()
        print("Click filter_price_open")

    def slider_prices(self):
        """Клик и Перемещение слайдера цены."""
        self.action_click_and_hold(self.get_slider_price(), 20, 0)
        print("Click slider_prices")

    def button_slider_prices(self):
        """Выполнить клик по кнопке 'Применить'"""
        self.get_button_slider_price().click()
        print("Click button_slider_prices")

    def scroll_to_product_692(self):
        """Прокрутить страницу до элемента продукта 692."""
        action = ActionChains(self.driver)
        action.scroll_to_element(self.get_select_product_692()).perform()
        print("Scroll to_product_692")

    def click_select_product_692(self):
        """Выполнить выбор продукта 692'"""
        self.get_select_product_692().click()
        print("Click select_product_692")



    # Methods

    def select_products_692(self):
        """Выполнить действия для выбора продукта 692"""
        with allure.step("select_products_692"):
            Logger.add_start_step(method="select_products_692")
            self.click_filter_open()  # Клик по элементу фильтра
            self.click_filter_price_open()  # Выполнить клик по слайдеру цены
            self.slider_prices()  # Клик и Перемещение слайдера цены
            self.button_slider_prices()  # Клик по кнопке 'Применить'
            self.scroll_to_product_692()  # Прокрутить страницу до элемента продукта 692
            self.click_select_product_692()  # Выбор продукта 692
            self.assert_url("https://afinabags.ru/catalog/sumki_i_ryukzaki/model-692/")  # Проверка URL
            self.assert_word(self.get_mail_word(), "Модель 692")  # Проверка отображение текста "Модель 692"
            # self.get_screenshot()  # Скриншот страницы
            Logger.add_end_step(url=self.driver.current_url, method="select_products_692")