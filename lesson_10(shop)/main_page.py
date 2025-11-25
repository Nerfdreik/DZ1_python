from typing import Tuple, Optional
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import allure


class BasePage:
    """Базовый класс для всех страниц веб-приложения."""
    
    def __init__(self, browser: WebDriver, url: Optional[str] = None) -> None:
        """
        Инициализация базовой страницы.
        
        Args:
            browser (WebDriver): Экземпляр WebDriver
            url (Optional[str]): URL страницы (по умолчанию None)
        """
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(browser, 10)
    
    def open(self) -> None:
        """
        Открывает страницу по указанному URL.
        
        Raises:
            ValueError: Если URL не указан
        """
        with allure.step(f"Открытие страницы: {self.url}"):
            if self.url:
                self.browser.get(self.url)
            else:
                raise ValueError("URL не указан для страницы")
    
    def is_element_present(self, locator: Tuple[By, str]) -> bool:
        """
        Проверяет наличие элемента на странице.
        
        Args:
            locator (Tuple[By, str]): Кортеж с стратегией поиска и локатором
            
        Returns:
            bool: True если элемент присутствует, иначе False
        """
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def click_element(self, locator: Tuple[By, str]) -> None:
        """
        Кликает на элемент.
        
        Args:
            locator (Tuple[By, str]): Кортеж с стратегией поиска и локатором
        """
        with allure.step(f"Клик по элементу: {locator[1]}"):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
    
    def input_text(self, locator: Tuple[By, str], text: str) -> None:
        """
        Вводит текст в поле ввода.
        
        Args:
            locator (Tuple[By, str]): Кортеж с стратегией поиска и локатором
            text (str): Текст для ввода
        """
        with allure.step(f"Ввод текста '{text}' в поле: {locator[1]}"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
    
    def get_element_text(self, locator: Tuple[By, str]) -> str:
        """
        Получает текст элемента.
        
        Args:
            locator (Tuple[By, str]): Кортеж с стратегией поиска и локатором
            
        Returns:
            str: Текст элемента
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    def get_current_url(self) -> str:
        """
        Получает текущий URL страницы.
        
        Returns:
            str: Текущий URL
        """
        return self.browser.current_url
    
