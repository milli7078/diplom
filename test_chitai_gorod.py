import allure
import pytest
from pages.main_page import MainPage

@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
class TestBookSearch:
    @allure.title("Поиск книги по заголовку")
    @allure.description("Тест проверяет возможность поиска книги по заголовку 'гарри поттер'.")
    def test_by_name(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.search_book("гарри поттер")
        assert "Показываем результаты по запросу «гарри поттер», найдено:" in main_page.get_search_results_text()

    def test_by_name(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.search_book("гоголь")
        assert "Показываем результаты по запросу «гоголь», найдено:" in main_page.get_search_results_text()

    def test_by_incorrect_simvol(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.search_book("#$%^&*")
        assert "Поиск по запросу «#$%^&*» не принёс результатов" in main_page.get_search_results_text()

    def test_by_incorrect_simvol(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.search_book("123456789")
        assert "Поиск по запросу «123456789» не принёс результатов" in main_page.get_search_results_text()

    def test_by_incorrect_simvol(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.search_book("你好世界")
        assert "Поиск по запросу «你好世界» не принёс результатов" in main_page.get_search_results_text()