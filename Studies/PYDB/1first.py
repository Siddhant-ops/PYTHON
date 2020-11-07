## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql
from password import passreturn

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(host="localhost", user="root", passwd=passreturn(), port="3306")

print(db)  # it will print a connection object if everything is fine

cursor = db.cursor()

print(cursor.execute("select version();"))
print(cursor.fetchall())

cursor.execute("SHOW DATABASES")

print(cursor.fetchone())

databases = cursor.fetchall()

print(databases)

for dbs in databases:
    print(dbs)


print('\n==================================================\n')


query = """
select version();
SHOW DATABASES
"""

cursor.execute(query)
print(cursor.fetchall())

db.close()
