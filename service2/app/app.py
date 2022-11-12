import os
import psycopg2

host = os.environ['service1_host']
database = os.environ['DB']
user = os.environ['user']
password = os.environ['password']

conn = psycopg2.connect(host=host, database=database, user=user, password=password, port=5432)
curs = conn.cursor()

curs.execute("CREATE TABLE people (name varchar(40), age integer);")

f = open(r'/data/data.csv', 'r')
next(f)
curs.copy_from(f, 'people', sep=',', columns=('name', 'age'))

f.close()
conn.commit()

curs.execute("SELECT * FROM people;")

for row in curs.fetchall():
    print(row)

curs.close()
conn.close()
