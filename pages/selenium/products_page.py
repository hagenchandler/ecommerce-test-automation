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
        return self.is_visible(*self.PRODUCTS_TITLE)
        
    def get_product_count(self) -> int:
        """Get number of products displayed."""
        return len(self.find_elements(*self.INVENTORY_ITEMS))
        
    def add_item_to_cart(self, product_id: str):
        """Add specific product to cart by ID."""
        # Wait for the add button to be present and clickable
        button_locator = (By.ID, f"add-to-cart-{product_id}")
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        )
        
        # Click add to cart button
        add_button.click()
        
        # Wait for button to change to "remove" button
        remove_button_locator = (By.ID, f"remove-{product_id}")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(remove_button_locator),
            message=f"Remove button for {product_id} did not appear after adding to cart"
        )
        
    def remove_item_from_cart(self, product_id: str):
        """Remove specific product from cart."""
        # Wait for remove button to be clickable
        button_locator = (By.ID, f"remove-{product_id}")
        remove_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        )
        
        # Click remove button
        remove_button.click()
        
        # Wait for removal to complete
        time.sleep(1)
        
    def get_cart_count(self) -> int:
        """Get number of items in cart."""
        try:
            # Wait briefly for badge to be visible
            badge_element = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(self.CART_BADGE)
            )
            return int(badge_element.text)
        except:
            return 0
        
    def go_to_cart(self):
        """Navigate to cart page."""
        # Click cart link
        self.click(*self.CART_LINK)
        
        # Simple wait for navigation
        time.sleep(2)
