import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


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


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_item_to_the_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_item_to_the_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    BasketPage.should_not_be_basket_items(page)
    BasketPage.should_be_empty_basket_message(page)
