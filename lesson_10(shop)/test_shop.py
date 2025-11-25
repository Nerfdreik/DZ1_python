import pytest
import allure
from pages.login_page import LoginPage
from selenium.webdriver.remote.webdriver import WebDriver


@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
class TestShoppingCart:
    """Тесты для функциональности интернет-магазина."""
    
    @allure.title("Проверка итоговой суммы заказа")
    @allure.description("Тест проверяет корректность расчета итоговой суммы при добавлении нескольких товаров в корзину")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_shopping_cart_total(self, browser: WebDriver) -> None:
        """
        Тестирует расчет итоговой суммы заказа при добавлении трех товаров.
        
        Args:
            browser (WebDriver): Фикстура браузера
        """
        # Arrange
        expected_total = "Total: $58.29"
        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt", 
            "Sauce Labs Onesie"
        ]
        
        # Act
        with allure.step("Логин в интернет-магазин"):
            login_page = LoginPage(browser)
            inventory_page = login_page.open().login()
        
        with allure.step(f"Добавление товаров в корзину: {', '.join(products_to_add)}"):
            inventory_page.add_multiple_products_to_cart(products_to_add)
        
        with allure.step("Переход в корзину и начало оформления заказа"):
            checkout_page = (inventory_page
                           .go_to_cart()
                           .checkout())
        
        with allure.step("Заполнение информации для доставки"):
            checkout_page.fill_info("Артур", "Мухаметгареев", "qwerty123")
        
        with allure.step("Получение итоговой суммы заказа"):
            total = checkout_page.get_total()
        
        # Assert
        with allure.step(f"Проверка итоговой суммы: ожидается {expected_total}"):
            assert total == expected_total, f"Ожидалась сумма '{expected_total}', но получено: '{total}'"
        
        with allure.step("Прикрепление информации о успешном выполнении"):
            allure.attach(
                f"Тест успешно завершен. Итоговая сумма: {total}",
                name="Результат теста",
                attachment_type=allure.attachment_type.TEXT
            )
    
    @allure.title("Добавление одного товара в корзину")
    @allure.description("Тест проверяет добавление одного товара в корзину и переход к оформлению")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_single_product_to_cart(self, browser: WebDriver) -> None:
        """
        Тестирует добавление одного товара в корзину.
        
        Args:
            browser (WebDriver): Фикстура браузера
        """
        # Arrange
        product_name = "Sauce Labs Backpack"
        
        # Act
        with allure.step("Логин в интернет-магазин"):
            login_page = LoginPage(browser)
            inventory_page = login_page.open().login()
        
        with allure.step(f"Добавление товара '{product_name}' в корзину"):
            inventory_page.add_product_to_cart(product_name)
        
        with allure.step("Переход в корзину"):
            cart_page = inventory_page.go_to_cart()
        
        # Assert
        with allure.step("Проверка количества товаров в корзине"):
            cart_items_count = cart_page.get_cart_items_count()
            assert cart_items_count == 1, f"Ожидался 1 товар в корзине, но найдено: {cart_items_count}"
    
    @allure.title("Полное оформление заказа")
    @allure.description("Тест проверяет полный процесс оформления заказа от логина до завершения")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_complete_order_flow(self, browser: WebDriver) -> None:
        """
        Тестирует полный процесс оформления заказа.
        
        Args:
            browser (WebDriver): Фикстура браузера
        """
        # Arrange
        product_name = "Sauce Labs Fleece Jacket"
        
        # Act
        with allure.step("Логин в интернет-магазин"):
            login_page = LoginPage(browser)
            inventory_page = login_page.open().login()
        
        with allure.step(f"Добавление товара '{product_name}' в корзину"):
            inventory_page.add_product_to_cart(product_name)
        
        with allure.step("Оформление заказа"):
            checkout_page = (inventory_page
                           .go_to_cart()
                           .checkout())
            
            checkout_page.fill_info("Иван", "Иванов", "123456")
            checkout_page.finish_order()
        
        # Assert
        with allure.step("Проверка сообщения о успешном оформлении"):
            completion_message = checkout_page.get_completion_message()
            assert "Thank you for your order" in completion_message, \
                f"Ожидалось сообщение о успешном заказе, но получено: {completion_message}"


@allure.feature("Навигация по магазину")
@allure.severity(allure.severity_level.NORMAL)
class TestShopNavigation:
    """Тесты навигации по интернет-магазину."""
    
    @allure.title("Проверка доступности страниц магазина")
    @allure.description("Тест проверяет корректность загрузки всех страниц интернет-магазина")
    @allure.severity(allure.severity_level.NORMAL)
    def test_page_availability(self, browser: WebDriver) -> None:
        """
        Проверяет доступность и корректность загрузки всех страниц.
        
        Args:
            browser (WebDriver): Фикстура браузера
        """
        with allure.step("Проверка страницы логина"):
            login_page = LoginPage(browser)
            login_page.open()
            assert login_page.is_login_page_displayed(), "Страница логина не загружена корректно"
        
        with allure.step("Проверка страницы инвентаря после логина"):
            inventory_page = login_page.login()
            assert inventory_page.is_inventory_page_displayed(), "Страница инвентаря не загружена корректно"
        
        with allure.step("Проверка страницы корзины"):
            cart_page = inventory_page.go_to_cart()
            assert cart_page.is_cart_page_displayed(), "Страница корзины не загружена корректно"
        
        with allure.step("Проверка страницы оформления заказа"):
            checkout_page = cart_page.checkout()
            assert checkout_page.is_checkout_page_displayed(), "Страница оформления заказа не загружена корректно"
