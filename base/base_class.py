import datetime
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method Find a visible element"""
    def element_is_visible(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    """Method Find present element"""
    def element_is_present(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    """Method Find clickable elements"""
    def element_is_clickable(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    """Method Move cursor to element"""
    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    """Method Move click_and_hold"""
    def action_click_and_hold(self, element, offset_x, offset_y):
        action = ActionChains(self.driver)
        action.click_and_hold(element).move_by_offset(offset_x, offset_y).release().perform()

    """Method Move scroll_to_element"""
    def action_scroll_to_element(self, element, offset_x, offset_y):
        action = ActionChains(self.driver)
        action.scroll_to_element(element).move_by_offset(offset_x, offset_y).release().perform()

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method Screenshot finish"""

    def get_screenshot(self, ):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")  # Дата и время в настоящий момент
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot('.\\screen\\' + name_screenshot)  # Делаем Скриншот в папку
        print('Screen good')


    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Метод Проверяет, содержится ли ожидаемый текст на текущей странице"""
    def assert_text_on_page(self, expected_text):
        try:
            element = self.driver.find_element(By.XPATH, f"//*[contains(text(), '{expected_text}')]") #Текст, который ожидается увидеть на странице
            actual_text = element.text
            assert expected_text in actual_text, f"Текст '{expected_text}' не найден на странице"
            print(f"Текст '{expected_text}' найден на странице")
        except NoSuchElementException:
            print(f"Элемент с текстом '{expected_text}' не найден на странице")

    """Кликнуть по элементу"""
    def click_element(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()
        print(f"Clicked element with XPath '{xpath}'.")

    """Ввести текст в поле ввода"""
    def input_text(self, xpath, text):
        element = self.driver.find_element(By.XPATH, xpath)
        element.clear()
        element.send_keys(text)
        print(f"Entered text '{text}' into element with XPath '{xpath}'.")

    """Очистить текст из элемента"""
    def clear_element(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        element.clear()
        print(f"Cleared text from element with XPath '{xpath}'.")

    """Нажать клавишу "Enter" на элементе"""
    def press_enter_key(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        element.send_keys(Keys.ENTER)
        print(f"Pressed 'Enter' key on element with XPath '{xpath}'.")