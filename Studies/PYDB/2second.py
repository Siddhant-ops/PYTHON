import mysql.connector as mysql
from password import passreturn

db = mysql.connect(host="localhost", user="root", passwd=passreturn())

print(db)

cursor = db.cursor()

# cursor.execute("CREATE DATABASE STUD_PYTHON;")

cursor.execute("show databases")
dta = cursor.fetchall()

for i in dta:
    for j in i:
        print(j)
