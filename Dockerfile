FROM python:latest

WORKDIR /app

COPY . .

RUN apt-get update

RUN pip install Flask

CMD ["python3", "flaskEX.py"]
