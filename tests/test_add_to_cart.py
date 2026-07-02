import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.cart
def test_add_item_to_cart(app_page):
    login_page = LoginPage(app_page)
    login_page.sign_in_standard()

    inventory_page = InventoryPage(app_page)
    inventory_page.add_and_open_cart()

    cart_page = CartPage(app_page)
    cart_page.is_open()
    cart_page.has_item("Sauce Labs Backpack")