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
        
        # Добавляем товары в корзину
        (inventory_page
         .add_product_to_cart("Sauce Labs Backpack")
         .add_product_to_cart("Sauce Labs Bolt T-Shirt")
         .add_product_to_cart("Sauce Labs Onesie"))
        
        # Переходим в корзину и начинаем оформление заказа
        checkout_page = (inventory_page
                        .go_to_cart()
                        .checkout())
        
        
        assert total == "Total: $58.29", f"Ожидалась сумма $58.29, но получено: {total}"
        
        print("Успех! Итоговая сумма равна: $58.29")
        
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_shopping_cart_total()