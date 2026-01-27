# tests/ui/test_demoga_search.py

def test_demoqa_search(page):
    page.goto("https://demoqa.com/text-box")
    page.fill("#userName", "Alex")
    page.fill("#userEmail", "alex@example.com")
    page.click("#submit")
    assert page.is_visible("#name")