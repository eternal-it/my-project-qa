# tests/ui/test_demoga_search.py

import pytest

@pytest.mark.flaky(reruns=2, reruns_delay=1)     # Декоратор, помечает тест как нестабильный ("flaky") и пробует запустить его еще 2 раза, если упадет. между попытками 1 секунда
def test_demoqa_search(page):
    page.goto("https://demoqa.com/text-box")     # Открывает страницу 
    
    # Ждём, пока поле станет кликабельным
    page.wait_for_selector("#userName", state="visible", timeout=15000)       # Ждем пока userName станет активным, без этого page.fill может упасть
    page.wait_for_function("() => document.querySelector('#userName').disabled === false") # Проверяем, что объект не заблокирован, отправляя java скрипт и ждем пока он вернет true 
    
    page.fill("#userName", "Alex")              # Находит поля и вводит туда инфу
    page.fill("#userEmail", "alex@example.com") 
    page.click("#submit")         # Кликает по полю submit
    
    # Ждём результата
    page.wait_for_selector("#name", timeout=10000)
    assert page.is_visible("#name")