# tests/ui/test_demoga_search.py

import pytest

@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_demoqa_search(page):
    page.goto("https://demoqa.com/text-box")
    
    # Ждём, пока поле станет кликабельным
    page.wait_for_selector("#userName", state="visible", timeout=15000)
    page.wait_for_function("() => document.querySelector('#userName').disabled === false")
    
    page.fill("#userName", "Alex")
    page.fill("#userEmail", "alex@example.com")
    page.click("#submit")
    
    # Ждём результата
    page.wait_for_selector("#name", timeout=10000)
    assert page.is_visible("#name")