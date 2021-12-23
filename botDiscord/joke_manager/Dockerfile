FROM python:3.8-slim AS base
RUN apt-get update && apt-get install --no-install-recommends --yes python3

RUN pip install mysql.connector
RUN pip install pika

ENV PYTHONUNBUFFERED 1

ARG DATABASE_IP1
ENV DATABASE_IP1 $DATABASE_IP1

COPY ./create_joke_database.py ./create_joke_database.py
COPY ./jmanager.py ./jmanager.py

CMD ["python", "jmanager.py"]