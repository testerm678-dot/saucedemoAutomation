from pages.base_page import BasePage


class CheckoutInformationPage(BasePage):
    PAGE_TITLE = ".title"
    FIRST_NAME_INPUT = '[data-test="firstName"]'
    LAST_NAME_INPUT = '[data-test="lastName"]'
    POSTAL_CODE_INPUT = '[data-test="postalCode"]'
    CONTINUE_BUTTON = '[data-test="continue"]'
    ERROR_BANNER = '[data-test="error"]'

    def is_open(self):
        self.expect_text(self.PAGE_TITLE, "Checkout: Your Information")

    def fill_details(self, first_name, last_name, postal_code):
        self.fill(self.FIRST_NAME_INPUT, first_name)
        self.fill(self.LAST_NAME_INPUT, last_name)
        self.fill(self.POSTAL_CODE_INPUT, postal_code)

    def next(self):
        self.click(self.CONTINUE_BUTTON)

    def has_error(self, message):
        self.expect_visible(self.ERROR_BANNER)
        self.expect_text(self.ERROR_BANNER, message)


class CheckoutOverviewPage(BasePage):
    PAGE_TITLE = ".title"
    SUMMARY_TOTAL_LABEL = ".summary_total_label"
    FINISH_BUTTON = '[data-test="finish"]'

    def is_open(self):
        self.expect_text(self.PAGE_TITLE, "Checkout: Overview")

    def has_item(self, item_name):
        self.expect_page_text_visible(item_name)

    def total_is(self, expected_total):
        self.expect_text(self.SUMMARY_TOTAL_LABEL, expected_total)

    def finish(self):
        self.click(self.FINISH_BUTTON)