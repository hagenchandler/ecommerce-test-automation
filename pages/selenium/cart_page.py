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
        # Wait for cart page to be loaded
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.CART_CONTENTS)
            )
        except:
            pass
        
        # Give a moment for items to render
        time.sleep(0.5)
        
        return len(self.find_elements(*self.CART_ITEMS))
        
    def proceed_to_checkout(self):
        """Click checkout button."""
        checkout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_btn.click()
        
    def continue_shopping(self):
        """Return to products page."""
        continue_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_SHOPPING)
        )
        continue_btn.click()
        
        # Wait for navigation
        time.sleep(2)
        
    def remove_item(self, product_id: str):
        """Remove item from cart."""
        button_locator = (By.ID, f"remove-{product_id}")
        
        # Wait for the remove button to be clickable
        remove_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        )
        
        # Click the button
        remove_btn.click()
        
        # Wait for item to be removed from DOM
        time.sleep(1)
