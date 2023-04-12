from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_CART_BTN = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_BTN = (By.CLASS_NAME, 'btn-add-to-basket')
    BOOK_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    BOOK_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    LATEST_ADD_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    CART_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div')


class BasketPageLocators:
    ITEMS = (By.CLASS_NAME, 'basket-title hidden-xs')
    EMPTY_MESSAGE = (By.XPATH, '//*[@id="content_inner"]/p/a')
