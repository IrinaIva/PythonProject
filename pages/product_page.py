from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ItemPageLocators


class ProductPage(BasePage):
    def add_item_to_the_basket(self):
        add_item_button = self.browser.find_element(*ItemPageLocators.ADD_ITEM_BUTTON)
        add_item_button.click()






