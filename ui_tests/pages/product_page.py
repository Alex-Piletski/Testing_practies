from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/inventory.html"
        # Кнопка добавления первого товара (Sauce Labs Backpack)
        self.add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        # Иконка корзины справа вверху
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def open(self):
        self.driver.get(self.url)

    def add_product_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        ).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
