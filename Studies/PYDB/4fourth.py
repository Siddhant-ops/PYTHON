import mysql.connector as mysql
from password import passreturn

try:
    db = mysql.connect(host="localhost", user="root", passwd=passreturn(), database="stud_python")

    print(db)

    cursor = db.cursor()

    def exe_fetch(query):
        cursor.execute(query)
        print(cursor.fetchall())

    exe_fetch("""show tables;""")

    q1 = """show tables;"""
    cursor.execute(q1)
    tab_fetch = cursor.fetchall()

    table_name = ""

    for i in tab_fetch:
        table_name = i[0]

    print(table_name)

    exe_fetch(f"""desc {table_name};""")

    # exe_fetch(f"""select * from {table_name};""")

    # print("\n==================================================\n")

    # cursor.execute(
    #     f"""insert into {table_name}(fname,lname,roll,age,marks)
    # values('Shivam','Gupta','062',19,378);"""
    # )

    # cursor.execute(
    #     f"""insert into {table_name}(fname,lname,roll,age,marks)
    # values('Pythons','Javafg','001er',140,9949);"""
    # )

    # cursor.execute(
    #     f"""update {table_name} set fname='Amisha',lname='Gupta',roll='060',age=18,marks='398' where fname='Pythons';"""
    # )

    # exe_fetch(f"""select * from {table_name};""")

    # # cursor.execute(f"""update {table_name} set fname='Python',lname='JAVA',roll='001',age=10,marks='999' where id='2';""")

    # # exe_fetch(f"""select * from {table_name};""")

    # # exe_fetch(f"""select * from {table_name};""")

    # cursor.execute("""delete from students where fname='Shivam'""")
    # cursor.execute("""delete from students where fname='Amisha'""")

    exe_fetch('''select * from students;''')

except Exception as e:
    print(e)
finally:
    db.close()
