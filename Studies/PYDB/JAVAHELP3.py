import mysql.connector as mysql
import random

from password import passreturn

deptPlace = ["DELHI DEL", "NAGPUR NAG", "BOMBAY BOM", "HYDERABAD HYD", "GOA GOI", "PUNE PNQ", "NASHIK ISK"]

arrPlace = deptPlace[::-1]

Airline = ["Air India", "Indigo", "AirAsia India", "GoAir", "Vistara", "TruJet"]

SeatClass = ["E", "B"]

try:

    db = mysql.connect(host="localhost", user="root", passwd=passreturn(), database="test")

    print(db)

    cursor = db.cursor()

    q1 = """CREATE TABLE RAWFLIGHT3(
        ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        DEPT_DATE VARCHAR(100),
        ORIGIN VARCHAR(100),
        DESTINATION VARCHAR(100),
        DEPT_TIME VARCHAR(100),
        ARR_TIME VARCHAR(100),
        FLIGHT_NO INT,
        AIRLINE VARCHAR(100),
        TOTAL_FARE VARCHAR(5),
        SEATS_AVAIL INT,
        SEATING_CLASS VARCHAR(2),
        DURATION VARCHAR(100)
    )"""
    # cursor.execute(q1)

    i = 0

    for year in range(2020, 2022):
        for month in range(1, 13):
            for day in range(1, 29):
                # print(f"{year}-{month}-{day}")
                duration = "2h 20m"

                if month < 10:
                    if day < 10:

                        for dp in deptPlace:
                            for ap in arrPlace:

                                if dp != ap:

                                    # randomDeptPlace = deptPlace[random.randint(0, len(deptPlace) - 1)]
                                    # randomArrPlace = arrPlace[random.randint(0, len(arrPlace) - 1)]
                                    deptTimeNo = random.randint(1, 20)
                                    deptTime = ""
                                    arrTimeNo = deptTimeNo + 2
                                    arrTime = ""
                                    flightNo = random.randint(1, 99)
                                    randomAirline = Airline[random.randint(0, len(Airline) - 1)]
                                    fare = f"{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}"
                                    seats = random.randint(1, 9)
                                    randomSeatClass = SeatClass[random.randint(0, len(SeatClass) - 1)]

                                    if deptTimeNo < 12:
                                        deptTime = f"{deptTimeNo}:20 AM"
                                    else:
                                        deptTime = f"{deptTimeNo}:20 PM"

                                    if arrTimeNo < 12:
                                        arrTime = f"{arrTimeNo}:40 AM"
                                    else:
                                        arrTime = f"{arrTimeNo}:40 PM"

                                    # print(
                                    #     f"values('{year}-0{month}-0{day}','{dp}','{ap}','{deptTime}', '{arrTime}', {flightNo}, '{randomAirline}','{fare}', {seats}, '{randomSeatClass}', '{duration}')"
                                    # )

                                    # query = f"Insert into rawflight3(DEPT_DATE,ORIGIN ,DESTINATION,DEPT_TIME,ARR_TIME ,FLIGHT_NO,AIRLINE ,TOTAL_FARE ,SEATS_AVAIL ,SEATING_CLASS,DURATION) values('{year}-0{month}-0{day}','{dp}','{ap}','{deptTime}', '{arrTime}', {flightNo}, '{randomAirline}','{fare}', {seats}, '{randomSeatClass}', '{duration}')"

                                    # cursor.execute(query)

                                    i += 1

                                else:
                                    print("Skipped")

                            # print(f"Date is : {year}-0{month}-0{day}  Flight No. is {flightNo}")
                            # query = f"Insert into rawflight3(DEPT_DATE,ORIGIN ,DESTINATION,DEPT_TIME,ARR_TIME ,FLIGHT_NO,AIRLINE ,TOTAL_FARE ,SEATS_AVAIL ,SEATING_CLASS,DURATION) values('{year}-0{month}-0{day}','{randomDeptPlace}','{randomArrPlace}','{deptTime}', '{arrTime}', {flightNo}, '{randomAirline}','{fare}', {seats}, '{randomSeatClass}', '{duration}')"
                            # cursor.execute(query)
                            # print(query)
                            # print(
                            #     f"values('{year}-0{month}-0{day}','{randomDeptPlace}','{randomArrPlace}','{deptTime}', '{arrTime}', {flightNo}, '{randomAirline}','{fare}', {seats}, '{randomSeatClass}', '{duration}')"
                            # )

                    else:

                        for dp in deptPlace:
                            for ap in arrPlace:

                                if dp != ap:

                                    # randomDeptPlace = deptPlace[random.randint(0, len(deptPlace) - 1)]
                                    # randomArrPlace = arrPlace[random.randint(0, len(arrPlace) - 1)]
                                    deptTimeNo = random.randint(1, 20)
                                    deptTime = ""
                                    arrTimeNo = deptTimeNo + 2
                                    arrTime = ""
                                    flightNo = random.randint(1, 99)
                                    randomAirline = Airline[random.randint(0, len(Airline) - 1)]
                                    fare = f"{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}"
                                    seats = random.randint(1, 9)
                                    randomSeatClass = SeatClass[random.randint(0, len(SeatClass) - 1)]
                                    if deptTimeNo < 12:
                                        deptTime = f"{deptTimeNo}:20 AM"
                                    else:
                                        deptTime = f"{deptTimeNo}:20 PM"

                                    if arrTimeNo < 12:
                                        arrTime = f"{arrTimeNo}:40 AM"
                                    else:
                                        arrTime = f"{arrTimeNo}:40 PM"

                                    print(
                                        f"values('{year}-0{month}-{day}','{dp}','{ap}','{deptTime}', '{arrTime}', {flightNo}, '{randomAirline}','{fare}', {seats}, '{randomSeatClass}', '{duration}')"
                                    )

                                    # query = f"Insert into rawflight3(DEPT_DATE,ORIGIN ,DESTINATION,DEPT_TIME,ARR_TIME ,FLIGHT_NO,AIRLINE ,TOTAL_FARE ,SEATS_AVAIL ,SEATING_CLASS,DURATION) values('{year}-0{month}-{day}','{dp}','{ap}','{deptTime}', '{arrTime}', {flightNo}, '{randomAirline}','{fare}', {seats}, '{randomSeatClass}', '{duration}')"

                                    # cursor.execute(query)

                                    i += 1
                                    # print(f"Date is : {year}-0{month}-0{day}  Flight No. is {flightNo}")
                                    # query = f"Insert into rawflight3(DEPT_DATE,ORIGIN ,DESTINATION,DEPT_TIME,ARR_TIME ,FLIGHT_NO,AIRLINE ,TOTAL_FARE ,SEATS_AVAIL ,SEATING_CLASS,DURATION) values('{year}-0{month}-{day}','{randomDeptPlace}','{randomArrPlace}','{deptTime}', '{arrTime}', {flightNo}, '{randomAirline}','{fare}', {seats}, '{randomSeatClass}', '{duration}')"
                                    # cursor.execute(query)
                                    # print(query)
                                    # print(
                                    #     f"values('{year}-0{month}-{day}','{randomDeptPlace}','{randomArrPlace}','{deptTime}', '{arrTime}', {flightNo}, '{randomAirline}','{fare}', {seats}, '{randomSeatClass}', '{duration}')"
                                    # )

                                else:
                                    print("Skipped")

                else:

                    for dp in deptPlace:
                        for ap in arrPlace:

                            if dp != ap:

                                # randomDeptPlace = deptPlace[random.randint(0, len(deptPlace) - 1)]
                                # randomArrPlace = arrPlace[random.randint(0, len(arrPlace) - 1)]
                                deptTimeNo = random.randint(1, 20)
                                deptTime = ""
                                arrTimeNo = deptTimeNo + 2
                                arrTime = ""
                                flightNo = random.randint(1, 99)
                                randomAirline = Airline[random.randint(0, len(Airline) - 1)]
                                fare = f"{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}"
                                seats = random.randint(1, 9)
                                randomSeatClass = SeatClass[random.randint(0, len(SeatClass) - 1)]
                                if deptTimeNo < 12:
                                    deptTime = f"{deptTimeNo}:20 AM"
                                else:
                                    deptTime = f"{deptTimeNo}:20 PM"

                                if arrTimeNo < 12:
                                    arrTime = f"{arrTimeNo}:40 AM"
                                else:
                                    arrTime = f"{arrTimeNo}:40 PM"

                                print(
                                    f"values('{year}-{month}-{day}','{dp}','{ap}','{deptTime}', '{arrTime}', {flightNo}, '{randomAirline}','{fare}', {seats}, '{randomSeatClass}', '{duration}')"
                                )

                                # query = f"Insert into rawflight3(DEPT_DATE,ORIGIN ,DESTINATION,DEPT_TIME,ARR_TIME ,FLIGHT_NO,AIRLINE ,TOTAL_FARE ,SEATS_AVAIL ,SEATING_CLASS,DURATION) values('{year}-{month}-{day}','{dp}','{ap}','{deptTime}', '{arrTime}', {flightNo}, '{randomAirline}','{fare}', {seats}, '{randomSeatClass}', '{duration}')"

                                # cursor.execute(query)

                                i += 1

                            else:
                                print("Skipped")

    db.commit()
except Exception as e:
    print(e)
finally:
    db.close()

print(i)
