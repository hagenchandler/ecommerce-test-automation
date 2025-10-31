"""Playwright checkout flow tests."""
import pytest
from pages.playwright.products_page import ProductsPage
from pages.playwright.cart_page import CartPage

@pytest.mark.playwright
@pytest.mark.ui
@pytest.mark.smoke
class TestPlaywrightCheckout:
    """Test suite for checkout functionality using Playwright."""
    
    def test_cart_page_displays_items(self, playwright_authenticated, 
                                     playwright_products_page: ProductsPage, 
                                     playwright_cart_page: CartPage):
        """Test that cart page displays added items."""
        playwright_products_page.navigate_to("/inventory.html")
        playwright_products_page.add_item_to_cart("sauce-labs-backpack")
        playwright_products_page.go_to_cart()
        
        item_count = playwright_cart_page.get_cart_item_count()
        assert item_count == 1, "Cart should display 1 item"
        
    def test_remove_item_from_cart_page(self, playwright_authenticated,
                                       playwright_products_page: ProductsPage,
                                       playwright_cart_page: CartPage):
        """Test removing item from cart page."""
        playwright_products_page.navigate_to("/inventory.html")
        playwright_products_page.add_item_to_cart("sauce-labs-backpack")
        playwright_products_page.go_to_cart()
        playwright_cart_page.remove_item("sauce-labs-backpack")
        
        item_count = playwright_cart_page.get_cart_item_count()
        assert item_count == 0, "Cart should be empty"
        
    def test_continue_shopping(self, playwright_authenticated,
                              playwright_products_page: ProductsPage,
                              playwright_cart_page: CartPage):
        """Test continue shopping button."""
        playwright_products_page.navigate_to("/inventory.html")
        playwright_products_page.add_item_to_cart("sauce-labs-backpack")
        playwright_products_page.go_to_cart()
        playwright_cart_page.continue_shopping()
        
        assert playwright_products_page.is_loaded(), "Should return to products page"
