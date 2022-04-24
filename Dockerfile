
FROM python:3.9-slim as build

RUN apt-get update

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD python3 manage.py