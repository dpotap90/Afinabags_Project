import allure
from pages.catalog_page import Catalog_page
from pages.main_page import Main_page
from pages.payment_page import Order_cart_page
from pages.product_692_page import Product_692_page

@allure.description("Test buy product")
def test_buy_product(set_up, screenshot_allure, driver):

    print("Start Test 1")

    """Catalog open"""
    mp = Main_page(driver)
    mp.select_catalogs()

    """Select product catalog"""
    cp = Catalog_page(driver)
    cp.select_products_692()

    """Checkout products"""
    pr_692 = Product_692_page(driver)
    pr_692.cart_and_checkout_products_692()

    """Order cart"""
    p = Order_cart_page(driver)
    p.order_cart()


    print("Finish test 1")

