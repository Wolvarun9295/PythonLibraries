# Imported date module from datetime pack.
from datetime import date

try:
    # Taking user input.
    year1 = int(input('Enter year: '))
    month1 = int(input('Enter month: '))
    date1 = int(input('Enter date: '))

    year2 = int(input('Enter year: '))
    month2 = int(input('Enter month: '))
    date2 = int(input('Enter date: '))
    # date takes input in form of (year,month,date)
    day2 = date(year2, month2, date2)
    day1 = date(year1, month1, date1)
    # Calculating number of days between the two inputs.
    days = day2 - day1
    print(abs(days.days))
except:
    print('Invalid Input! Try Again!')
