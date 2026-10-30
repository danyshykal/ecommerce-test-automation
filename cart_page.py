from pages.base_page import BasePage


class CartPage(BasePage):
    @property
    def cart_items(self):
        return self.page.locator(".cart_item")

    def checkout(self):
        self.by_test("checkout").click()
