import allure
from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from pages.order_cart_page import (OrderTest)
from pages.payment_page import OrderCartPage
from pages.product_692_page import Product692Page
from pages.main_page import MainTest

@allure.description("Test buy product")
def test_buy_product(set_up, screenshot_allure, driver):

    print("Start test_buy_product")

    """"Catalog open"""
    # mp = MainPage(driver)
    # mp.select_catalogs()

    mp = MainTest(driver)
    mp.select_catalogs()

    """Select product catalog"""
    cp = CatalogPage(driver)
    cp.select_products_692()

    """Checkout products"""
    pr_692 = Product692Page(driver)
    pr_692.cart_and_checkout_products_692()

    """Order cart"""

    o = OrderTest(driver)
    o.order_cart_1()  # тест файла 1
    # o.order_cart_2()  # тест файла 2

    print("Finish test_buy_product")

