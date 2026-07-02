import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.login
def test_login_with_standard_user(app_page):
    login_page = LoginPage(app_page)
    login_page.sign_in_standard()

    inventory_page = InventoryPage(app_page)
    inventory_page.is_open()


@pytest.mark.login
def test_login_with_locked_out_user_shows_error(app_page):
    login_page = LoginPage(app_page)
    login_page.sign_in_locked()

    login_page.has_error("Epic sadface: Sorry, this user has been locked out.")


@pytest.mark.login
def test_login_with_invalid_password_shows_error(app_page):
    login_page = LoginPage(app_page)
    login_page.sign_in_bad_password()

    login_page.has_error(
        "Epic sadface: Username and password do not match any user in this service"
    )