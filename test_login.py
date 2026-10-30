import pytest
from playwright.sync_api import expect
from tests.conftest import PASSWORD


@pytest.mark.smoke
def test_TC_LOGIN_01_valid_login(login_page, page):
    login_page.login("standard_user", PASSWORD)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


@pytest.mark.negative
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("standard_user", "wrong_pass", "Username and password do not match"),
        ("", PASSWORD, "Username is required"),
        ("standard_user", "", "Password is required"),
        ("locked_out_user", PASSWORD, "this user has been locked out"),
    ],
    ids=["TC_LOGIN_02_wrong_password", "TC_LOGIN_03_empty_username",
         "TC_LOGIN_04_empty_password", "TC_LOGIN_05_locked_user"],
)
def test_invalid_login(login_page, username, password, expected_error):
    login_page.login(username, password)
    expect(login_page.error_message).to_contain_text(expected_error)


def test_TC_LOGIN_06_logout(logged_in, page):
    logged_in.logout()
    expect(page).to_have_url("https://www.saucedemo.com/")
