"""Helper utilities for tests."""
import os
from datetime import datetime
from pathlib import Path

def take_screenshot(driver_or_page, test_name: str, framework: str = "selenium"):
    """Take screenshot and save with timestamp.
    
    Args:
        driver_or_page: Selenium WebDriver or Playwright Page
        test_name: Name of the test
        framework: 'selenium' or 'playwright'
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = Path("screenshots")
    screenshot_dir.mkdir(exist_ok=True)
    
    filename = f"{framework}_{test_name}_{timestamp}.png"
    filepath = screenshot_dir / filename
    
    if framework == "selenium":
        driver_or_page.save_screenshot(str(filepath))
    else:  # playwright
        driver_or_page.screenshot(path=str(filepath))
    
    return str(filepath)

def get_test_data(filename: str):
    """Load test data from file."""
    # Placeholder for loading test data from JSON/CSV
    pass
