import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAutomationTask:
    base_url = "https://automationexercise.com/"

    @pytest.fixture
    def driver(self):
        """Setup and teardown for the WebDriver"""
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_validate_homepage(self, driver):
        """
        Test to validate the homepage elements and styling.

        This test performs the following validations:
        1. Navigates to the automation exercise.com homepage
        2. Verifies that the 'Home' navigation link is visible
        3. Validates that the 'Home' link has orange color styling
         Expected Results:
        - Home element should be displayed on the page
        - Home element's style attribute should contain 'orange' color
        """
        driver.get(self.base_url)
        home_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Home')]"))
        )
        assert home_element.is_displayed()
        style_attribute = home_element.get_attribute("style")
        assert "orange" in style_attribute

