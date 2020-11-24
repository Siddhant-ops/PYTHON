# Write a program in python to update entries in above created table using mysql.

import mysql.connector as mysql
from password import passreturn

try:
    db = mysql.connect(host="localhost", username="root", passwd=passreturn(), database="stud_python")

    if db:
        print("Connected")

    cursor = db.cursor()

    def exe_fetch(query):
        cursor.execute(query)
        print(cursor.fetchall())

    q1 = """delete from employee where emp_sal=10000000;"""
    q2 = """delete from employee where emp_sal=9000000;"""
    q3 = """delete from employee where emp_sal=8000000;"""

    my_t = (q1, q2, q3)

    for i in my_t:
        cursor.execute(i)

    exe_fetch("""select * from employee;""")

    print("Entries Deleted")

    db.commit()

    db.close()

except Exception as e:
    print(e)