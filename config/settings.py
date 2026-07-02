import os

class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")

    STANDARD_USER = os.getenv("STANDARD_USER", "standard_user")
    LOCKED_OUT_USER = os.getenv("LOCKED_OUT_USER", "locked_out_user")
    PASSWORD = os.getenv("PASSWORD", "secret_sauce")

    DEFAULT_TIMEOUT = 30000
