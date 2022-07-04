FROM python:3.10.0-alpine

WORKDIR /usr/src/server

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache git

RUN pip install --upgrade pip
COPY ./requirements_dev.txt .
RUN pip install -r requirements_dev.txt

COPY . .
