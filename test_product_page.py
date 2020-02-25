import pytest

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
                                  "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.maximize()
    page.open()
    page.should_be_promo_in_url()
    page.should_be_add_to_cart_button()
    page.click_add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.should_be_names_are_like()
    page.should_be_prices_are_equal()

@pytest.mark.xfail
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.maximize()
    page.open()
    page.should_be_promo_in_url()
    page.should_be_add_to_cart_button()
    page.click_add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.message_is_not_present()
    time.sleep(1000)

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.maximize()
    page.open()
    page.message_is_not_present()

@pytest.mark.xfail
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.maximize()
    page.open()
    page.should_be_promo_in_url()
    page.should_be_add_to_cart_button()
    page.click_add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.message_is_dissapeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.go_to_basket_page()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_empty_basket()

@pytest.mark.product
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = login_page.generate_email()
        password = login_page.generate_password()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_button()
        page.go_to_basket_page()
        basket = BasketPage(browser, browser.current_url)
        basket.should_be_empty_basket()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_cart_button()
        page.click_add_to_cart_button()
        page.should_be_names_are_like()
        page.should_be_prices_are_equal()