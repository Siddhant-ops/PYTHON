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

    q1 = """update employee set emp_name='Python',emp_dept='IT',emp_gender='None',emp_sal=10000000,emp_age='29' where emp_name='Siddhant';"""
    q2 = """update employee set emp_name='JAVA',emp_dept='IT',emp_gender='None',emp_sal=8000000,emp_age='29' where emp_name='Rajak';"""
    q3 = """update employee set emp_name='Python',emp_dept='IT',emp_gender='None',emp_sal=9000000,emp_age='29' where emp_name='Shivam';"""

    my_t = (q1, q2, q3)

    for i in my_t:
        cursor.execute(i)

    exe_fetch("""select * from employee;""")

    db.commit()

    db.close()

except Exception as e:
    print(e)