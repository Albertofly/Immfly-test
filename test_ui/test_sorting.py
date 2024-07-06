import pytest

from pom.home_page_elements import HomePage
from playwright.sync_api import expect


def test_assert_sorting_options(go_to_homepage, allow_cookies) -> None:
    home_page = HomePage(go_to_homepage)
    home_page.sort_item.click()
    expect(home_page.product_name_asc).to_be_visible()
    expect(home_page.product_name_desc).to_be_visible()
    expect(home_page.product_price_asc).to_be_visible()
    expect(home_page.product_price_desc).to_be_visible()


def test_assert_default_position(go_to_homepage, allow_cookies) -> None:
    home_page = HomePage(go_to_homepage)
    home_page.sort_item.click()
    expect(home_page.first_item_default).to_be_visible()
    expect(home_page.fist_item_product_name).not_to_be_visible()


def test_assert_sorting_product_name_asc(go_to_homepage, allow_cookies,page) -> None:
    home_page = HomePage(go_to_homepage)
    home_page.sort_item.click()
    home_page.product_name_asc.click()
    page.pause()
    expect(home_page.fist_item_product_name).to_be_visible()
    expect(home_page.last_item_product_name).not_to_be_visible()


def test_assert_sorting_product_name_desc(go_to_homepage, allow_cookies) -> None:
    home_page = HomePage(go_to_homepage)
    home_page.sort_item.click()
    home_page.product_name_desc.click()
    expect(home_page.last_item_product_name).to_be_visible()
    expect(home_page.fist_item_product_name).not_to_be_visible()


def test_assert_sorting_product_price_asc(go_to_homepage, allow_cookies) -> None:
    home_page = HomePage(go_to_homepage)
    home_page.sort_item.click()
    home_page.product_price_asc.click()
    expect(home_page.first_item_price).to_be_visible()
    expect(home_page.fist_item_price_amount).to_be_visible()


def test_assert_sorting_product_price_desc(go_to_homepage, allow_cookies) -> None:
    home_page = HomePage(go_to_homepage)
    home_page.sort_item.click()
    home_page.product_price_desc.click()
    expect(home_page.last_item_price).to_be_visible()
    expect(home_page.last_item_price_amount).to_be_visible()
    expect(home_page.first_item_price).not_to_be_visible()
    expect(home_page.fist_item_price_amount).not_to_be_visible()
