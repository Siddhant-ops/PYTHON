import mysql.connector as mysql
from password import passreturn

try:

    db = mysql.connect(host="localhost", user="root", passwd=passreturn(), database="stud_python")

    print(db)

    cursor = db.cursor()

    select = """SELECT * FROM students;"""

    q1 = """DROP TABLE IF EXISTS students"""
    cursor.execute(q1)

    q2 = """
    create table students
    (
    id int NOT NULL AUTO_INCREMENT,
    fname char(10),
    lname char(15),
    roll varchar(8),
    age int,
    marks int,
    PRIMARY KEY (id)
    );
    """
    cursor.execute(q2)

    q3 = """show databases;"""

    q4 = """show tables;"""

    q6 = """desc students;"""

    t = (q3, q4, select, q6)

    for i in t:
        cursor.execute(i)
        data = cursor.fetchall()
        if isinstance(data, list) and len(data) == 5:
            for j in data:
                print(j[0])

    q7 = """insert into students(fname, lname, roll, age, marks)
    values('Siddhant','Dalvi','sdit003a',18,550);"""

    cursor.execute(q7)

    cursor.execute(select)
    print(cursor.fetchall())

    q9 = """insert into students(fname, lname, roll, age, marks)
    values('Python','JAVA','007',16,823);"""

    cursor.execute(q9)

    cursor.execute(select)
    print(cursor.fetchall())

    q10 = """insert into students(fname, lname, roll, age, marks)
    values('Rajak','Ladaf','017',20,623);"""

    cursor.execute(q10)

    cursor.execute(select)
    print(cursor.fetchall())

    db.commit()
except Exception as e:
    print(e)
finally:

    db.close()
