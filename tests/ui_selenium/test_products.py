"""Selenium products page tests."""
import pytest
from pages.selenium.products_page import ProductsPage

@pytest.mark.selenium
@pytest.mark.ui
@pytest.mark.regression
class TestSeleniumProducts:
    """Test suite for products functionality using Selenium."""
    
    def test_products_displayed(self, selenium_authenticated, 
                               selenium_products_page: ProductsPage):
        """Test that products are displayed after login."""
        selenium_products_page.navigate_to("/inventory.html")
        
        product_count = selenium_products_page.get_product_count()
        assert product_count > 0, "Products should be displayed"
        assert product_count == 6, "Should display 6 products"
    
    @pytest.mark.xfail(reason="Selenium cart state isolation issue in CI")
    def test_add_single_item_to_cart(self, selenium_authenticated,
                                    selenium_products_page: ProductsPage):
        """Test adding a single item to cart."""
        selenium_products_page.navigate_to("/inventory.html")
        selenium_products_page.add_item_to_cart("sauce-labs-backpack")
        
        cart_count = selenium_products_page.get_cart_count()
        assert cart_count == 1, "Cart should show 1 item"
    
    @pytest.mark.xfail(reason="Selenium cart state isolation issue in CI")
    def test_add_multiple_items(self, selenium_authenticated,
                               selenium_products_page: ProductsPage):
        """Test adding multiple items to cart."""
        selenium_products_page.navigate_to("/inventory.html")
        selenium_products_page.add_item_to_cart("sauce-labs-backpack")
        selenium_products_page.add_item_to_cart("sauce-labs-bike-light")
        
        cart_count = selenium_products_page.get_cart_count()
        assert cart_count == 2, "Cart should show 2 items"
    
    @pytest.mark.xfail(reason="Selenium cart state isolation issue in CI")
    def test_remove_item_from_products_page(self, selenium_authenticated,
                                           selenium_products_page: ProductsPage):
        """Test removing item from products page."""
        selenium_products_page.navigate_to("/inventory.html")
        selenium_products_page.add_item_to_cart("sauce-labs-backpack")
        selenium_products_page.remove_item_from_cart("sauce-labs-backpack")
        
        cart_count = selenium_products_page.get_cart_count()
        assert cart_count == 0, "Cart should be empty"
