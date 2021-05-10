import mysql.connector as mysql
import random
from password import passreturn

try:

    db = mysql.connect(host="localhost", user="root", passwd=passreturn(), database="test")

    print(db)

    cursor = db.cursor()

    select = """SELECT * FROM rawflight2;"""

    deptPlace = ["DELHI DEL", "NAGPUR NAG", "BOMBAY BOM", "HYDERABAD HYD", "GOA GOI", "PUNE PNQ", "NASHIK ISK"]

    arrPlace = deptPlace[::-1]

    flightNo = 20
    airline = "Air India"
    seatingClass = "E"
    stops = 0

    for i in range(1, 25):
        deptTime = random.randint(2, 20)
        columnNumber = 40000 + i - 1
        day = i
        daysFly = random.randint(1, 100)
        randomDeptPlace = deptPlace[random.randint(0, len(deptPlace) - 1)]
        randomArrPlace = arrPlace[random.randint(0, len(arrPlace) - 1)]
        fare = f"{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}"
        seatsAvailable = random.randint(2, 7)
        duration = "2h 0m"
        if randomDeptPlace != randomArrPlace:
            query = f"Insert into rawflight2 values({columnNumber},'2021-6-{day}','2021-6-{day}',{daysFly},'{randomDeptPlace}','{randomArrPlace}','{deptTime}:00','{deptTime+2}:00',{flightNo},'{airline}',{fare},{seatsAvailable},'{seatingClass}','{duration}',0,'','' )"
            cursor.execute(query)

        print(query)
        print(f"Inserted {i} times!")

    # cursor.execute(select)
    # print(cursor.fetchall())

    db.commit()
except Exception as e:
    print(e)
finally:

    db.close()
