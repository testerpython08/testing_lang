from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .locators import MainPageLocators

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def maximize(self):
        self.browser.maximize_window()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # упадет, как только искомый элемент появится
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # будет ждать, пока элемент не исчезнет
    def is_dissappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        basket = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        basket.click()

    def should_be_basket_button(self):
        assert self.is_element_present(*MainPageLocators.BASKET_BUTTON)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon isn\'t presented, " \
                                                                     "probably unauthorized user"