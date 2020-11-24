import mysql.connector as mysql

try:
    db = mysql.connect(host="localhost", username="root", passwd=, database="python")

    cursor = db.cursor()

    q1 = """update employee set emp_id=1,emp_name='abc',emp_dept='IT',emp_gender='None',emp_sal=10000000,emp_age='9' where emp_name='Nancy';"""
    q2 = """update employee set emp_id=2,emp_name='efg',emp_dept='IT',emp_gender='None',emp_sal=8000000,emp_age='9' where emp_name='Khanak';"""
    q3 = """update employee set emp_id=3,emp_name='xyz',emp_dept='IT',emp_gender='None',emp_sal=9000000,emp_age='9' where emp_name='Shivani';"""

    cursor.execute(q1)
    cursor.execute(q2)
    cursor.execute(q3)

    cursor.execute("""select * from employee;""")

    print(cursor.fetchall())

    db.commit()

    db.close()

except Exception as e:
    print(e)
