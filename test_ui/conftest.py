
import pytest
from playwright.sync_api import Playwright, expect
from pom.home_page_elements import HomePage


@pytest.fixture()
def go_to_homepage(page):
    page.goto("https://highlifeshop.com/cafe")
    yield page
    page.close()


@pytest.fixture()
def allow_cookies(page):
    home_page = HomePage(page)
    expect(home_page.allow_all_cookies).to_be_visible()
    home_page.allow_all_cookies.click()
    yield page
    page.close()

