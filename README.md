# Автотесты для сайта «Читай-город»

📌 **Описание задачи**

Проект автоматизирует тестирование сайта Читай-город с помощью UI и API тестов.

Для корректной работы тестов необходимо получить свежий токенна сайте https://www.chitai-gorod.ru/

ПУТЬ:
1) DevTools
2) Application
3) Cookies
4) В фильтре написать token - выбрать access-token
5) В графе Value актуакльный token




В рамках проекта реализованы:

1. UI тесты поиска книг по названию, автору и вводу некорректных символов.
2. API тесты работы корзины, поиска и избранного.
3. Использование **Page Object** для UI тестов.
4. Генерация **Allure-отчётов** для наглядной аналитики.

📂 **Структура проекта**

project/
│
├── pages/ # Page Object классы
│ ├── main_page.py # Главная страница (поиск)
│ ├── product_page.py # Страница товара
│ └── cart_page.py # Страница корзины
│
├── test_chitai_gorod.py # UI тесты
├── test_api.py # API тесты
├── conftest.py # Фикстуры pytest и конфиг драйвера
├── config.py # Конфигурации: токены, URL
├── requirements.txt # Зависимости проекта
└── README.md # Описание проекта


⚙️ **Подготовка окружения**

Клонировать проект:

```bash
git clone <ссылка-на-репозиторий>
cd project

Создать виртуальное окружение и активировать его:
python -m venv venv
source venv/bin/activate       # macOS / Linux
venv\Scripts\activate          # Windows

Установить зависимости:
pip install -r requirements.txt

🚀 Запуск тестов

UI тесты:
pytest test_chitai_gorod.py --alluredir=allure-results

API тесты:
pytest test_api.py --alluredir=allure-results

Все тесты:
pytest --alluredir=allure-results



📊 Просмотр Allure отчёта

Сформировать результаты:
pytest --alluredir=allure-results

Запустить сервер Allure:
allure serve allure-results


📝 Примечания

UI тесты используют WebDriverWait вместо time.sleep() для стабильности.

API тесты используют библиотеку requests.

Проект поддерживает повторяемость тестов — можно запускать 10+ раз подряд без изменения кода.

