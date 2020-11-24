import mysql.connector as mysql

try:
    db = mysql.connect(host="localhost", username="root", passwd=, port="3306", database="python")

    cursor = db.cursor()

    q1 = """Drop table if exists employee"""

    cursor.execute(q1)

    q2 = """
    Create table employee
    (
    emp_id int,
    emp_name char(25),
    emp_dept char(10),
    emp_gender char(8),
    emp_sal int,
    emp_age int
    );
    """

    cursor.execute(q2)

    q3 = """desc employee;"""

    cursor.execute(q3)

    print(cursor.fetchall())

    db.close()

except Exception as e:
    print(e)
