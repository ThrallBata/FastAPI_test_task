# Тестовое задание REST-сервис на FastAPI

## Для запуска сервиса необходимо сделать, без docker:
0. Установить Python 3.11 и Postgres 14.
1. Клонировать репозиторий `git clone https://gitlab.com/ThrallBata/test-task-fastapi-rest.git`
2. Установить зависимости `poetry install`
3. Для облегчения запуска сервиса файл с переменными окружения **.env** уже в проекте нужно подредактировать, если пользуетесь другими портами или нестандартными данными Postgres.
4. Так как миграция уже присутсвует в репозитории, необходимо ее применить, чтобы создать таблицы в БД `poetry run alembic upgrade head` .
5. Можно запускать сервер `poetry run python main.py` , обязательно находиться в корневой папке.

## Для запуска сервиса необходимо сделать, с помощью docker:
0. Шаги 0 и 1 обязательны ☝.
1. Собираем проект `*sudo* docker-compose build` , **sudo** необходимо для Ubuntu.
2. Запускаем проект `*sudo* docker-compose up`
3. Сервер запущен. `http://0.0.0.0:1489/docs`

## Функционал
0. После запуска сервера перейти `http://0.0.0.0:выбранный порт/docs`
1. Создать пользователя в `/singup`
2. Получить токен в `/login/token`
3. Через /docs: авторизироваться через встроенный функционал "Authorize" и запросить информацию `/profile` 
 /// Через Postman: Получить информацию о юзере `/profile` с передачей токена в **Headers** с **key** 'Authorization' и **value** 'Bearer Токен'
