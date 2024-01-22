import allure
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):
    """Страница главной страницы Afinabags.ru"""
    url = "https://afinabags.ru/"


    # Locators
    catalog_menu = ("//header/div[2]/ul/li[1]/a")
    all_catalog = "//a[text()='Посмотреть все']"

    # Getters

    def get_hover_over_element_catalog(self):
        """Получить элемент 'Каталог' для наведения."""
        return self.element_is_visible((By.XPATH, self.catalog_menu))

    def get_select_all_catalog(self):
        """Получить элемент 'Посмотреть все' для выбора."""
        return self.element_is_clickable((By.XPATH, self.all_catalog))

    # Actions
    def hover_over_and_click_all_catalog(self):
        """Навести курсор на 'Каталог' и кликнуть по 'Посмотреть все'."""
        self.action_move_to_element(self.get_hover_over_element_catalog())
        self.get_select_all_catalog().click()
        print("Click select_all_catalog")


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


