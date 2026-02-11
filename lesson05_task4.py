from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get("http://the-internet.herokuapp.com/login")
    
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("Artur")
    
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("qwerty123")
    
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    
    flash_message = driver.find_element(By.ID, "flash")
    print("Текст с зеленой плашки:", flash_message.text)
    
except Exception as e:
    print(f"Ошибка: {e}")
    
finally:
    driver.quit()