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
        Test to Login User with correct email and password


        """
        driver.get(self.base_url)
        home_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Home')]"))
        )
        assert home_element.is_displayed()
        style_attribute = home_element.get_attribute("style")
        assert "orange" in style_attribute

    def test_validate_login(self, driver):
        """
        Test to Login User with correct email and password.

        This test performs the following validations:
        1. Navigates to the automation exercise.com homepage
        2. Clicks on 'Signup / Login' link
        3. Verifies 'Login to your account' is visible
        4. Enters correct email address and password
        5. Clicks 'Login' button
        6. Verifies that 'Logged in as username' is visible

        Expected Results:
        - User should be successfully logged in
        - Username should be displayed in the navigation bar
        """
        # Navigate to the login page
        driver.get(self.base_url + "login")

        # Wait for the email input field to be visible and locate it
        email_input_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        # Enter the email address
        email_input_element.send_keys("hagai.tregerman@gmail.com")

        # Wait for the password input field to be visible and locate it
        password_input_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        # Enter the password
        password_input_element.send_keys("KMsuTYNyY@Q5y")

        # Wait for the login button to be visible and locate it
        login_button_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Login']"))
        )
        # Click the login button to submit credentials
        login_button_element.click()

        # Wait for the 'Logged in as' element to be visible after successful login
        logged_in_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Logged in as')]"))
        )
        # Verify the 'Logged in as' element is displayed
        assert logged_in_element.is_displayed()
        # Verify the username 'hagai tregerman' appears in the logged in message
        assert "hagai tregerman" in logged_in_element.text.lower()
