try:
    # Taking the user input and storing it in year variable.
    year = int(input('Enter year: '))
    # Logic for checking if the year is a LEAP YEAR or NOT.
    if year % 400 == 0:
        print("LEAP YEAR")
    elif year % 100 == 0:
        print("NOT LEAP YEAR")
    elif year % 4 == 0:
        print("LEAP YEAR")
    else:
        print("NOT LEAP YEAR")
except Exception:
    print("Invalid Input! Try Again!")
