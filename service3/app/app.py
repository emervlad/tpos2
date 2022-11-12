import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def bowels():
    host = os.environ['service1_host']
    database = os.environ['DB']
    user = os.environ['user']
    password = os.environ['password']

    conn = psycopg2.connect(host=host, database=database, user=user, password=password, port=5432)
    curs = conn.cursor()
    curs.execute("SELECT * FROM people;")

    js = [{"name": row[0], "age": row[1]} for row in curs.fetchall()]

    curs.close()
    conn.close()

    return jsonify({"data": js})


@app.route('/health')
def healthcheck():
    return jsonify({"status": "OK"})
