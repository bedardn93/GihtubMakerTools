FROM python:3.10.4-slim-buster

RUN apt update

# Create app directory
WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

# Avoiding repeated reinstalls upon making unrelated code changes.
COPY . .

ENTRYPOINT [ "python", "main.py" ]
