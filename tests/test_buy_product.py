import allure
from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from pages.payment_page import OrderCartPage
from pages.product_692_page import Product692Page
from base.base_class import Base

@allure.description("Test buy product")
def test_buy_product(set_up, screenshot_allure, driver):

    print("Start test_buy_product")

    """"Catalog open"""
    mp = MainPage(driver)
    mp.select_catalogs()

    """Select product catalog"""
    cp = CatalogPage(driver)
    cp.select_products_692()

    """Checkout products"""
    pr_692 = Product692Page(driver)
    pr_692.cart_and_checkout_products_692()

    """Order cart"""
    p = OrderCartPage(driver)
    p.order_cart_1()
    # p.order_cart_2()

    print("Finish test_buy_product")

