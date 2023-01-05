import datetime

# now we will create an object of time

# The following method is with args (hours, minutes)

# if we pass no args the default time is 00:00:00

mytime = datetime.time(2, 30, 55, 41)

print((mytime))

print("\n================================================================================================\n")

print(mytime.hour)

print("\n================================================================================================\n")

print(mytime.minute)

print("\n================================================================================================\n")

print(type(mytime))

print("\n================================================================================================\n")

today = datetime.date.today()

print(today)

print("\n==================================================\n")

print(today.ctime())

print("\n================================================================================================\n")

from datetime import datetime

mydatetime = datetime(2021, 10, 3, 14, 20, 1)

print(mydatetime)

print("\n================================================================================================\n")

# DATE

from datetime import date

date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)

# we can perform arithmatic operation on date now

result = date1 - date2

print(result)

print("\n==================================================\n")

print(type(date1 - date2))

print("\n================================================================================================\n")

print(result.days)

print("\n================================================================================================\n")

datetime1 = datetime(2022, 11, 3, 22, 0)
datetime2 = datetime(2021, 11, 3, 12, 0)

mydiff = datetime1 - datetime2

print(mydiff)

print("\n==================================================\n")

# total_seconds show how many seconds in total with respect to year, days, and minutes

print(mydiff.total_seconds())

print("\n==================================================\n")

print(mydiff.seconds)
