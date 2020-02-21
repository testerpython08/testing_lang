from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def basket_is_present(self):
        assert self.is_element_present(*BasketPageLocators.CONTAINER_BASKET)

    def should_be_empty_basket(self):
        assert len(self.browser.find_elements(*BasketPageLocators.ITEMS_INTO_BASKET)) == 0

    def text_about_empty_basket_is_exists(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT)