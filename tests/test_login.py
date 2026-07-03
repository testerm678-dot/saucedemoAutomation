import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.login
def test_login_with_standard_user(navigate_base_url):
    login_page = LoginPage(navigate_base_url)
    login_page.sign_in_standard()

    inventory_page = InventoryPage(navigate_base_url)
    inventory_page.is_open()


@pytest.mark.login
def test_login_with_locked_out_user_shows_error(navigate_base_url):
    login_page = LoginPage(navigate_base_url)
    login_page.sign_in_locked()

    login_page.has_error("Epic sadface: Sorry, this user has been locked out.")


@pytest.mark.login
def test_login_with_invalid_password_shows_error(navigate_base_url):
    login_page = LoginPage(navigate_base_url)
    login_page.sign_in_bad_password()

    login_page.has_error(
        "Epic sadface: Username and password do not match any user in this service"
    )