# calender module imported for calender operations.
import calendar

try:
    # Taking user input.
    year = int(input('Enter year: '))
    month = int(input('Enter month: '))
    # Displaying the calender of given user input.
    cal = calendar.month(year, month)
    print(cal)
except:
    print('Invalid Input! Try Again!')
