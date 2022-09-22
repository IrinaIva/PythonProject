from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")



class LoginPageLocators:
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#register_form #id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#register_form #id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#register_form #id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")





class ItemPageLocators:
    ADD_ITEM_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_TITLE = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p")
    PRODUCT_ADDED_MESSAGE = (By.XPATH, "//div[@id='messages']//div[1]//strong")
    BASKET_TOTAL = (By.XPATH, "//div[@id='messages']//div[3]//strong")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//div[@id='content_inner']//p")
    BASKET_ITEMS = (By.XPATH, "//div[@class='basket-items']")
