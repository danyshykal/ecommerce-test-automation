from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def fill_info(self, first: str, last: str, postcode: str):
        self.by_test("firstName").fill(first)
        self.by_test("lastName").fill(last)
        self.by_test("postalCode").fill(postcode)
        self.by_test("continue").click()

    def finish(self):
        self.by_test("finish").click()

    @property
    def error_message(self):
        return self.by_test("error")

    @property
    def subtotal_label(self):
        return self.page.locator(".summary_subtotal_label")

    @property
    def complete_header(self):
        return self.page.locator(".complete-header")
