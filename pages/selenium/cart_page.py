"""Selenium cart page object."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.selenium.base_page import BasePage


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
        
    def remove_item(self, product_id: str):
        """Remove item from cart."""
        self.wait_for_cart_to_load()
        button_locator = (By.ID, f"remove-{product_id}")
        # Wait for the remove button to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(button_locator)
        )
        self.click(*button_locator)
        # Wait for the item to be removed
        WebDriverWait(self.driver, 10).until(
            EC.staleness_of(self.find_element(*button_locator))
        )
