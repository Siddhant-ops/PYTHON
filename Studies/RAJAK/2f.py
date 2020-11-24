import mysql.connector as mysql

try:
    conn = mysql.connect(host="localhost", username="root", passwd="toor", port="3306", database="python")

    cursor = conn.cursor()

    q1 = """delete from employee where emp_id=1;"""

    cursor.execute(q1)

    q4 = """select * from employee;"""
    cursor.execute(q4)

    print(cursor.fetchall())

    print("Entries Deleted")

    conn.commit()

    conn.close()

except Exception as e:
    print(e)
