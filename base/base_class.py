import datetime
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Base():

    def __init__(self, driver):
        self.driver = driver

    def load_page_and_maximize(self, url):
        """Загрузить страницу и максимизировать окно браузера."""
        self.driver.get(url)
        self.driver.maximize_window()

    def element_is_visible(self, locator, timeout=30):
        """Method Find a visible element"""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_present(self, locator, timeout=30):
        """Method Find present element"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=30):
        """Method Find clickable elements"""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def action_move_to_element(self, element):
        """Method Move cursor to element"""
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def action_click_and_hold(self, element, offset_x, offset_y):
        """Method Move click_and_hold"""
        action = ActionChains(self.driver)
        action.click_and_hold(element).move_by_offset(offset_x, offset_y).release().perform()

    def action_scroll_to_element(self, element, offset_x, offset_y):
        """Method Move scroll_to_element"""
        action = ActionChains(self.driver)
        action.scroll_to_element(element).move_by_offset(offset_x, offset_y).release().perform()

    def get_current_url(self):
        """Method get current url"""
        get_url = self.driver.current_url
        print("Current url " + get_url)

    def assert_word(self, word, result):
        """Method assert word"""
        value_word = word.text
        assert value_word == result
        print("Good value word")

    def get_screenshot(self, ):
        """Method Screenshot finish"""
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")  # Дата и время в настоящий момент
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot('.\\screen\\' + name_screenshot)  # Делаем Скриншот в папку
        print('Screen good')

    def assert_url(self, result):
        """Method assert url"""
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    def assert_text_on_page(self, expected_text):
        """Метод Проверяет, содержится ли ожидаемый текст на текущей странице"""
        try:
            element = self.element_is_visible((By.XPATH, f"//*[contains(text(), '{expected_text}')]")) #Текст, который ожидается увидеть на странице
            actual_text = element.text
            assert expected_text in actual_text, f"Текст '{expected_text}' не найден на странице"
            print(f"Текст '{expected_text}' найден на странице")
        except NoSuchElementException:
            print(f"Элемент с текстом '{expected_text}' не найден на странице")

    def click_element(self, xpath):
        """Кликнуть по элементу"""
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()
        print(f"Clicked element with XPath '{xpath}'.")

    def input_text(self, xpath, text):
        """Ввести текст в поле ввода"""
        element = self.driver.find_element(By.XPATH, xpath)
        element.clear()
        element.send_keys(text)
        print(f"Entered text '{text}' into element with XPath '{xpath}'.")

    def clear_element(self, xpath):
        """Очистить текст из элемента"""
        element = self.driver.find_element(By.XPATH, xpath)
        element.clear()
        print(f"Cleared text from element with XPath '{xpath}'.")

    def press_enter_key(self, xpath):
        """Нажать клавишу "Enter" на элементе"""
        element = self.driver.find_element(By.XPATH, xpath)
        element.send_keys(Keys.ENTER)
        print(f"Pressed 'Enter' key on element with XPath '{xpath}'.")

    def refresh_page(self):
        """Обновить текущую страницу."""
        self.driver.refresh()
        print("Refresh_page")