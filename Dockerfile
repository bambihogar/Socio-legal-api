FROM python:3.12.5-slim 

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

WORKDIR /app/api

CMD uvicorn main:application --host=0.0.0.0