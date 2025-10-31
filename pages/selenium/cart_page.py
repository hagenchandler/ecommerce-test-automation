"""Selenium cart page object."""
from selenium.webdriver.common.by import By
from pages.selenium.base_page import BasePage

class CartPage(BasePage):
    """Shopping cart page interactions using Selenium."""
    
    # Locators
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    
    def get_cart_item_count(self) -> int:
        """Get number of items in cart."""
        return len(self.find_elements(*self.CART_ITEMS))
        
    def proceed_to_checkout(self):
        """Click checkout button."""
        self.click(*self.CHECKOUT_BUTTON)
        
    def continue_shopping(self):
        """Return to products page."""
        self.click(*self.CONTINUE_SHOPPING)
        
    def remove_item(self, product_id: str):
        """Remove item from cart."""
        button_locator = (By.ID, f"remove-{product_id}")
        self.click(*button_locator)
