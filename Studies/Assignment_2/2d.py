# Write a program in python to insert entries in above created table using mysql.

import mysql.connector as mysql
from password import passreturn

try:
    db = mysql.connect(host="localhost", username="root", passwd=passreturn(), port=3306, database="stud_python")

    cursor = db.cursor()

    if db:
        print("Connected")

    def exe_fetch(query):
        cursor.execute(query)
        print(cursor.fetchall())

    q1 = """insert into employee(emp_name,emp_dept,emp_gender,emp_sal,emp_age)
    values('Siddhant','IT','Male',150000,24);"""
    q2 = """insert into employee(emp_name,emp_dept,emp_gender,emp_sal,emp_age)
    values('Rajak','IT','Male',100000,26);"""
    q3 = """insert into employee(emp_name,emp_dept,emp_gender,emp_sal,emp_age)
    values('Shivam','IT','Male',100000,25);"""

    my_t = (q1, q2, q3)

    for i in my_t:
        cursor.execute(i)

    exe_fetch("""select * from employee;""")

    db.commit()

except Exception as e:
    print(e)