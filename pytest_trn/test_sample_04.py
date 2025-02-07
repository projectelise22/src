from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import pytest

# Fixture to setup the Webdriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_valid(driver):
    # Get actual page
    driver.get("https://play1.automationcamp.ir/login.html")

    # Locate input fields
    username = driver.find_element(By.ID, "user")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

     # Perform login
    username.send_keys("admin") 
    password.send_keys("admin")
    login_button.click()

    # Assertion to check successful login
    assert "Pizza House" in driver.page_source, "Login failed!"

def test_calcpage_add(driver):
    # Open webpage
    driver.get("https://testsheepnz.github.io/BasicCalculator.html")

    # Locate the elements
    a1 = driver.find_element(By.ID, "number1Field")
    a2 = driver.find_element(By.ID, "number2Field")
    oper = driver.find_element(By.NAME, "selectOperation")
    calc = driver.find_element(By.ID, "calculateButton")
    clr = driver.find_element(By.ID, "clearButton")
    ans = driver.find_element(By.ID, "numberAnswerField")

    # Check based on different inputs
    # Check for addition only
    select = Select(oper)
    select.select_by_index(0)
    
    # Input the numbers and then click calculate
    a1.send_keys("5")
    a2.send_keys("5")
    calc.click()

    # Wait until value is available
    res = WebDriverWait(driver, 5).until(
        lambda d: ans.get_attribute("value") != ""
    )
    assert "10" == ans.get_attribute("value"), "Incorrect addition computation!"

    clr.click()



