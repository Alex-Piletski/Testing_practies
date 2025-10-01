# QA Portfolio

## Описание
Учебный проект для практики тестирования на разных уровнях:
- UI-тесты: Python + Selenium
- API-тесты: Postman
- Нагрузочные тесты: JMeter

Тесты проводились на учебных сайтах:
- [SauceDemo](https://www.saucedemo.com/) — интернет-магазин для UI и функционального тестирования.
- [Restful Booker](https://restful-booker.herokuapp.com/) — API для тестирования запросов.

Цель проекта: показать навыки в различных типах тестирования, автоматизации и документации тестовых сценариев.

## Как запускать тесты

### UI-тесты (Python + Selenium)
bash
cd ui-tests
python -m venv venv
source venv/bin/activate   # Unix
pip install -r requirements.txt
pytest tests

### API-тесты (Postman)
Импортируйте коллекцию Postman (collection.json) и окружение (environment.json) в Postman.

### Нагрузочные тесты (JMeter)
Откройте load_tests/***.jmx в JMeter и запустите план.

### Отчёты и документация
Все отчёты, скриншоты и документация хранятся в папке docs.
