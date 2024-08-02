FROM python:3.12.3-slim

RUN pip install poetry

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root --no-dev

COPY . /app/

CMD ["poetry", "run", "python", "src/main.py"]