import math

from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def should_be_promo_in_url(self):
        assert "?promo=newYear" in self.browser.current_url

    def should_be_price_product(self):
        self.is_element_present(*ProductPageLocators.PRICE_PRODUCT)

    def get_name_product(self):
        name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        return name

    def get_alert_name_product(self):
        name = self.browser.find_elements(*ProductPageLocators.ALERT_NAME_PRODUCT)[0]
        return name.text

    def should_be_names_are_like(self):
        alert_name_product = self.get_alert_name_product()
        name_product = self.get_name_product()
        assert name_product == alert_name_product

    def get_price_product(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        return price

    def get_alert_price_product(self):
        price = self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text
        return price

    def should_be_prices_are_equal(self):
        block_price = self.get_price_product()
        alert_price = self.get_alert_price_product()
        assert block_price == alert_price

    def should_be_add_to_cart_button(self):
        self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON)

    def click_add_to_cart_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except (NoAlertPresentException):
            print("No second alert presented")