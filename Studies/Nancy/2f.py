import mysql.connector as mysql
try:
    db = mysql.connect(host="localhost", username="root", passwd=, database="python")

    cursor = db.cursor()

    q1 = """delete from employee where emp_sal=10000000;"""
    q2 = """delete from employee where emp_sal=9000000;"""
    q3 = """delete from employee where emp_sal=8000000;"""

    cursor.execute(q1)
    cursor.execute(q2)
    cursor.execute(q3)

    cursor.execute("""select * from employee;""")

    print(cursor.fetchall())

    print("Entries Deleted")

    db.commit()

    db.close()

except Exception as e:
    print(e)