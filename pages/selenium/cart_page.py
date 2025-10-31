"""Selenium cart page object."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.selenium.base_page import BasePage
import time


class CartPage(BasePage):
    """Shopping cart page interactions using Selenium."""
    
    # Locators
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CART_LIST = (By.CLASS_NAME, "cart_list")
    
    def wait_for_cart_to_load(self):
        """Wait for cart page to fully load."""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CART_LIST)
        )
    
    def get_cart_item_count(self) -> int:
        """Get number of items in cart."""
        self.wait_for_cart_to_load()
        try:
            # Wait a moment for items to be present if they exist
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(self.CART_ITEMS)
            )
        except:
            # No items in cart is valid
            pass
        return len(self.find_elements(*self.CART_ITEMS))
        
    def proceed_to_checkout(self):
        """Click checkout button."""
        self.wait_for_cart_to_load()
        self.click(*self.CHECKOUT_BUTTON)
        
    def continue_shopping(self):
        """Return to products page."""
        self.wait_for_cart_to_load()
        self.click(*self.CONTINUE_SHOPPING)
        # Wait for products page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        
    def remove_item(self, product_id: str):
        """Remove item from cart."""
        self.wait_for_cart_to_load()
        button_locator = (By.ID, f"remove-{product_id}")
        
        # Wait for the remove button to be clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        )
        
        # Click the button
        self.click(*button_locator)
        
        # Wait for item to be removed from DOM
        time.sleep(1)
