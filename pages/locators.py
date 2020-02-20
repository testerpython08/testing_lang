from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "article.product_page .product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "article.product_page .product_main > .price_color")
    ALERT_NAME_PRODUCT = (By.CSS_SELECTOR, "#messages .alert-success strong")
    ALERT_PRICE = (By.CSS_SELECTOR, "#messages .alert-info strong")
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, "#messages .alert-success")