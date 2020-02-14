# Importing random module for generating random values.
import random

try:
    # Taking values from user.
    stake = int(input('Enter stake $: '))
    goal = int(input('Enter goal $: '))
    # Initializing win, lose and bets for further process.
    win = 0
    lose = 0
    bets = 0
    # Logic for virtual Gambler.
    while stake != 0:
        # As soon as the game starts, bets increase and stake decreases no matter what.
        bets += 1
        stake -= 1
        if stake == goal:
            print('Goal Reached!')
            break
        elif stake == 0:
            print('Stake Exhausted!')
            break
        else:
            # If the random number is less than 0.5, the Gambler loses and vice versa.
            if random.random() < 0.5:
                lose += 1
                stake -= 1
            else:
                win += 1
                stake += 2

    print(f'Bets played: {bets}')
    print(f'Times Won: {win} and Times Lost: {lose}')
    # Calculating the percentage of win and lose.
    winPercent = (win / bets) * 100
    losePercent = (lose / bets) * 100
    print(f'Percentage Win: {round(winPercent)}% and Lose: {round(losePercent)}%')

except Exception:
    print('Invalid Input! Try Again!')
