import mysql.connector as mysql
from password import passreturn

try:

    db = mysql.connect(host="localhost", user="root", passwd=passreturn(), database="test")

    print(db)

    cursor = db.cursor()

    select = """SELECT * FROM mydb;"""

    # q1 = """DROP TABLE IF EXISTS mydb"""
    # cursor.execute(q1)

    # q2 = """
    # create table flightRoutes
    # (
    # ID int NOT NULL Auto_Increment,
    # username varchar(20),
    # desg varchar(10),
    # sal varchar(20)
    # );
    # """
    # cursor.execute(q2)

    # q3 = """show databases;"""

    # q4 = """show tables;"""

    # q6 = """desc User_master;"""

    # t = (q3, q4, select, q6)

    def insertTable(name, gen, add, sal):
        return f"""insert into rawflight2(Ename, Egen, Eadd, Esal)
            values('{name}','{gen}','{add}',{sal});"""

    # for i in t:
    #     cursor.execute(i)

    #     print("\n==================================================\n")

    #     data = cursor.fetchall()
    #     if isinstance(data, list) and len(data) > 0:
    #         for j in data:
    #             print(j[0])

    # q7 = """insert into students(fname, lname, roll, age, marks)
    # values('Siddhant','Dalvi','sdit003a',18,550);"""

    # cursor.execute(q7)

    # cursor.execute(select)
    # print(cursor.fetchall())

    # q9 = """insert into students(fname, lname, roll, age, marks)
    # values('Python','JAVA','007',16,823);"""

    # cursor.execute(q9)

    # cursor.execute(select)
    # print(cursor.fetchall())

    # q10 = """insert into students(fname, lname, roll, age, marks)
    # values('Rajak','Ladaf','017',20,623);"""

    # cursor.execute(q10)

    # cursor.execute(select)
    # print(cursor.fetchall())


    deptPlace = ["NAG","BOM","HYD"]

    arrPlace = de

    db.commit()
except Exception as e:
    print(e)
finally:

    db.close()
