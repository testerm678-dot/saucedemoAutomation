from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    COMPLETE_HEADER = ".complete-header"
    COMPLETE_TEXT = ".complete-text"

    def order_done(self):
        self.expect_text(self.COMPLETE_HEADER, "Thank you for your order!")
        self.expect_contains_text(self.COMPLETE_TEXT, "Your order has been dispatched")