"""Performance comparison between Selenium and Playwright."""
import pytest
import time
from pages.selenium.login_page import LoginPage as SeleniumLoginPage
from pages.selenium.products_page import ProductsPage as SeleniumProductsPage
from pages.playwright.login_page import LoginPage as PlaywrightLoginPage
from pages.playwright.products_page import ProductsPage as PlaywrightProductsPage
from utils.config import config

@pytest.mark.comparison
class TestPerformanceComparison:
    """Compare Selenium vs Playwright performance."""
    
    def test_selenium_login_time(self, request):
        """Measure Selenium login time."""
        from utils.driver_factory import DriverFactory
        
        # Use Firefox explicitly
        driver = DriverFactory.get_driver(browser="firefox")
        
        login_page = SeleniumLoginPage(driver)
        products_page = SeleniumProductsPage(driver)
        
        start_time = time.time()
        login_page.navigate()
        login_page.login(config.VALID_USER, config.PASSWORD)
        assert products_page.is_loaded()
        elapsed_time = time.time() - start_time
        
        print(f"\nSelenium (Firefox) login time: {elapsed_time:.2f} seconds")
        assert elapsed_time < 10, "Login should complete within 10 seconds"
        
        driver.quit()
    
    def test_playwright_login_time(self, playwright_page):
        """Measure Playwright login time."""
        login_page = PlaywrightLoginPage(playwright_page)
        products_page = PlaywrightProductsPage(playwright_page)
        
        start_time = time.time()
        login_page.navigate()
        login_page.login(config.VALID_USER, config.PASSWORD)
        assert products_page.is_loaded()
        elapsed_time = time.time() - start_time
        
        print(f"\nPlaywright login time: {elapsed_time:.2f} seconds")
        assert elapsed_time < 10, "Login should complete within 10 seconds"
    
    def test_selenium_add_to_cart_time(self, request):
        """Measure Selenium cart operations time."""
        from utils.driver_factory import DriverFactory
        
        # Use Firefox explicitly and authenticate
        driver = DriverFactory.get_driver(browser="firefox")
        login_page = SeleniumLoginPage(driver)
        login_page.navigate()
        login_page.login(config.VALID_USER, config.PASSWORD)
        
        products_page = SeleniumProductsPage(driver)
        products_page.navigate_to("/inventory.html")
        
        start_time = time.time()
        for _ in range(5):
            products_page.add_item_to_cart("sauce-labs-backpack")
            products_page.remove_item_from_cart("sauce-labs-backpack")
        elapsed_time = time.time() - start_time
        
        print(f"\nSelenium (Firefox) cart operations time: {elapsed_time:.2f} seconds")
        
        driver.quit()
        
    def test_playwright_add_to_cart_time(self, playwright_authenticated,
                                        playwright_products_page: PlaywrightProductsPage):
        """Measure Playwright cart operations time."""
        playwright_products_page.navigate_to("/inventory.html")
        
        start_time = time.time()
        for _ in range(5):
            playwright_products_page.add_item_to_cart("sauce-labs-backpack")
            playwright_products_page.remove_item_from_cart("sauce-labs-backpack")
        elapsed_time = time.time() - start_time
        
        print(f"\nPlaywright cart operations time: {elapsed_time:.2f} seconds")
