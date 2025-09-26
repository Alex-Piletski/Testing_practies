import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()   # Selenium Manager сам подхватит драйвер
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("student", "Password123")   # рабочие тестовые креды
    assert "Logged In Successfully" in driver.page_source
