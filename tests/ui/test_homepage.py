# tests/ui/test_homepage.py

def test_homepage_has_title(page):
        page.goto("https://example.com")          #Открываем страницу
        assert page.title() == "Example Domain"   #Проверяем заголовок