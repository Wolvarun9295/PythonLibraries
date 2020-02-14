try:
    # Taking user input and storing it in number variable.
    number = int(input('Enter a number: '))
    # Logic for finding out the Prime Factors of the number.
    if number == 0:
        print("Invalid Input!")
    elif number == 1:
        print(number)
    else:
        # Here the for loop starts from 2 since the first Prime number is 2 till the number + 1
        # because Python for loop considers number variable as 1 less than the number.
        for i in range(2, number + 1):
            # This while loop checks if the number is Prime or Not.
            while number % i == 0:
                print(i)
                # This line divides the number with the i and stores it in the number itself for further calculation.
                number = number // i

except Exception:
    print("Invalid Input! Try Again!")
