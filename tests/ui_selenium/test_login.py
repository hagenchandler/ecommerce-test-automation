"""Selenium login functionality tests."""
import pytest
from pages.selenium.login_page import LoginPage
from pages.selenium.products_page import ProductsPage
from utils.config import config

@pytest.mark.smoke
@pytest.mark.selenium
@pytest.mark.ui
class TestSeleniumLogin:
    """Test suite for login functionality using Selenium."""
    
    def test_successful_login(self, selenium_login_page: LoginPage, 
                             selenium_products_page: ProductsPage):
        """Test successful login with valid credentials."""
        selenium_login_page.navigate()
        selenium_login_page.login(config.VALID_USER, config.PASSWORD)
        
        assert selenium_products_page.is_loaded(), \
            "Products page should be displayed after login"
        
    def test_invalid_username(self, selenium_login_page: LoginPage):
        """Test login with invalid username."""
        selenium_login_page.navigate()
        selenium_login_page.login("invalid_user", config.PASSWORD)
        
        assert selenium_login_page.is_error_displayed(), \
            "Error message should be displayed"
        error_text = selenium_login_page.get_error_message()
        assert "Epic sadface" in error_text
        
    def test_invalid_password(self, selenium_login_page: LoginPage):
        """Test login with invalid password."""
        selenium_login_page.navigate()
        selenium_login_page.login(config.VALID_USER, "wrong_password")
        
        assert selenium_login_page.is_error_displayed(), \
            "Error message should be displayed"
        
    def test_empty_credentials(self, selenium_login_page: LoginPage):
        """Test login with empty credentials."""
        selenium_login_page.navigate()
        selenium_login_page.login("", "")
        
        assert selenium_login_page.is_error_displayed(), \
            "Error message should be displayed"
        error_text = selenium_login_page.get_error_message()
        assert "Username is required" in error_text
        
    def test_locked_out_user(self, selenium_login_page: LoginPage):
        """Test login with locked out user."""
        selenium_login_page.navigate()
        selenium_login_page.login(config.LOCKED_USER, config.PASSWORD)
        
        assert selenium_login_page.is_error_displayed(), \
            "Error message should be displayed"
        error_text = selenium_login_page.get_error_message()
        assert "locked out" in error_text.lower()
