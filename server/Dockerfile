FROM python:3.10.0-alpine

WORKDIR /usr/src/server

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements_dev.txt .
RUN pip install -r requirements_dev.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/server/entrypoint.sh
RUN chmod +x /usr/src/server/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/server/entrypoint.sh"]
