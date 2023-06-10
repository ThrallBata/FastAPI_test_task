FROM python:3.11

RUN mkdir /fastapi_app

# установить каталог для приложения
WORKDIR /fastapi_app

# копировать все файлы в контейнер
COPY . .

RUN pip install poetry
# установка зависимостей
RUN poetry install

RUN chmod a+x docker/*.sh
