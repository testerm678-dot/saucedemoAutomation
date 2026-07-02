from pages.base_page import BasePage


class InventoryPage(BasePage):
    PAGE_TITLE = ".title"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    INVENTORY_ITEM = ".inventory_item"

    def is_open(self):
        self.expect_text(self.PAGE_TITLE, "Products")

    def has_product(self, product_name):
        self.expect_page_text_visible(product_name)

    def add_item(self, product_name):
        self.page.locator(self.INVENTORY_ITEM).filter(has_text=product_name).get_by_role(
            "button"
        ).click()

    def cart_count(self, count):
        self.expect_text(self.CART_BADGE, str(count))

    def open_cart(self):
        self.click(self.CART_LINK)

    def add_and_open_cart(self, product_name="Sauce Labs Backpack"):
        self.is_open()
        self.has_product(product_name)
        self.add_item(product_name)
        self.cart_count(1)
        self.open_cart()