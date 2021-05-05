FROM python:3.9

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt

WORKDIR /app

ENV MODE=runserver
ENV PYTHONPATH "/app/.env"

COPY . .