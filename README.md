# QA Automation Learning Project

[![Tests](https://github.com/eternal-it/my-project-qa/actions/workflows/tests.yml/badge.svg)](https://github.com/eternal-it/my-project-qa/actions)

## Проект для изучения автоматизированного тестирования API и UI.

## Стек технологий
- Python 3.9+
- pytest
- requests
- Playwright
- Allure Framework
- GitHub Actions

## Как запустить`
1. Установи зависимости:
```bash
   pip3 install -r requirements.txt
```

2. Установи браузеры Playwright:
```bash
   python3 -m playwright install
```

3. Запуск тестов
```bash
   # Все тесты
   python3 -m pytest tests/ -v

   # Только API
   python3 -m pytest tests/api/ -v

   # Только UI
   python3 -m pytest tests/ui/ -v

   # Параллельный запуск (4 потока)
   python3 -m pytest tests/ -n 4
```

## Генерация отчета Allure
1. Запустить тесты с сохранением результатов
```bash
   python3 -m pytest tests/ --alluredir=./allure-results
```
2. Посмотреть отчет
```bash
   allure serve ./allure-results
```

## Структура
- `tests/api/` - API-тесты (requests + pytest)
- `test/ui/` - UI-тесты (Playwright)
- `utils/` - вспомогательные функции и логгер
- `config/` - настройки (BASE_URL и др.)
- `conftest.py` - фикстуры и хуки pytest
- `pytest.ini` - конфигурация pytest
- `screenshots/` - автоматические скриншоты

## CI/CD
Тесты автоматически запускаются при каждом пуше в `main` через **GitHub Actions**