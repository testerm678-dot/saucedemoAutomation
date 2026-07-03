import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.login
def test_login_with_standard_user(navigate_base_url):
    login_page = LoginPage(navigate_base_url)
    login_page.sign_in_standard()

    inventory_page = InventoryPage(navigate_base_url)
    inventory_page.is_open()
    assert "inventory" in inventory_page.page.url, "Standard login should redirect to the inventory page"


@pytest.mark.login
def test_login_with_locked_out_user_shows_error(navigate_base_url):
    login_page = LoginPage(navigate_base_url)
    login_page.sign_in_locked()

    error_text = login_page.page.locator(login_page.ERROR_BANNER).text_content()
    assert "Epic sadface" in error_text, "The login error title should be displayed"
    assert "Sorry, this user has been locked out." in error_text, "The locked out error message should be visible"


@pytest.mark.login
def test_login_with_invalid_password_shows_error(navigate_base_url):
    login_page = LoginPage(navigate_base_url)
    login_page.sign_in_bad_password()

    error_text = login_page.page.locator(login_page.ERROR_BANNER).text_content()
    assert "Epic sadface" in error_text, "The login error title should be displayed"
    assert "Username and password do not match any user in this service" in error_text, "The invalid password error message should be visible"
