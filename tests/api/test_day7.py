import pytest
from config.settings import BASE_URL
from utils.helpers import assert_is_positive_int
from utils.logger import logger

print("...Логер инициализирован")
@pytest.mark.parametrize("user_id,title",[
    (1, "Post of the user 1"),
    (2, "Post of the user 2"),
    (3, "Post of the user 3")
])

def test_my_performance(api_client, user_id, title):
    logger.info(f"Начинаем тест для user_id={user_id}, title='{title}'")
    text_body = "Текст поста"
    new_post = {
        "title": title,
        "body": text_body,
        "userId": user_id
    }

    response = api_client.post(f"{BASE_URL}/posts", json=new_post)
    logger.info(f"Получен статус: {response.status_code}")
    assert response.status_code == 201, f"Ожидался код 201, но получили {response.status_code}"
    
    data = response.json()
    assert "id" in data
    assert_is_positive_int(data["id"])
    logger.info(f"Проверка {data['id']} выполнена")

    assert data["title"] == title
    assert data["body"] == text_body
    assert data["userId"] == user_id
    logger.info(f"Все проверки выполнены")


