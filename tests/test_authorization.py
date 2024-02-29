import allure
from pages.main_page import MainTest
@allure.description("Test authorization")
def test_authorization(set_up, screenshot_allure, driver):

    print("Start Test authorization")

    mp = MainTest(driver)
    mp.authorization()

    print("Finish Test authorization")