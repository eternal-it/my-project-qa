import requests
from config import BASE_URL


def test_create_post():
    new_post = {
        "title": "Тестовый пост от QA",
        "body": "Этот пост создан автоматизированным тестом",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201, f"Ожидался статус 201, но по факту {response.status_code}!"

    data = response.json()

    assert "id" in data, "Поля id нет в файле"
    assert "title" in data, "Поля title нет в файле"
    assert "body" in data, "Поля body нет в файле"
    assert "userId" in data, "Поля userId нет в файле"

    assert data["title"] == new_post["title"], "Заголовок не совпадает"
    assert data["body"] == new_post["body"], "Текст не совпадает"
    assert data["userId"] == new_post["userId"], "userId не совпадает"
