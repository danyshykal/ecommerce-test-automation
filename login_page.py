from pages.base_page import BasePage


class LoginPage(BasePage):
    def open(self):
        self.page.goto("/")

    def login(self, username: str, password: str):
        self.by_test("username").fill(username)
        self.by_test("password").fill(password)
        self.by_test("login-button").click()

    @property
    def error_message(self):
        return self.by_test("error")
