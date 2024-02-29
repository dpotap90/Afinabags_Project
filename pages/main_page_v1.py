import time
import allure
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):
    """Страница главной страницы Afinabags.ru"""
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://afinabags.ru/"

    # Locators
    catalog_menu = "/html/body/header/div[3]/ul/li[1]/a"
    all_catalog = "//a[text()='Посмотреть все']"
    open_user = "//div[@class='header-top__control-item header-top__user']"
    button_user_mail = "//button[contains(@class, 'js-open-email')]"
    email_user = "//input[@id='email']"
    password_user = "//input[@id='pass']"
    button_user_check = "//button[contains(@class, 'email-auth')]"

    # Getters

    def get_hover_over_element_catalog(self):
        """Получить элемент 'Каталог' для наведения."""
        return self.element_is_visible((By.XPATH, self.catalog_menu))

    def get_select_all_catalog(self):
        """Получить элемент 'Посмотреть все' для выбора."""
        return self.element_is_clickable((By.XPATH, self.all_catalog))

    def get_open_user(self):
        """Получить элемент открытия меню пользователя"""
        return self.element_is_clickable((By.XPATH, self.open_user))

    def get_button_user_mail(self):
        """Получить кнопку "Открыть почту"""
        return self.element_is_clickable((By.XPATH, self.button_user_mail))

    def get_email_user(self):
        """Получить поле ввода электронной почты пользователя"""
        return self.element_is_clickable((By.XPATH, self.email_user))

    def get_password_user(self):
        """Получить поле ввода пароля пользователя"""
        return self.element_is_clickable((By.XPATH, self.password_user))

    def get_button_user_check(self):
        """Получить кнопку "Проверить пользователя"""
        return self.element_is_clickable((By.XPATH, self.button_user_check))

    # Actions
    def hover_over_and_click_all_catalog(self):
        """Навести курсор на 'Каталог' и кликнуть по 'Посмотреть все'."""
        self.action_move_to_element(self.get_hover_over_element_catalog())
        self.get_select_all_catalog().click()
        print("Click select_all_catalog")

    def click_open_user(self):
        """Клик по элементу открытия меню пользователя"""
        self.get_open_user().click()
        print("Click open_user")

    def click_button_user_mail(self):
        """Клик по кнопке "Войти по почте"""
        self.get_button_user_mail().click()
        print("Click button_user_mail")

    def input_email_user(self, email_user):
        """Ввод электронной почты пользователя"""
        self.get_email_user().send_keys(email_user)
        print("Input email_user")

    def input_password_user(self, password_user):
        """Ввод пароля пользователя"""
        self.get_password_user().send_keys(password_user)
        print("Input email_user")

    def click_button_user_check(self):
        """Клик по кнопке "Войти"""
        self.get_button_user_check().click()
        print("Click button_user_check")

    # Methods

    def select_catalogs(self):
        """Выполнить действия по выбору каталога и раздела 'Выбрать все'"""
        with allure.step("select_catalogs"):
            Logger.add_start_step(method="select_catalogs")
            self.load_page_and_maximize(self.url)  # Загрузить страницу и максимизировать окно браузера
            self.hover_over_and_click_all_catalog()  # Навести курсор на 'Каталог' и кликнуть по 'Посмотреть все'
            self.assert_url("https://afinabags.ru/catalog/")  # Проверяем URL
            Logger.add_end_step(url=self.driver.current_url, method="select_catalogs")

    def authorization(self):
        """Авторизация пользователя"""
        with allure.step("authorization"):
            Logger.add_start_step(method="authorization")
            self.load_page_and_maximize(self.url)  # Загрузить страницу и максимизировать окно браузера
            self.click_open_user()  # Клик по элементу открытия меню пользователя
            self.click_button_user_mail()  # Клик по кнопке "Войти по почте"
            self.input_email_user("123@test.ru")  # Ввод электронной почты пользователя
            self.input_password_user("testovich")  # Ввод пароля пользователя
            self.click_button_user_check()  # Клик по кнопке "Войти"
            self.assert_url(self.url + "personal/")  # Проверяем URL
            self.assert_text_on_page("Личный кабинет") # Проверка отображения текста на странице
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
