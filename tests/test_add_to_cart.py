import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.cart
def test_add_item_to_cart(navigate_base_url):
    login_page = LoginPage(navigate_base_url)
    login_page.sign_in_standard()

    inventory_page = InventoryPage(navigate_base_url)
    inventory_page.add_and_open_cart()

    cart_page = CartPage(navigate_base_url)
    cart_page.is_open()
    cart_page.has_item("Sauce Labs Backpack")
    assert navigate_base_url.get_by_text("Sauce Labs Backpack").is_visible(), "Sauce Labs Backpack should be visible in the cart"