import mysql.connector as mysql

try:
    db = mysql.connect(host="localhost", username="root", passwd=, port=3306, database="python")

    cursor = db.cursor()

    q1 = """insert into employee(emp_id,emp_name,emp_dept,emp_gender,emp_sal,emp_age)
    values(1,'Nancy','IT','Female',15000,24);"""
    q2 = """insert into employee(emp_id,emp_name,emp_dept,emp_gender,emp_sal,emp_age)
    values(2,'Khanak','IT','Female',10000,26);"""
    q3 = """insert into employee(emp_id,emp_name,emp_dept,emp_gender,emp_sal,emp_age)
    values(3,'Shivani','IT','Female',10000,25);"""
    
    cursor.execute(q1)
    cursor.execute(q2)
    cursor.execute(q3)

    cursor.execute("""select * from employee;""")

    print(cursor.fetchall())

    db.commit()

    db.close()

except Exception as e:
    print(e)
