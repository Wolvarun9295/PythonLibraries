# Imported time module.
import time

print('Do you want the (D)irect time or you want to see it with (I)nterruption or you want to (Q)uit?: ')
inputThis = ""
while inputThis.upper() != "Q":
    inputThis = input('> ')
    if inputThis.upper() == "D":
        # Initializing the start time.
        startTime = time.time()
        # Printing the time of execution.
        print((time.time() - startTime))
    elif inputThis.upper() == "I":
        interrupt = int(input('Enter the time in secs: '))
        print("Interrupt Initailized...")
        startTime = time.time()
        time.sleep(interrupt)
        print((time.time() - startTime))
