from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from .locators import ItemPageLocators


class ProductPage(BasePage):
    def add_item_to_the_basket(self):
        add_item_button = self.browser.find_element(*ItemPageLocators.ADD_ITEM_BUTTON)
        add_item_button.click()

    def get_item_title(self):
        return self.browser.find_element(*ItemPageLocators.PRODUCT_TITLE).text

    def get_item_price(self):
        return self.browser.find_element(*ItemPageLocators.PRODUCT_PRICE).text

    def assert_item_added_to_the_basket_message(self, title):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ItemPageLocators.PRODUCT_ADDED_MESSAGE))
        product_name = self.browser.find_element(*ItemPageLocators.PRODUCT_ADDED_MESSAGE).text
        assert title == product_name, f"Wrong product was added, expected: {title}, but was: {product_name}"

    def assert_item_price_added_to_the_basket_message(self, price):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ItemPageLocators.BASKET_TOTAL))
        product_price = self.browser.find_element(*ItemPageLocators.BASKET_TOTAL).text
        assert price == product_price, f"Wrong product price of the added product, expected: {price}, but was: {product_price} "

    def assert_open_item(self, title, price):
        product_title = self.browser.find_element(*ItemPageLocators.PRODUCT_TITLE).text
        product_price = self.browser.find_element(*ItemPageLocators.PRODUCT_PRICE).text
        assert price == product_price, f"Wrong product price after adding, expected: {price}, but was: {product_price}"
        assert title == product_title, f"Wrong product title after adding, expected: {title}, but was: {product_title}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ItemPageLocators.PRODUCT_ADDED_MESSAGE), \
       "Success message is presented, but should not be"

    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*ItemPageLocators.PRODUCT_ADDED_MESSAGE), \
       "Success message is presented, but should not be"
