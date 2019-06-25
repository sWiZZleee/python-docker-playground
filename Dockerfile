FROM python:3.7-alpine

WORKDIR /app

COPY lib/ /app

COPY requirements.txt /app

RUN python buildMessage.py

