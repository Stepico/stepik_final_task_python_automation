from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_have_items_by_default(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS), \
            "The basket is not empty"

    def should_have_empty_cart_message_by_default(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "The basket does not show message that it is empty"
