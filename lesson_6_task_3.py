from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.maximize_window()
driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

element = WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#text'), 'Done!')
    )

src = driver.find_element(By.CSS_SELECTOR, '#award').get_attribute('src')

print(src)

driver.quit()