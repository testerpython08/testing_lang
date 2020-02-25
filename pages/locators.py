from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "article.product_page .product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "article.product_page .product_main > .price_color")
    ALERT_NAME_PRODUCT = (By.CSS_SELECTOR, "#messages .alert-success strong")
    ALERT_PRICE = (By.CSS_SELECTOR, "#messages .alert-info strong")
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, "#messages .alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    CONTAINER_BASKET = (By.CSS_SELECTOR, ".container-fluid")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, ".content")
    ITEMS_INTO_BASKET = (By.CSS_SELECTOR, ".basket-items")