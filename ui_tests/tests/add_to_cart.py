import pytest
from selenium import webdriver
from ui_tests.pages.login_page import LoginPage
from ui_tests.pages.product_page import ProductPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_and_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Переход на страницу товаров
    product_page = ProductPage(driver)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.go_to_cart()
    # Проверка, что товар Sauce Labs Backpack есть в корзине
    assert "Sauce Labs Backpack" in driver.page_source
