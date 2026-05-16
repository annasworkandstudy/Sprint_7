# Автоматизация API

Проект содержит пакет автоматизированных тестов для проверки ключевых эндпоинтов API учебного сервиса «Яндекс.Самокат» (сущности Курьер и Заказ).

## Стек технологий
* **Язык**: Python 3.11+
* **Тестовый фреймворк**: [Pytest](https://pytest.org)
* **HTTP-клиент**: [Requests](https://readthedocs.io)
* **Генерация данных**: [Faker](https://readthedocs.io)
* **Отчетность**: [Allure Framework](https://allurereport.org)

## Структура проекта
* `url.py` — конфигурационный класс `URL` со всеми эндпоинтами стенда.
* `generators.py` — класс `GenerateData` для динамической генерации уникальных данных курьеров (с временными метками для предотвращения коллизий) и заказов.
* `scooter_methods.py` — класс `ScooterMethods` с обертками для HTTP-запросов (POST/GET) и интеграцией шагов `@allure.step`.
* `tests/` — директория с тест-кейсами:
  * `test_create_courier.py` — позитивные и негативные проверки создания курьера (включая обработку дубликатов).
  * `test_login_courier.py` — позитивные проверки авторизации и валидация ошибок при отправке неполных данных.
  * `test_create_order.py` — параметризованные тесты создания заказов с различными комбинациями цветов.

## Установка и подготовка

1. **Клонируйте репозиторий:**
   ```bash
   git clone <ссылка_на_ваш_репозиторий>
   cd <название_папки_проекта>
   ```

2. **Создайте и активируйте виртуальное окружение:**
   ```bash
   python -m venv .venv
   # Для Windows:
   .venv\Scripts\activate
   # Для macOS/Linux:
   source .venv/bin/activate
   ```

3. **Установите зависимости:**
   ```bash
   pip install pytest requests faker allure-pytest
   ```

4. **Убедитесь, что установлен Allure Commandline:**
   * **Windows** (via Scoop): `scoop install allure`
   * **macOS** (via Homebrew): `brew install allure`

## Запуск тестов

* **Запуск всех тестов сбором результатов для Allure:**
  ```bash
  pytest --alluredir=allure-results
  ```

* **Запуск конкретного файла (например, тесты заказов):**
  ```bash
  pytest tests/test_create_order.py --alluredir=allure-results
  ```

## Просмотр отчетов Allure

После завершения прогона тестов сгенерируйте и откройте интерактивный HTML-отчет в браузере командой:
```bash
allure serve allure-results
```