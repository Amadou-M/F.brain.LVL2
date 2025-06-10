FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

RUN pip install poetry==1.8.3

COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --only main --no-interaction --no-ansi

COPY . /app

COPY wait-for-db.sh /app/wait-for-db.sh
# Ensure the wait-for-db.sh script is executable
RUN chmod +x /app/wait-for-db.sh

EXPOSE 8000

CMD ["./wait-for-db.sh", "poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "server_config.wsgi:application"]
