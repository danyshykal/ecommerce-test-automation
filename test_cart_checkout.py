import pytest
from playwright.sync_api import expect


def test_TC_CART_01_add_item_updates_badge(logged_in):
    logged_in.add_to_cart("sauce-labs-backpack")
    expect(logged_in.cart_badge).to_have_text("1")


def test_TC_CART_02_remove_item_clears_badge(logged_in):
    logged_in.add_to_cart("sauce-labs-backpack")
    logged_in.remove_from_cart("sauce-labs-backpack")
    expect(logged_in.cart_badge).to_have_count(0)


def test_TC_CART_03_cart_shows_added_items(logged_in, cart_page):
    logged_in.add_to_cart("sauce-labs-backpack")
    logged_in.add_to_cart("sauce-labs-bike-light")
    logged_in.go_to_cart()
    expect(cart_page.cart_items).to_have_count(2)


@pytest.mark.smoke
def test_TC_CHK_01_full_checkout(logged_in, cart_page, checkout_page):
    logged_in.add_to_cart("sauce-labs-backpack")      # $29.99
    logged_in.add_to_cart("sauce-labs-bike-light")    # $9.99
    logged_in.go_to_cart()
    cart_page.checkout()
    checkout_page.fill_info("Danysh", "Test", "81700")
    expect(checkout_page.subtotal_label).to_contain_text("39.98")
    checkout_page.finish()
    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")


@pytest.mark.negative
@pytest.mark.parametrize(
    "first, last, postcode, expected_error",
    [
        ("", "Test", "81700", "First Name is required"),
        ("Danysh", "", "81700", "Last Name is required"),
        ("Danysh", "Test", "", "Postal Code is required"),
    ],
    ids=["TC_CHK_02_no_first_name", "TC_CHK_03_no_last_name", "TC_CHK_04_no_postcode"],
)
def test_checkout_validation(logged_in, cart_page, checkout_page, first, last, postcode, expected_error):
    logged_in.add_to_cart("sauce-labs-backpack")
    logged_in.go_to_cart()
    cart_page.checkout()
    checkout_page.fill_info(first, last, postcode)
    expect(checkout_page.error_message).to_contain_text(expected_error)
