"""Selenium products page object."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.selenium.base_page import BasePage
import time


class ProductsPage(BasePage):
    """Products page interactions using Selenium."""
    
    # Locators
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCT_SORT = (By.CLASS_NAME, "product_sort_container")
    
    def is_loaded(self) -> bool:
        """Check if products page is loaded."""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.PRODUCTS_TITLE)
            )
            return True
        except:
            return False
        
    def get_product_count(self) -> int:
        """Get number of products displayed."""
        return len(self.find_elements(*self.INVENTORY_ITEMS))
        
    def add_item_to_cart(self, product_id: str):
        """Add specific product to cart by ID."""
        button_locator = (By.ID, f"add-to-cart-{product_id}")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        ).click()
        time.sleep(1)
        
    def remove_item_from_cart(self, product_id: str):
        """Remove specific product from cart."""
        button_locator = (By.ID, f"remove-{product_id}")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        ).click()
        time.sleep(1)
        
    def get_cart_count(self) -> int:
        """Get number of items in cart."""
        try:
            badge_element = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(self.CART_BADGE)
            )
            return int(badge_element.text)
        except:
            return 0
        
    def go_to_cart(self):
        """Navigate to cart page."""
        self.click(*self.CART_LINK)
        time.sleep(4)
