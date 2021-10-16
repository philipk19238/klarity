FROM python:3

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /app
COPY app app
WORKDIR /app
