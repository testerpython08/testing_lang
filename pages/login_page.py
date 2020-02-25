import time
import random
from string import ascii_letters

from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not exists"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not exists"

    def generate_email(self):
        email = str(time.time()) + "@fakemail.org"
        return email

    def generate_password(self):
        password = "".join(random.sample(ascii_letters, 10))
        return password

    def register_new_user(self, email, password):
        self.should_be_register_form()
        email_register = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_register.send_keys(email)
        password_register = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_register.send_keys(password)
        password_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        password_confirm.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()