"""Playwright login functionality tests."""
import pytest
from pages.playwright.login_page import LoginPage
from pages.playwright.products_page import ProductsPage
from utils.config import config

@pytest.mark.smoke
@pytest.mark.playwright
@pytest.mark.ui
class TestPlaywrightLogin:
    """Test suite for login functionality using Playwright."""
    
    def test_successful_login(self, playwright_login_page: LoginPage, 
                             playwright_products_page: ProductsPage):
        """Test successful login with valid credentials."""
        playwright_login_page.navigate()
        playwright_login_page.login(config.VALID_USER, config.PASSWORD)
        
        assert playwright_products_page.is_loaded(), \
            "Products page should be displayed after login"
        
    def test_invalid_username(self, playwright_login_page: LoginPage):
        """Test login with invalid username."""
        playwright_login_page.navigate()
        playwright_login_page.login("invalid_user", config.PASSWORD)
        
        assert playwright_login_page.is_error_displayed(), \
            "Error message should be displayed"
        error_text = playwright_login_page.get_error_message()
        assert "Epic sadface" in error_text
        
    def test_invalid_password(self, playwright_login_page: LoginPage):
        """Test login with invalid password."""
        playwright_login_page.navigate()
        playwright_login_page.login(config.VALID_USER, "wrong_password")
        
        assert playwright_login_page.is_error_displayed(), \
            "Error message should be displayed"
        
    def test_empty_credentials(self, playwright_login_page: LoginPage):
        """Test login with empty credentials."""
        playwright_login_page.navigate()
        playwright_login_page.login("", "")
        
        assert playwright_login_page.is_error_displayed(), \
            "Error message should be displayed"
        error_text = playwright_login_page.get_error_message()
        assert "Username is required" in error_text
        
    def test_locked_out_user(self, playwright_login_page: LoginPage):
        """Test login with locked out user."""
        playwright_login_page.navigate()
        playwright_login_page.login(config.LOCKED_USER, config.PASSWORD)
        
        assert playwright_login_page.is_error_displayed(), \
            "Error message should be displayed"
        error_text = playwright_login_page.get_error_message()
        assert "locked out" in error_text.lower()
