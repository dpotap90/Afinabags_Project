import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base
from utilities.logger import Logger


class Catalog_page(Base):

    url = "https://afinabags.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    filter_open = "//div[contains(@class,'js-filter-modal')]"
    filter_price_open = "//div[text()='Цена']"
    slider_price = "//span[@tabindex='0'][1]"
    button_slider_price = "//button[@id='modal_filter_btn']"
    select_product_692 = "//div[@id='good-5109']"
    mail_word = "//h1[@itemprop='name']"

    # Getters

    def get_filter_open(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_open)))

    def get_filter_price_open(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_open)))

    def get_slider_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_price)))

    def get_button_slider_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_slider_price)))

    def get_select_product_692(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_692)))

    def get_mail_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail_word)))

    # Actions

    def click_filter_open(self):
        self.get_filter_open().click()
        print("Click filter_open")

    def click_filter_price_open(self):
        self.get_filter_price_open().click()
        print("Click filter_price_open")

    def slider_prices(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_slider_price()).move_by_offset(20, 0).release().perform()
        print("Click slider_prices" )

    def button_slider_prices(self):
        self.get_button_slider_price().click()
        print("Click button_slider_prices")

    def scroll_to_product_692(self):
        action = ActionChains(self.driver)
        action.scroll_to_element(self.get_select_product_692()).perform()
        print("Scroll to_product_692")

    def click_select_product_692(self):
        self.get_select_product_692().click()
        print("Click select_product_692")



    # Methods

    def select_products_692(self):
        with allure.step("select_products_692"):
            Logger.add_start_step(method="select_products_692")
            self.get_current_url()
            self.click_filter_open()
            self.click_filter_price_open()
            self.slider_prices()
            self.button_slider_prices()
            self.scroll_to_product_692()
            self.click_select_product_692()
            self.assert_url("https://afinabags.ru/catalog/sumki_i_ryukzaki/model-692/")
            self.assert_word(self.get_mail_word(), "Модель 692")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="select_products_692")