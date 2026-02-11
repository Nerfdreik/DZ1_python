from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def click_blue_button():
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        
        driver.get("http://uitestingplayground.com/classattr")
        
        
        blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        blue_button.click()
        
        print("Клик по синей кнопке выполнен успешно")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        
    finally:
        
        driver.quit()

if __name__ == "__main__":
    click_blue_button()