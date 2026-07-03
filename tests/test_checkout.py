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
def test_checkout_and_order_confirmation(navigate_base_url):
    login_page = LoginPage(navigate_base_url)
    login_page.sign_in_standard()

    inventory_page = InventoryPage(navigate_base_url)
    inventory_page.add_and_open_cart(PRODUCT_NAME)

    cart_page = CartPage(navigate_base_url)
    cart_page.is_open()
    cart_page.has_item(PRODUCT_NAME)
    cart_page.checkout()

    checkout_info_page = CheckoutInformationPage(navigate_base_url)
    checkout_info_page.is_open()
    checkout_info_page.fill_details(
        CHECKOUT_FIRST_NAME, CHECKOUT_LAST_NAME, CHECKOUT_POSTAL_CODE
    )
    checkout_info_page.next()

    checkout_overview_page = CheckoutOverviewPage(navigate_base_url)
    checkout_overview_page.is_open()
    checkout_overview_page.has_item(PRODUCT_NAME)
    checkout_overview_page.total_is(CHECKOUT_TOTAL)
    checkout_overview_page.finish()

    complete_page = CheckoutCompletePage(navigate_base_url)
    complete_page.order_done()
    assert complete_page.page.locator(complete_page.COMPLETE_HEADER).text_content() == "Thank you for your order!", "The order completion message should be displayed"