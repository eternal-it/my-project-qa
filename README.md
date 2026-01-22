# QA Automation Learning Project

Проект для изучения автоматизированного тестирования API и UI

## Стек технологий
- Python 3.9+
- pytest
- requests
- Playwringht

## Как запустить
1. Установи зависимости:
```bash
   pip install -r requirements.txt
```

2. Установи браузеры Playwright:
```bash
   python -m playwright install
```

3. Запусти тесты
```bash
   python -m pytest tests/ -v
```

## Структура
- `tests/api/` - API-тесты
- `test/ui/` - UI-тесты
- `utils/` - вспомогательные функции
- `config/` - настройки