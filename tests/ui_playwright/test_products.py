"""Playwright products page tests."""
import pytest
from pages.playwright.products_page import ProductsPage

@pytest.mark.playwright
@pytest.mark.ui
@pytest.mark.regression
class TestPlaywrightProducts:
    """Test suite for products functionality using Playwright."""
    
    def test_products_displayed(self, playwright_authenticated, 
                               playwright_products_page: ProductsPage):
        """Test that products are displayed after login."""
        playwright_products_page.navigate_to("/inventory.html")
        
        product_count = playwright_products_page.get_product_count()
        assert product_count > 0, "Products should be displayed"
        assert product_count == 6, "Should display 6 products"
        
    def test_add_single_item_to_cart(self, playwright_authenticated,
                                    playwright_products_page: ProductsPage):
        """Test adding a single item to cart."""
        playwright_products_page.navigate_to("/inventory.html")
        playwright_products_page.add_item_to_cart("sauce-labs-backpack")
        
        cart_count = playwright_products_page.get_cart_count()
        assert cart_count == 1, "Cart should show 1 item"
        
    def test_add_multiple_items(self, playwright_authenticated,
                               playwright_products_page: ProductsPage):
        """Test adding multiple items to cart."""
        playwright_products_page.navigate_to("/inventory.html")
        playwright_products_page.add_item_to_cart("sauce-labs-backpack")
        playwright_products_page.add_item_to_cart("sauce-labs-bike-light")
        playwright_products_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
        
        cart_count = playwright_products_page.get_cart_count()
        assert cart_count == 3, "Cart should show 3 items"
        
    def test_remove_item_from_cart(self, playwright_authenticated,
                                  playwright_products_page: ProductsPage):
        """Test removing item from cart."""
        playwright_products_page.navigate_to("/inventory.html")
        playwright_products_page.add_item_to_cart("sauce-labs-backpack")
        playwright_products_page.remove_item_from_cart("sauce-labs-backpack")
        
        cart_count = playwright_products_page.get_cart_count()
        assert cart_count == 0, "Cart should be empty"
