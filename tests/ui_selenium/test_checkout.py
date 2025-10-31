"""Selenium checkout flow tests."""
import pytest
from pages.selenium.products_page import ProductsPage
from pages.selenium.cart_page import CartPage

@pytest.mark.selenium
@pytest.mark.ui
@pytest.mark.smoke
class TestSeleniumCheckout:
    """Test suite for checkout functionality using Selenium."""
    
    def test_cart_page_displays_items(self, selenium_authenticated, 
                                     selenium_products_page: ProductsPage, 
                                     selenium_cart_page: CartPage):
        """Test that cart page displays added items."""
        selenium_products_page.navigate_to("/inventory.html")
        selenium_products_page.add_item_to_cart("sauce-labs-backpack")
        selenium_products_page.go_to_cart()
        
        item_count = selenium_cart_page.get_cart_item_count()
        assert item_count == 1, "Cart should display 1 item"
        
    def test_remove_item_from_cart_page(self, selenium_authenticated,
                                       selenium_products_page: ProductsPage,
                                       selenium_cart_page: CartPage):
        """Test removing item from cart page."""
        selenium_products_page.navigate_to("/inventory.html")
        selenium_products_page.add_item_to_cart("sauce-labs-backpack")
        selenium_products_page.go_to_cart()
        selenium_cart_page.remove_item("sauce-labs-backpack")
        
        item_count = selenium_cart_page.get_cart_item_count()
        assert item_count == 0, "Cart should be empty"
        
    def test_continue_shopping(self, selenium_authenticated,
                              selenium_products_page: ProductsPage,
                              selenium_cart_page: CartPage):
        """Test continue shopping button."""
        selenium_products_page.navigate_to("/inventory.html")
        selenium_products_page.add_item_to_cart("sauce-labs-backpack")
        selenium_products_page.go_to_cart()
        selenium_cart_page.continue_shopping()
        
        assert selenium_products_page.is_loaded(), "Should return to products page"
