import pytest
from selenium import webdriver
from ui_tests.pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    # Проверяем, что после логина попали на страницу товаров
    assert "inventory.html" in driver.current_url
    assert "Sauce Labs Backpack" in driver.page_source

