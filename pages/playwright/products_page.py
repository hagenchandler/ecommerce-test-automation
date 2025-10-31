from pages.playwright.base_page import BasePage

class ProductsPage(BasePage):
    """Products page interactions using Playwright."""
    
    # Locators
    PRODUCTS_TITLE = ".title"
    INVENTORY_ITEMS = ".inventory_item"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    PRODUCT_SORT = ".product_sort_container"
    
    def is_loaded(self) -> bool:
        """Check if products page is loaded."""
        return self.is_visible(self.PRODUCTS_TITLE)
        
    def get_product_count(self) -> int:
        """Get number of products displayed."""
        return self.page.locator(self.INVENTORY_ITEMS).count()
        
    def add_item_to_cart(self, product_id: str):
        """Add specific product to cart by ID."""
        self.click(f"#add-to-cart-{product_id}")
        
    def remove_item_from_cart(self, product_id: str):
        """Remove specific product from cart."""
        self.click(f"#remove-{product_id}")
        
    def get_cart_count(self) -> int:
        """Get number of items in cart."""
        if not self.is_visible(self.CART_BADGE):
            return 0
        return int(self.get_text(self.CART_BADGE))
        
    def go_to_cart(self):
        """Navigate to cart page."""
        self.click(self.CART_LINK)
