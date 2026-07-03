import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutInformationPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


CHECKOUT_LAST_NAME = "SQA"
CHECKOUT_POSTAL_CODE = "10001"
MISSING_POSTAL_CODE_ERROR = "Error: Postal Code is required"
MISSING_FIRST_NAME_ERROR = "Error: First Name is required"


@pytest.mark.checkout_validation
def test_checkout_from_cart_missing_first_name_shows_error(navigate_base_url):
    login_page = LoginPage(navigate_base_url)
    login_page.sign_in_standard()

    inventory_page = InventoryPage(navigate_base_url)
    inventory_page.add_and_open_cart()

    cart_page = CartPage(navigate_base_url)
    cart_page.is_open()
    cart_page.checkout()

    checkout_info_page = CheckoutInformationPage(navigate_base_url)
    checkout_info_page.is_open()
    checkout_info_page.fill_details("", CHECKOUT_LAST_NAME, CHECKOUT_POSTAL_CODE)
    checkout_info_page.next()
    checkout_info_page.has_error(MISSING_FIRST_NAME_ERROR)


@pytest.mark.checkout_validation
def test_checkout_from_cart_missing_postal_code_shows_error(navigate_base_url):
    login_page = LoginPage(navigate_base_url)
    login_page.sign_in_standard()

    inventory_page = InventoryPage(navigate_base_url)
    inventory_page.add_and_open_cart()

    cart_page = CartPage(navigate_base_url)
    cart_page.is_open()
    cart_page.checkout()

    checkout_info_page = CheckoutInformationPage(navigate_base_url)
    checkout_info_page.is_open()
    checkout_info_page.fill_details("Tuhin", CHECKOUT_LAST_NAME, "")
    checkout_info_page.next()
    checkout_info_page.has_error(MISSING_POSTAL_CODE_ERROR)