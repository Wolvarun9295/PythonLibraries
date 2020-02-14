# Importing the time module for doing time related work.
import time

print('''
    Choose the state:
    1. Start (S)
    2. Stop (X)
    ''')
# Initializing state variable for getting the Stopwatch state.
state = ""
# The isStarted variable checks if the Stopwatch is already started.
isStarted = False
# The switch variable checks the Stopwatch was started or not.
switch = False
# Logic for Stopwatch.
while state != "X":
    state = input('> ')
    if state.upper() == "S":
        if isStarted:
            print('Stopwatch already started!')
        else:
            isStarted = True
            print('Stopwatch Started...')
            # Rounding and getting the time in seconds by using modulus 60.
            # NOTE: The time in minutes can be obtained by dividing the time with 60.
            start = round(time.time() % 60)
            print(f'Started at: {start} seconds')
            switch = True

if not isStarted:
    print('Stopwatch already stopped!')
else:
    isStarted = False
    stop = round(time.time() % 60)
    print(f'Stopped at: {stop} seconds')
    print('Stopwatch Stopped!')
# Calculating the time elapsed between the start time and stop time.
if switch:
    timeElapsed = (stop - start)
    print(f'The elapsed time between {start} seconds and {stop} seconds is: {timeElapsed} seconds!')
elif not switch:
    print('Stopwatch not started!')
