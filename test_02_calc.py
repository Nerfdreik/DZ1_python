from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
import datetime
import pytest

def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html") 

    text_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    text_input.clear()
    text_input.send_keys("45")

    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()
    
    first_time = datetime.datetime.now()
    
    WebDriverWait(driver, 60).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
    
    later_time = datetime.datetime.now()
    
    time_difference = (later_time - first_time).total_seconds()
    assert 43 <= time_difference <= 47, f"Время выполнения {time_difference} секунд, ожидалось около 45 секунд"
    
    res = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert res == "15", f"Ожидался результат 15, но получен {res}"
    
    driver.quit()

if __name__ == "__main__":
    test_slow_calculator()