import pytest
import allure
import time
from pages.calculator_page import CalculatorPage
from selenium.webdriver.remote.webdriver import WebDriver


@allure.feature("Медленный калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    """Тесты для функциональности медленного калькулятора."""
    
    @allure.title("Тест вычисления 7 + 8 с задержкой 45 секунд")
    @allure.description("Тест проверяет корректность работы калькулятора с установленной задержкой вычислений")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_slow_calculator_addition(self, calculator_page: CalculatorPage) -> None:
        """
        Тестирует операцию сложения с большой задержкой вычислений.
        
        Args:
            calculator_page (CalculatorPage): Фикстура страницы калькулятора
        """
        # Arrange
        start_time = time.time()
        
        # Act
        with allure.step("Выполнение операции сложения 7 + 8"):
            (calculator_page.open()
             .set_delay(45)
             .click_button("7")
             .click_button("+")
             .click_button("8")
             .click_button("="))
        
        with allure.step("Ожидание результата вычислений"):
            result_waited = calculator_page.wait_for_result("15", timeout=50)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Assert
        with allure.step("Проверка результата вычислений"):
            result = calculator_page.get_result()
            assert result == "15", f"Ожидался результат '15', но получен '{result}'"
        
        with allure.step("Проверка времени выполнения"):
            assert result_waited, "Результат не появился в течение таймаута"
            assert execution_time >= 45, f"Вычисления заняли меньше времени ({execution_time:.2f}сек) чем установленная задержка"
            allure.attach(
                f"Время выполнения: {execution_time:.2f} секунд",
                name="Время выполнения",
                attachment_type=allure.attachment_type.TEXT
            )
    
    @allure.title("Проверка готовности калькулятора к работе")
    @allure.description("Тест проверяет, что все элементы калькулятора корректно загружены")
    @allure.severity(allure.severity_level.NORMAL)
    def test_calculator_ready_state(self, calculator_page: CalculatorPage) -> None:
        """
        Проверяет, что калькулятор загружен и все элементы доступны.
        
        Args:
            calculator_page (CalculatorPage): Фикстура страницы калькулятора
        """
        with allure.step("Открытие страницы калькулятора"):
            calculator_page.open()
        
        with allure.step("Проверка наличия всех элементов интерфейса"):
            assert calculator_page.is_calculator_ready(), "Не все элементы калькулятора загружены"
    
    @allure.title("Быстрое вычисление с минимальной задержкой")
    @allure.description("Тест проверяет работу калькулятора с минимальной задержкой вычислений")
    @allure.severity(allure.severity_level.NORMAL)
    def test_fast_calculation(self, calculator_page: CalculatorPage) -> None:
        """
        Тестирует операцию сложения с минимальной задержкой.
        
        Args:
            calculator_page (CalculatorPage): Фикстура страницы калькулятора
        """
        # Arrange
        start_time = time.time()
        
        # Act
        with allure.step("Выполнение операции с задержкой 1 секунда"):
            (calculator_page.open()
             .set_delay(1)
             .click_button("7")
             .click_button("+")
             .click_button("8")
             .click_button("="))
        
        with allure.step("Ожидание результата"):
            result_waited = calculator_page.wait_for_result("15", timeout=10)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Assert
        with allure.step("Проверка быстрого получения результата"):
            result = calculator_page.get_result()
            assert result == "15", f"Ожидался результат '15', но получен '{result}'"
            assert execution_time < 10, "Вычисления заняли слишком много времени"
    
    @allure.title("Проверка метода perform_calculation")
    @allure.description("Тест проверяет удобный метод для выполнения вычислений")
    @allure.severity(allure.severity_level.MINOR)
    def test_perform_calculation_method(self, calculator_page: CalculatorPage) -> None:
        """
        Тестирует удобный метод perform_calculation для выполнения вычислений.
        
        Args:
            calculator_page (CalculatorPage): Фикстура страницы калькулятора
        """
        with allure.step("Использование метода perform_calculation для сложения"):
            calculator_page.perform_calculation("7", "+", "8", delay=5)
        
        with allure.step("Ожидание и проверка результата"):
            result_waited = calculator_page.wait_for_result("15", timeout=10)
            result = calculator_page.get_result()
            
            assert result_waited, "Результат не появился в течение таймаута"
            assert result == "15", f"Ожидался результат '15', но получен '{result}'"


@allure.feature("Производительность калькулятора")
@allure.severity(allure.severity_level.NORMAL)
class TestCalculatorPerformance:
    """Тесты производительности калькулятора."""
    
    @allure.title("Измерение времени отклика калькулятора")
    @allure.description("Тест измеряет время отклика интерфейса калькулятора")
    @allure.severity(allure.severity_level.MINOR)
    def test_calculator_responsiveness(self, calculator_page: CalculatorPage) -> None:
        """
        Измеряет время отклика интерфейса калькулятора.
        
        Args:
            calculator_page (CalculatorPage): Фикстура страницы калькулятора
        """
        calculator_page.open()
        
        with allure.step("Измерение времени отклика кнопок"):
            start_time = time.time()
            calculator_page.click_button("7")
            end_time = time.time()
            response_time = end_time - start_time
            
            allure.attach(
                f"Время отклика кнопки: {response_time:.3f} секунд",
                name="Время отклика",
                attachment_type=allure.attachment_type.TEXT
            )
            
            assert response_time < 2, f"Время отклика слишком большое: {response_time:.3f}сек"
