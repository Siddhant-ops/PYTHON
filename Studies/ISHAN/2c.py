# Write a program in python to create table employee with columns as emp_id, emp_name, emp_dept, emp_gender,emp_sal and emp_age using mysql.

import mysql.connector as mysql
from password import passreturn  # P.S. A fruitfull function which returns my secret password

try:
    db = mysql.connect(host="localhost", username="root", passwd=passreturn(), port="3306", database="stud_python")

    if db:
        print("Connection established")

    cursor = db.cursor()

    def exe_fetch(query):
        cursor.execute(query)
        print(cursor.fetchall())

    q2 = """Drop table if exists employee"""

    cursor.execute(q2)

    q3 = """
    Create table employee
    (
    emp_id int NOT NULL AUTO_INCREMENT,
    emp_name char(25),
    emp_dept char(10),
    emp_gender char(8),
    emp_sal int,
    emp_age int,
    PRIMARY KEY (emp_id)
    );
    """

    cursor.execute(q3)

    q4 = """desc employee;"""

    exe_fetch(q4)

    db.close()

except Exception as e:
    print(e)
