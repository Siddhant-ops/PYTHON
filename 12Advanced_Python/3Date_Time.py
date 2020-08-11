import datetime

# now we will create an object of time

# The following method is with args (hours, minutes)

# if we pass no args the default time is 00:00:00

mytime = datetime.time(2, 30, 55, 41)

print((mytime))

print("================================================================================================")

print(mytime.hour)

print("================================================================================================")

print(mytime.minute)

print("================================================================================================")

print(type(mytime))

print("================================================================================================")

today = datetime.date.today()

print(today)

print("==================================================")

print(today.ctime())

print("================================================================================================")

from datetime import datetime

mydatetime = datetime(2021, 10, 3, 14, 20, 1)

print(mydatetime)

print("================================================================================================")

# DATE

from datetime import date

date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)

# we can perform arithmatic operation on date now

result = date1 - date2

print(result)

print("==================================================")

print(type(date1 - date2))

print("================================================================================================")

print(result.days)

print("================================================================================================")

datetime1 = datetime(2022, 11, 3, 22, 0)
datetime2 = datetime(2021, 11, 3, 12, 0)

mydiff = datetime1 - datetime2

print(mydiff)

print("==================================================")

# total_seconds show how many seconds in total with respect to year, days, and minutes

print(mydiff.total_seconds())

print("==================================================")

print(mydiff.seconds)
