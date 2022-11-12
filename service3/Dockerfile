FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install psycopg2-binary==2.9.5 flask==2.2.2

COPY ./app .

CMD python3 -m flask run --host=0.0.0.0 --port=${web_port_internal}