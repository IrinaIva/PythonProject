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
        assert title == product_name, "Wrong product was added"

    def assert_item_price_added_to_the_basket_message(self, price):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ItemPageLocators.BASKET_TOTAL))
        product_price = self.browser.find_element(*ItemPageLocators.BASKET_TOTAL).text
        assert price == product_price, "Wrong product was added"

