import pytest

from config.settings import Settings


@pytest.fixture
def navigate_base_url(page):
    page.set_default_timeout(Settings.DEFAULT_TIMEOUT)
    page.goto(Settings.BASE_URL, wait_until="domcontentloaded")
    return page