from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service

edge_driver_path = "C:/Users/User/Desktop 2/СКУ ПРО/DZ PYTHON/DZ7_lesson/msedgedriver.exe"

service = Service(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service)

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")
    
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".is-invalid"))
    )
    
    zip_code_field = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
    assert "is-invalid" in zip_code_field.get_attribute("class"), "Поле Zip code не подсвечено красным"
    
    valid_fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]
    
    for field in valid_fields:
        element = driver.find_element(By.CSS_SELECTOR, f"input[name='{field}']")
        assert "is-valid" in element.get_attribute("class"), f"Поле {field} не подсвечено зеленым"

finally:
    driver.quit()