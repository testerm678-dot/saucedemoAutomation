from pathlib import Path
import sys

import pytest


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config.settings import Settings


@pytest.fixture
def app_page(page):
    page.set_default_timeout(Settings.DEFAULT_TIMEOUT)
    page.set_viewport_size({"width": 1440, "height": 1080})
    page.goto(Settings.BASE_URL, wait_until="domcontentloaded")
    return page