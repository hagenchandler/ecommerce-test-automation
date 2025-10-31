"""Selenium products page object."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.selenium.base_page import BasePage


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
        # Get current cart count
        current_count = self.get_cart_count()
        
        # Click add to cart button
        button_locator = (By.ID, f"add-to-cart-{product_id}")
        self.click(*button_locator)
        
        # Wait for cart badge to update (if going from 0 to 1, wait for badge to appear)
        if current_count == 0:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.CART_BADGE)
            )
        else:
            # Wait for count to increment
            WebDriverWait(self.driver, 10).until(
                lambda driver: self.get_cart_count() > current_count
            )
        
    def remove_item_from_cart(self, product_id: str):
        """Remove specific product from cart."""
        # Get current cart count
        current_count = self.get_cart_count()
        
        # Click remove button
        button_locator = (By.ID, f"remove-{product_id}")
        self.click(*button_locator)
        
        # Wait for cart count to decrease or badge to disappear
        if current_count == 1:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(self.CART_BADGE)
            )
        else:
            WebDriverWait(self.driver, 10).until(
                lambda driver: self.get_cart_count() < current_count
            )
        
    def get_cart_count(self) -> int:
        """Get number of items in cart."""
        try:
            if self.is_visible(*self.CART_BADGE, timeout=1):
                return int(self.get_text(*self.CART_BADGE))
        except:
            pass
        return 0
        
    def go_to_cart(self):
        """Navigate to cart page."""
        self.click(*self.CART_LINK)
        # Wait for cart page to load
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/cart.html")
        )
