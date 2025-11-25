from typing import Optional
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import allure
from .base_page import BasePage


class CalculatorPage(BasePage):
    """Класс для работы со страницей калькулятора."""
    
    def __init__(self, browser: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.
        
        Args:
            browser (WebDriver): Экземпляр WebDriver
        """
        super().__init__(browser, "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
        self.BUTTON_7 = (By.XPATH, "//span[text()='7']")
        self.BUTTON_8 = (By.XPATH, "//span[text()='8']")
        self.BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
        self.BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
        self.RESULT_DISPLAY = (By.CSS_SELECTOR, ".screen")
    
    def set_delay(self, delay_seconds: int) -> 'CalculatorPage':
        """
        Устанавливает задержку вычислений в калькуляторе.
        
        Args:
            delay_seconds (int): Количество секунд задержки
            
        Returns:
            CalculatorPage: Текущий экземпляр страницы для цепочки вызовов
        """
        with allure.step(f"Установка задержки вычислений: {delay_seconds} секунд"):
            self.input_text(self.DELAY_INPUT, str(delay_seconds))
            return self
    
    def click_button(self, button_text: str) -> 'CalculatorPage':
        """
        Нажимает кнопку калькулятора по тексту.
        
        Args:
            button_text (str): Текст на кнопке ('7', '8', '+', '=' и т.д.)
            
        Returns:
            CalculatorPage: Текущий экземпляр страницы для цепочки вызовов
            
        Raises:
            ValueError: Если передан неизвестный текст кнопки
        """
        with allure.step(f"Нажатие кнопки: '{button_text}'"):
            button_locators = {
                "7": self.BUTTON_7,
                "8": self.BUTTON_8,
                "+": self.BUTTON_PLUS,
                "=": self.BUTTON_EQUALS
            }
            
            if button_text not in button_locators:
                raise ValueError(f"Неизвестная кнопка: {button_text}")
            
            self.click_element(button_locators[button_text])
            return self
    
    def wait_for_result(self, expected_result: str, timeout: int = 50) -> bool:
        """
        Ожидает появления ожидаемого результата на экране калькулятора.
        
        Args:
            expected_result (str): Ожидаемый результат вычислений
            timeout (int): Максимальное время ожидания в секундах (по умолчанию 50)
            
        Returns:
            bool: True если результат появился в течение timeout, иначе False
        """
        with allure.step(f"Ожидание результата: '{expected_result}' (таймаут: {timeout}сек)"):
            try:
                wait = WebDriverWait(self.browser, timeout)
                wait.until(
                    EC.text_to_be_present_in_element(self.RESULT_DISPLAY, expected_result)
                )
                return True
            except TimeoutException:
                return False
    
    def get_result(self) -> str:
        """
        Получает текущий результат с экрана калькулятора.
        
        Returns:
            str: Текст результата вычислений
        """
        return self.get_element_text(self.RESULT_DISPLAY)
    
    def perform_calculation(self, num1: str, operator: str, num2: str, delay: int = 45) -> 'CalculatorPage':
        """
        Выполняет вычисление с заданными параметрами.
        
        Args:
            num1 (str): Первое число
            operator (str): Оператор ('+', '-', '*', '/')
            num2 (str): Второе число
            delay (int): Задержка вычислений в секундах (по умолчанию 45)
            
        Returns:
            CalculatorPage: Текущий экземпляр страницы для цепочки вызовов
        """
        with allure.step(f"Выполнение вычисления: {num1} {operator} {num2} с задержкой {delay}сек"):
            return (self.open()
                    .set_delay(delay)
                    .click_button(num1)
                    .click_button(operator)
                    .click_button(num2)
                    .click_button("="))
    
    def is_calculator_ready(self) -> bool:
        """
        Проверяет, что калькулятор загружен и готов к работе.
        
        Returns:
            bool: True если все основные элементы калькулятора присутствуют
        """
        return (self.is_element_present(self.DELAY_INPUT) and
                self.is_element_present(self.BUTTON_7) and
                self.is_element_present(self.BUTTON_8) and
                self.is_element_present(self.BUTTON_PLUS) and
                self.is_element_present(self.BUTTON_EQUALS) and
                self.is_element_present(self.RESULT_DISPLAY))
