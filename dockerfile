FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-interaction --no-ansi

COPY ./src ./src

CMD ["python", "./src/bot.py"]