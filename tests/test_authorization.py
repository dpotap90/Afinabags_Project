import allure
from pages.catalog_page import Catalog_page
from pages.main_page import Main_page
from pages.payment_page import Order_cart_page
from pages.product_692_page import Product_692_page
from base.base_class import Base

@allure.description("Test_authorization")
def test_authorization(set_up, screenshot_allure, driver):

    print("Start Test_authorization")

    mp = Main_page(driver)
    mp.authorization()

    print("Finish test 1")