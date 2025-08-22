from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def ajax_button_click():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        driver.get("http://uitestingplayground.com/ajax")
        
        blue_button = driver.find_element(By.ID, "ajaxButton")
        
        blue_button.click()
        
        wait = WebDriverWait(driver, 10)
        success_message = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
        )
        
        message_text = success_message.text
        print(message_text)
        
    except Exception as e:
        print(f"Ошибка: {e}")
        
    finally:
        driver.quit()

if __name__ == "__main__":

    ajax_button_click()
