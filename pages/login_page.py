from pages.base_page import BasePage
from config.settings import Settings


class LoginPage(BasePage):
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    PAGE_LOGO = ".login_logo"
    ERROR_BANNER = '[data-test="error"]'

    def sign_in(self, username, password):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def sign_in_standard(self):
        self.is_open()
        self.sign_in(Settings.STANDARD_USER, Settings.PASSWORD)

    def sign_in_locked(self):
        self.is_open()
        self.sign_in(Settings.LOCKED_OUT_USER, Settings.PASSWORD)

    def sign_in_bad_password(self):
        self.is_open()
        self.sign_in(Settings.STANDARD_USER, "wrong_password")

    def is_open(self):
        self.expect_text(self.PAGE_LOGO, "Swag Labs")
        self.expect_visible(self.LOGIN_BUTTON)

    def has_error(self, message):
        self.expect_visible(self.ERROR_BANNER)
        self.expect_text(self.ERROR_BANNER, message)