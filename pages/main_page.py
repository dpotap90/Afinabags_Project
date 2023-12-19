import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base

class Main_page(Base):

    url = "https://afinabags.ru/"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    catalog_menu = "//header/div[3]/ul/li[1]"
    all_catalog = "//a[text()='Посмотреть все']"

    # Getters

    def get_hover_over_element_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.catalog_menu)))

    def get_select_all_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.all_catalog)))

    def hover_over_and_click_all_catalog(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_hover_over_element_catalog()).perform()
        self.get_select_all_catalog().click()
        print("Click select_all_catalog")


    # Methods

    def select_catalogs(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.hover_over_and_click_all_catalog()
        self.assert_url("https://afinabags.ru/catalog/")
        self.get_screenshot()


