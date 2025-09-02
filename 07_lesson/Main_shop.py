from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        
    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self
        
    def login(self, username="standard_user", password="secret_sauce"):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.username_input)
        ).send_keys(username)
        
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        return InventoryPage(self.driver)

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        
    def add_product_to_cart(self, product_name):
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"))
        )
        add_button.click()
        return self
        
    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
        return CartPage(self.driver)

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        
    def checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()
        return CheckoutPage(self.driver)

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        
    def fill_info(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_name_input)
        ).send_keys(first_name)
        
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()
        return self
        
    def get_total(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_label)
        ).text
