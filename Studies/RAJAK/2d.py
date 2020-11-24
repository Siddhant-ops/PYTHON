import mysql.connector

try:
    conn = mysql.connector.connect(host="localhost", username="root", passwd="toor", port="3306", database="python")

    cursor = conn.cursor()

    q1 = """insert into employee(emp_id,emp_name,emp_dept,emp_gender,emp_sal,emp_age)
    values(1,'Rajak','IT','male',50000,27);"""
    q2 = """insert into employee(emp_id,emp_name,emp_dept,emp_gender,emp_sal,emp_age)
    values(2,'Sid','CS','male',10000,24);"""
    q3 = """insert into employee(emp_id,emp_name,emp_dept,emp_gender,emp_sal,emp_age)
    values(3,'Shivam','CSIT','Female',1000,25);"""
    q4 = """insert into employee(emp_id,emp_name,emp_dept,emp_gender,emp_sal,emp_age)
    values(4,'Sarosh','IT','Female',100,25);"""
    q5 = """insert into employee(emp_id,emp_name,emp_dept,emp_gender,emp_sal,emp_age)
    values(5,'Elon Musk','IT','Female',10,25);"""

    cursor.execute(q1)
    cursor.execute(q2)
    cursor.execute(q3)
    cursor.execute(q4)
    cursor.execute(q5)

    q4 = """select * from employee;"""
    cursor.execute(q4)

    print(cursor.fetchall())

    conn.commit()

    conn.close()

except Exception as e:
    print(e)
