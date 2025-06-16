import datetime as dt

#Getting a datetime
now = dt.datetime.now()
year = now.year
month = now.month
hour = now.hour
week_day = now.weekday()
print(now)

#Creating a date time
date_of_birth = dt.datetime(year=1993, month= 12, day= 23, hour=4)
print(date_of_birth)