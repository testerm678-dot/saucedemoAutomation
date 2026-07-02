from playwright.sync_api import expect


class BasePage:
    def __init__(self, page):
        self.page = page

    def fill(self, selector, value):
        self.page.locator(selector).fill(value)

    def click(self, selector):
        self.page.locator(selector).click()

    def expect_text(self, selector, text):
        expect(self.page.locator(selector)).to_have_text(text)

    def expect_contains_text(self, selector, text):
        expect(self.page.locator(selector)).to_contain_text(text)

    def expect_visible(self, selector):
        expect(self.page.locator(selector)).to_be_visible()

    def expect_page_text_visible(self, text):
        expect(self.page.get_by_text(text)).to_be_visible()
