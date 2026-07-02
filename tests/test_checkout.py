import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutInformationPage, CheckoutOverviewPage
from pages.confirmation_page import CheckoutCompletePage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


PRODUCT_NAME = "Sauce Labs Backpack"
CHECKOUT_FIRST_NAME = "Tuhin"
CHECKOUT_LAST_NAME = "SQA"
CHECKOUT_POSTAL_CODE = "10001"
CHECKOUT_TOTAL = "Total: $32.39"


@pytest.mark.checkout
def test_checkout_and_order_confirmation(app_page):
    login_page = LoginPage(app_page)
    login_page.sign_in_standard()

    inventory_page = InventoryPage(app_page)
    inventory_page.add_and_open_cart(PRODUCT_NAME)

    cart_page = CartPage(app_page)
    cart_page.is_open()
    cart_page.has_item(PRODUCT_NAME)
    cart_page.checkout()

    checkout_info_page = CheckoutInformationPage(app_page)
    checkout_info_page.is_open()
    checkout_info_page.fill_details(
        CHECKOUT_FIRST_NAME, CHECKOUT_LAST_NAME, CHECKOUT_POSTAL_CODE
    )
    checkout_info_page.next()

    checkout_overview_page = CheckoutOverviewPage(app_page)
    checkout_overview_page.is_open()
    checkout_overview_page.has_item(PRODUCT_NAME)
    checkout_overview_page.total_is(CHECKOUT_TOTAL)
    checkout_overview_page.finish()

    complete_page = CheckoutCompletePage(app_page)
    complete_page.order_done()