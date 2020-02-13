def test_language(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    button_shop = browser.find_element_by_css_selector(".btn-group a.btn-default")
    assert len(button_shop.text)