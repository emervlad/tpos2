#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $service1_host $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python3 app.py

exec "$@"