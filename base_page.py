from playwright.sync_api import Page


class BasePage:
    """Shared helpers for every page object."""

    def __init__(self, page: Page):
        self.page = page

    def by_test(self, name: str):
        # saucedemo uses data-test="..." attributes on elements
        return self.page.locator(f'[data-test="{name}"]')
