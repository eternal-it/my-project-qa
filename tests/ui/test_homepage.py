# tests/ui/test_homepage.py

import pytest
from playwright.sync_api import sync_playwright

def test_homepage_has_title():
    with sync_playwright() as p:
        #Запускаем браузер (без GUI - "headless")
        browser = p.chromium.launch()
        page = browser.new_page()

        #Открываем страницу
        page.goto("https://example.com")

        #Проверяем заголовок
        assert page.title() == "Example Domain"

        #Закрываем браузер
        browser.close()