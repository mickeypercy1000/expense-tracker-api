# Use Ubuntu as Operation System
FROM ubuntu:16.04

# Use python 3.8
FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1

WORKDIR /django_expense

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver", "127.0.0.1:8000"]

