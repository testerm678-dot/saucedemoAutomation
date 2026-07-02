from pages.base_page import BasePage


class CartPage(BasePage):
    PAGE_TITLE = ".title"
    CHECKOUT_BUTTON = '[data-test="checkout"]'

    def is_open(self):
        self.expect_text(self.PAGE_TITLE, "Your Cart")

    def has_item(self, item_name):
        self.expect_page_text_visible(item_name)

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)