from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_BTN)
        add_btn.click()

    def should_be_added_to_cart_message(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        latest_add_message = self.browser.find_element(*ProductPageLocators.LATEST_ADD_MESSAGE).text
        assert book_name == latest_add_message, f"{book_name} not equal {latest_add_message}"

    def should_modify_price_of_cart_message(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        assert cart_price == book_price, f"{cart_price} not equal {book_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
