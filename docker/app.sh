#!/bin/bash

pip install poetry

poetry install

poetry run alembic upgrade head

poetry run python main.py