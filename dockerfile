FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry

RUN poetry config virtualenvs.create false
<<<<<<< HEAD
RUN poetry install --without dev --no-interaction --no-ansi --no-root
=======
RUN poetry install --without dev --no-interaction --no-ansi
>>>>>>> 527d96cd208028a912e9a41439603fa78f7a25b3

COPY ./src ./src

CMD ["python", "./src/bot.py"]