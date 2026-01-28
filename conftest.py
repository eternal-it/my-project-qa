import pytest
import requests
import os
from config.settings import BASE_URL
from playwright.sync_api import sync_playwright

# =======================
# Фикстура для API-тестов
# =======================
@pytest.fixture(scope="session")                                   #Создаем фикстуру один раз на весь запуск тестов (еще варианты: "function" - для каждого теста, "class" - для каждого класса, "module" - для каждого модуля)
def api_client():                                                  #имя фикстуры - это имя функции
    """Фикстура: HTTP клиент для API"""
    session = requests.Session()                                   #Создаем объект сессии - умный HTTP клиент, который может сохранять заголовки, куки и переиспользовать соединения
    session.headers.update({"Content-Type": "application/json"})   #Отправляем HTTP-заголовок ко всем запросам, отправляемым этой сессией, чтобы сервер понимал, что тело запроса в JSON
    yield session                                                  #Отдаем объект session тесту
    session.close()                                                #Закрываем HTTP-сессию


# ======================
# Фикстура для UI-тестов
# ======================
@pytest.fixture(scope="function")
def page():
    """Фикстура: страница браузера для UI-тестов"""
    with sync_playwright() as p:
        # Запускаем Chromium в headless-режиме
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"widht": 1920, "height": 1080},
            locale="en-US"
        )
        page = context.new_page()
        page.set_default_timeout(15000)
        yield page
        browser.close()


# ======================
# Хук для скриншотов при падении
# ======================
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Делает скриншот при падении UI-тестов"""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        os.makedirs("screenshots", exist_ok=True)
        page = item.funcargs.get("page")
        if page:
            try:
                page.wait_for_timeout(500)
            except:
                pass

            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"\n Скриншот сохранен: {screenshot_path}")

            