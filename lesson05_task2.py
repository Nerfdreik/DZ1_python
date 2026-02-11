from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def click_blue_button_without_id():
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        
        driver.get("http://uitestingplayground.com/dynamicid")
        blue_button = driver.find_element(
            By.XPATH, 
            "//button[contains(@class, 'btn-primary') and text()='Button with Dynamic ID']"
        )
        blue_button.click()
        
        print("Клик по синей кнопке с динамическим ID выполнен успешно")
        
    except Exception as e:
        print(f"Ошибка: {e}")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    click_blue_button_without_id()