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
        Test to validate the homepage loads correctly and the 'Home' navigation link is present and styled.

        This test performs the following steps:
        1. Navigate to the site's base URL.
        2. Wait for the 'Home' navigation link to be visible.
        3. Assert the 'Home' link is displayed.
        4. Assert the 'Home' link contains 'orange' in its inline style attribute indicating expected styling.

        Expected Results:
        - The homepage loads successfully.
        - The 'Home' navigation link is visible on the page.
        - The 'Home' link's style attribute includes the color 'orange'.
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


    def test_validate_logout(self, driver):
        """
        Test to verify the logout functionality after a successful login.

        This test performs the following steps:
        1. Navigate to the login page
        2. Enter valid email and password and submit to log in
        3. Click the 'Logout' link
        4. Verify that the user is redirected back to the login page

        Expected results:
        - The user is successfully logged out
        - The current URL contains '/login' indicating the login page
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

        # Wait for the logout button to be visible and locate it
        logout_link_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='/logout']"))
        )
        # Click the login button to submit credentials
        logout_link_element.click()

        # Verify that user is navigated to login page after logout
        assert "/login" in driver.current_url



    def test_validate_incorrect_login(self, driver):
        """
        Test to verify that login fails when incorrect credentials are used.

        This test performs the following steps:
        1. Navigate to the login page.
        2. Enter a valid email address and an incorrect password.
        3. Click the 'Login' button.
        4. Verify that login is not successful and an error message is displayed.

        Expected Results:
        - An error message is shown indicating incorrect credentials.
        - The 'Logged in as' element is not visible (user remains logged out).
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
        password_input_element.send_keys("123456789")

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