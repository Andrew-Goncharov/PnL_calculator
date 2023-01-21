# Проект: Calculator PnL 
### Описание

Программа выполняет вычисления PnL и Index PnL для доллара
(USD) относительно биткоина (BTC) за определенныи период, для
счета на торговой бирже Deribit.

### Схема проекта

![alt text](https://github.com/Andrew-Goncharov/PnL_calculator/blob/main/PnL_calculator/web/static/assets/img/img.png)

- PnL_calculator - основная директория проекта;
  - application - директория с обработчиками и дополнительными функциями;
  - database - директория со схемой базы данных и функциями ORM SQLAlchemy;
- migrations - директория, содержащая ресурсы инструмента управления миграциями alembic;

### Команды для запуска и настройки

- <code> docker-compose up -d --build </code> - сборка и запуск проекта 

- <code> docker logs --tail 50 --follow --timestamps dev_backend </code> -  просмотр логов контейнера с основным приложением

- <code> docker logs --tail 50 --follow --timestamps dev_db </code> - просмотр логов контейнера с базой данных 
