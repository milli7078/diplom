import allure
import requests
token="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTUzNDE4NDcsImlhdCI6MTc1NTE3Mzg0NywiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6Ijg2Yjg5M2Q2ZGM1MTJmNGIwYzYxN2RmZTEwMzk4ZjIxZDM4NTJlNmNkYjFhNTg4NmY4ZTQ0Yjk0NmIxNTRjNGIiLCJ0eXBlIjoxMH0.0Czycqh0ZmZV7ZZPnY38PYuTCBdWWJ1nVHkw6BH65iQ"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 YaBrowser/25.4.0.0 Safari/537.36","authorization":token}
base_url = "https://web-gate.chitai-gorod.ru/api/"

@allure.epic("API Тестирование")
@allure.feature("Добавление книги")
@allure.title("Тестирование добавления книги")
@allure.description("Проверка, что API добавляет книгу в корзину")
def test_add_book():
    body={"id":2968841,"adData":{"product_shelf":"","item_list_name":"catalog-page"}}
    resp = requests.post(f"{base_url}v1/cart/product", headers=headers,json=body)
    assert resp.status_code == 200

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Тестирование поиска книги по названию")
@allure.description("Проверка, что API возвращает книгу с ожидаемым названием")
def test_api_book_by_title():
    resp = requests.get(f"{base_url}v2/search/product?phrase=капитанская дочка", headers=headers)
    assert resp.status_code == 200


@allure.epic("API Тестирование")
@allure.feature("Содержание избранного")
@allure.title("Тестирование содержание избранного после удаления")
@allure.description("Проверка, что API показывает содержание избранного после удаления книги")
def test_api_book_by_title():
    resp = requests.get(f"{base_url}v1/cart/short", headers=headers)
    assert resp.status_code == 200

@allure.epic("API Тестирование")
@allure.feature("Содержание избранного после добавления")
@allure.title("Тестирование Содержание избранного после добавления")
@allure.description("Проверка, что API показывает Содержание избранного после добавления")
def test_api_book_by_title():
    resp = requests.get(f"{base_url}v1/cart/short", headers=headers)
    assert resp.status_code == 200

@allure.epic("API Тестирование")
@allure.feature("Поиск автора")
@allure.title("Тестирование поиска по автору")
@allure.description("Проверка, что API возвращает поиск автора с ожидаемым названием")
def test_api_book_by_title():
    resp = requests.get(f"{base_url}v2/search/product?phrase=гоголь", headers=headers)
    assert resp.status_code == 200