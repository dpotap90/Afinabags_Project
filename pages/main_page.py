import time
import allure
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):
    """Страница главной страницы Afinabags.ru"""
    url = "https://afinabags.ru/"


    # Locators
    catalog_menu = "//header/div[2]/ul/li[1]/a"
    all_catalog = "//a[text()='Посмотреть все']"
    open_user = "//div[@class='header-top__control-item header-top__user']"
    button_user_mail = "//button[text()='Войти по почте']"
    email_user = "//input[@id='email']"
    password_user = "//input[@id='pass']"
    button_user_check = "//div[contains(@class, 'header-top__user')]"

    # Getters

    def get_hover_over_element_catalog(self):
        """Получить элемент 'Каталог' для наведения."""
        return self.element_is_visible((By.XPATH, self.catalog_menu))

    def get_select_all_catalog(self):
        """Получить элемент 'Посмотреть все' для выбора."""
        return self.element_is_clickable((By.XPATH, self.all_catalog))

    def get_open_user(self):
        return self.element_is_clickable((By.XPATH, self.open_user))

    def get_button_user_mail(self):
        return self.element_is_clickable((By.XPATH, self.button_user_mail))

    def get_email_user(self):
        return self.element_is_clickable((By.XPATH, self.email_user))

    def get_password_user(self):
        return self.element_is_clickable((By.XPATH, self.password_user))

    def get_button_user_check(self):
        return self.element_is_clickable((By.XPATH, self.button_user_check))


    # Actions
    def hover_over_and_click_all_catalog(self):
        """Навести курсор на 'Каталог' и кликнуть по 'Посмотреть все'."""
        self.action_move_to_element(self.get_hover_over_element_catalog())
        self.get_select_all_catalog().click()
        print("Click select_all_catalog")

    def click_open_user(self):
        self.get_open_user().click()
        print("Click open_user")

    def click_button_user_mail(self):
        self.get_button_user_mail().click()
        print("Click button_user_mail")

    def input_email_user(self, email_user):
        self.get_email_user().send_keys(email_user)
        print("Input email_user")

    def input_password_user(self, password_user):
        self.get_password_user().send_keys(password_user)
        print("Input email_user")

    def click_button_user_check(self):
        self.get_button_user_check().click()
        print("Click button_user_check")

    # Methods

    def select_catalogs(self):
        """Выполнить действия по выбору каталога."""
        with allure.step("select_catalogs"):
            Logger.add_start_step(method="select_catalogs")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.hover_over_and_click_all_catalog()
            self.assert_url("https://afinabags.ru/catalog/")
            # self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="select_catalogs")


    def authorization(self):
        """Авторизация пользователя"""
        with allure.step("authorization"):
            Logger.add_start_step(method="select_catalogs")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_open_user()
            self.input_email_user("123@test.ru")
            self.input_password_user("test")
            self.click_button_user_check()
            self.get_current_url()
            self.assert_url("https://afinabags.ru/personal/")
            self.assert_text_on_page("Личный кабинет")