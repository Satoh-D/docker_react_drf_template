FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get -y upgrade
RUN pip install --upgrade pip
WORKDIR /works

COPY requirements.txt .
RUN pip install -r requirements.txt