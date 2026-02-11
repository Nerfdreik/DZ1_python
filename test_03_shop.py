import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def test_shopping_cart_total():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    
    try:
        driver.get("https://www.saucedemo.com/")
        
        username_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "user-name"))
        )
        username_field.send_keys("standard_user")
        
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")
        
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        
        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt", 
            "Sauce Labs Onesie"
        ]
        
        for product_name in products_to_add:
            add_to_cart_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"))
            )
            add_to_cart_button.click()
        
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        
        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()
        
        first_name_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "first-name"))
        )
        first_name_field.send_keys("Артур")
        
        last_name_field = driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Мухаметгареев")
        
        postal_code_field = driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys("qwerty123")
        
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()
        
        total_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        
        assert "Total: $58.29" in total_text, f"Итоговая сумма неверная. Ожидалось: $58.29, Фактически: {total_text}"
        
        print("Тест пройден, сумма: $58.29")
        
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_shopping_cart_total()