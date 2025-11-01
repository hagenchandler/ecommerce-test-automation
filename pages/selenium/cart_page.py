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
    CART_CONTENTS = (By.ID, "cart_contents_container")
    
    def get_cart_item_count(self) -> int:
        """Get number of items in cart."""
        # Wait longer for cart page and items to be fully loaded
        time.sleep(2)
        
        # Try to find cart items
        items = self.find_elements(*self.CART_ITEMS)
        return len(items)
        
    def proceed_to_checkout(self):
        """Click checkout button."""
        checkout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_btn.click()
        
    def continue_shopping(self):
        """Return to products page."""
        # Wait longer for page to be ready
        time.sleep(1)
        
        try:
            # Try to find and click the continue shopping button
            continue_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CONTINUE_SHOPPING)
            )
            continue_btn.click()
        except:
            # If not found, try alternative: just navigate back
            self.driver.back()
        
        # Wait for navigation
        time.sleep(2)
        
    def remove_item(self, product_id: str):
        """Remove item from cart."""
        # Wait a moment for page to be ready
        time.sleep(1)
        
        button_locator = (By.ID, f"remove-{product_id}")
        
        # Wait for the remove button to be clickable
        remove_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        )
        
        # Click the button
        remove_btn.click()
        
        # Wait for item to be removed from DOM
        time.sleep(2)
