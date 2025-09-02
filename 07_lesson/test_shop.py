import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Main_Shop import LoginPage

def test_shopping_cart_total():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        inventory_page = (LoginPage(driver)
                         .open()
                         .login())  
        
        (inventory_page
         .add_product_to_cart("Sauce Labs Backpack")
         .add_product_to_cart("Sauce Labs Bolt T-Shirt")
         .add_product_to_cart("Sauce Labs Onesie"))
        
        checkout_page = (inventory_page
                        .go_to_cart()
                        .checkout())
        
        checkout_page.fill_info("Артур", "Мухаметгареев", "qwerty123")
        
        total = checkout_page.get_total()
        
        assert total == "Total: $58.29", f"Ожидалась сумма $58.29, но получено: {total}"
        
        print("Успех! Итоговая сумма равна: $58.29")
        
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_shopping_cart_total()
