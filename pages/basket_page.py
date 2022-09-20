from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from .locators import ItemPageLocators, BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
       "Tere are items in the basket, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
       "Tere is no Empty basket message, but should be"
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        empty_message = "Your basket is empty"
        assert empty_message in message, f"Wrong product was added, expected: {empty_message}, but was: {message}"
