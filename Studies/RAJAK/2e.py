import mysql.connector as mysql

try:
    conn = mysql.connect(host="localhost", username="root", passwd="toor", port="3306", database="python")

    cursor = conn.cursor()

    q1 = """update employee set emp_name='abc',emp_gender='None' where emp_name='Rajak';"""
    q2 = """update employee set emp_name='efg',emp_gender='None' where emp_name='Sid';"""
    q3 = """update employee set emp_name='xyz',emp_gender='None' where emp_name='Shivam';"""

    cursor.execute(q1)
    cursor.execute(q2)
    cursor.execute(q3)

    q4 = """select * from employee;"""
    cursor.execute(q4)

    print(cursor.fetchall())

    conn.commit()

    conn.close()

except Exception as e:
    print(e)
