FROM python:3.10.4-slim-buster

RUN apt update

# Create app directory
WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt