import mysql.connector as mysql
from password import passreturn

try:

    db = mysql.connect(host="localhost", user="root", passwd=passreturn())

    if db:
        print("Connected")

    def exe_fetch(query):
        cursor.execute(query)
        print(cursor.fetchall())

    cursor = db.cursor()

    cursor.execute("CREATE DATABASE class")

    cursor.execute("use class")

    select = """SELECT * FROM student;"""

    q1 = """DROP TABLE IF EXISTS student"""

    q2 = """
    create table student
    (
    Name char(10),
    Roll_Number varchar(8),
    Age int,
    Marks int,
    Grade varchar(4)
    );
    """

    q3 = """insert into student(Name,Roll_Number,Age,Marks,Grade)
    values('Siddhant','SDIT003A',17,625,"A+");"""
    q4 = """insert into student(Name,Roll_Number,Age,Marks,Grade)
    values('Rajak','SDIT017A',19,615,"A");"""
    q5 = """insert into student(Name,Roll_Number,Age,Marks,Grade)
    values('Shivam','SDIT060A',19,605,"A");"""

    my_t = (q1, q2, q3, q4, q5)

    for i in my_t:
        cursor.execute(i)

    exe_fetch(select)

    db.commit()

except Exception as e:
    print(e)
finally:
    db.close()
