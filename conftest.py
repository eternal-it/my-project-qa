import pytest
import requests
from config.settings import BASE_URL

@pytest.fixture(scope="session")                                   #Создаем фикстуру один раз на весь запуск тестов (еще варианты: "function" - для каждого теста, "class" - для каждого класса, "module" - для каждого модуля)
def api_client():                                                  #имя фикстуры - это имя функции
    """Фикстура: HTTP клиент для API"""
    session = requests.Session()                                   #Создаем объект сессии - умный HTTP клиент, который может сохранять заголовки, куки и переиспользовать соединения
    session.headers.update({"Content-Type": "application/json"})   #Отправляем HTTP-заголовок ко всем запросам, отправляемым этой сессией, чтобы сервер понимал, что тело запроса в JSON
    yield session                                                  #Отдаем объект session тесту
    session.close()                                                #Закрываем HTTP-сессию