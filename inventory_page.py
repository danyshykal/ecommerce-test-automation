from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL_PART = "/inventory.html"

    @property
    def items(self):
        return self.page.locator(".inventory_item")

    @property
    def cart_badge(self):
        return self.page.locator(".shopping_cart_badge")

    def add_to_cart(self, product_slug: str):
        # e.g. "sauce-labs-backpack"
        self.by_test(f"add-to-cart-{product_slug}").click()

    def remove_from_cart(self, product_slug: str):
        self.by_test(f"remove-{product_slug}").click()

    def sort_by(self, option: str):
        # options: az, za, lohi, hilo
        self.by_test("product-sort-container").select_option(option)

    def item_names(self) -> list[str]:
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def item_prices(self) -> list[float]:
        texts = self.page.locator(".inventory_item_price").all_inner_texts()
        return [float(t.replace("$", "")) for t in texts]

    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()

    def logout(self):
        self.page.locator("#react-burger-menu-btn").click()
        self.page.locator("#logout_sidebar_link").click()
