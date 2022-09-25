from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email: str, password: str):
        #enter_text = BasePage.enter_text
        self.enter_text(*LoginPageLocators.REGISTER_EMAIL, email)
        self.enter_text(*LoginPageLocators.REGISTER_PASSWORD, password)
        self.enter_text(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD, password)
        self.click(*LoginPageLocators.REGISTER_BUTTON)

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This is not login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
