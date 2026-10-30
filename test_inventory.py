from playwright.sync_api import expect


def test_TC_INV_01_products_displayed(logged_in):
    expect(logged_in.items).to_have_count(6)


def test_TC_INV_02_sort_price_low_to_high(logged_in):
    logged_in.sort_by("lohi")
    prices = logged_in.item_prices()
    assert prices == sorted(prices)


def test_TC_INV_03_sort_name_z_to_a(logged_in):
    logged_in.sort_by("za")
    names = logged_in.item_names()
    assert names == sorted(names, reverse=True)
