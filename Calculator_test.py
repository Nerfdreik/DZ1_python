import time
import pytest
from selenium import webdriver
from Main_Calculator_page import CalculatorPage

def test_slow_calculator():
    driver = webdriver.Chrome()
    calculator_page = CalculatorPage(driver)
    
    try:
        start_time = time.time()
        
        (calculator_page.open()
         .set_delay(45)
         .click_button("7")
         .click_button("+")
         .click_button("8")
         .click_button("=")
         .wait_for_result("15"))
        
        end_time = time.time()
        
        result = calculator_page.get_result()
        assert result == "15", f"Expected result '15', but got '{result}'"
        
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_slow_calculator()
