try:
    # Taking the Nth term input from user.
    Nth_Term = int(input('Enter the Nth term: '))
    # Initializing the harmonicNumber variable to store the result.
    harmonicNumber = 0
    # Logic for calculating the Harmonic Number.
    if Nth_Term == 0:
        print('Enter a valid positive num!')
    else:
        for i in range(1, Nth_Term + 1):
            harmonicNumber += (1 / i)
        print(harmonicNumber)
except Exception:
    print("Error! Try Again!")
