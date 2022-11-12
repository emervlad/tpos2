FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install psycopg2-binary==2.9.5
RUN apt-get update && apt-get install -y netcat

COPY ./app .

ENTRYPOINT ["./entrypoint.sh"]