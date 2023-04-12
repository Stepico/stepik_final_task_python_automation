from .pages.basket_page import BasketPage


def test_basket_do_not_have_items_by_default(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_have_items_by_default()


def test_basket_show_empty_message_by_default(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_have_empty_cart_message_by_default()
