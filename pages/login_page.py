from .base_page import BasePage
from .locators import LoginPageLocators
from faker import Faker


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login is absent in the url"

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form.is_displayed(), "login form is absent on the Login Page"

    def should_be_register_form(self):
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert register_form.is_displayed(), "registration form is absent on the Login Page"

    def register_new_user(self):
        faker = Faker('en_US')
        password = 'Qwerty12345!'

        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(faker.email())
        pass_field = self.browser.find_element(*LoginPageLocators.PASS_FIELD)
        pass_field.send_keys(password)
        confirm_pass_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASS_FIELD)
        confirm_pass_field.send_keys(pass_field)
        submit_registration_btn = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTRATION_BTN)
        submit_registration_btn.click()
