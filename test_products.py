from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.maximize()
    page.open()
    page.should_be_promo_in_url()
    page.should_be_add_to_cart_button()
    page.click_add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.should_be_names_are_like()
    page.should_be_prices_are_equal()

def test_guest_can_add_product_to_basket_2019(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.maximize()
    page.open()
    page.should_be_promo_in_url()
    page.should_be_add_to_cart_button()
    page.click_add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.should_be_names_are_like()
    page.should_be_prices_are_equal()