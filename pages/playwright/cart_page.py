"""Playwright cart page object."""
from pages.playwright.base_page import BasePage

class CartPage(BasePage):
    """Shopping cart page interactions using Playwright."""
    
    # Locators
    CART_ITEMS = ".cart_item"
    CHECKOUT_BUTTON = "#checkout"
    CONTINUE_SHOPPING = "#continue-shopping"
    
    def get_cart_item_count(self) -> int:
        """Get number of items in cart."""
        return self.page.locator(self.CART_ITEMS).count()
        
    def proceed_to_checkout(self):
        """Click checkout button."""
        self.click(self.CHECKOUT_BUTTON)
        
    def continue_shopping(self):
        """Return to products page."""
        self.click(self.CONTINUE_SHOPPING)
        
    def remove_item(self, product_id: str):
        """Remove item from cart."""
        self.click(f"#remove-{product_id}")
