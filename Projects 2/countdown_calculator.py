#take two dates as input,and then calculate the amount of time between them
from datetime import date

print("Enter  Start Date Details: ")
year_1 = int(input('Year: '))
month_1 = int(input('Month: '))
day_1 = int(input('Day: '))
startdate = date(year_1, month_1, day_1)

print("Enter End Date Details: ")
year_2 = int(input('Year: '))
month_2 = int(input('Month: '))
day_2 = int(input('Day: '))

enddate = date(year_2, month_2, day_2)
numstudydays = enddate - startdate

print (numstudydays)
