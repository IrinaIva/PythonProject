import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .pages.main_page import MainPage
from .pages.product_page import ProductPage


promo = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

@pytest.mark.parametrize('promo', promo)
def test_guest_can_add_product_to_basket(browser, promo):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + promo
    product_page = ProductPage(browser, link)
    product_page.open()
    product_title = product_page.get_item_title()
    product_price = product_page.get_item_price()
    product_page.add_item_to_the_basket()
    product_page.solve_quiz_and_get_code()
    product_page.assert_item_added_to_the_basket_message(product_title)
    product_page.assert_item_price_added_to_the_basket_message(product_price)
    product_page.assert_open_item(product_title, product_price)








