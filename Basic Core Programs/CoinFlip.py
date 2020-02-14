import random

try:
    # Taking input from the user.
    flip = int(input('Enter number of times a coin is to be flipped: '))
    # Initializing heads and tails to store the random values generated from the random function.
    heads = 0
    tails = 0
    # Logic to check if the random number generated is > 0.5 or < 0.5.
    # If the random number is < 0.5 then the tails gets incremented else the heads gets incremented.
    if flip > 0:
        for num in range(flip):
            if random.random() < 0.5:
                tails += 1
            else:
                heads += 1
        # Printing the random generated values of heads and tails
        print(str(heads) + ' Heads')
        print(str(tails) + ' Tails')
        # Calculating the percentage of heads and tails.
        hPercent = (heads / flip) * 100
        tPercent = (tails / flip) * 100

        print(f"Percentage of Heads vs Tails is: {hPercent} Heads, {tPercent} Tails")
    else:
        print("Invalid input!")
except Exception:
    print("Error! Try Again!")
