import allure
from pages.main_page import MainPage

@allure.description("Test authorization")
def test_authorization(set_up, screenshot_allure, driver):

    print("Start Test authorization")

    mp = MainPage(driver)
    mp.authorization()

    print("Finish Test authorization")