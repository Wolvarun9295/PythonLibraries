# adder function with parameters of numbers list and size of list has been made to ease the process.
def adder(numbers, size):
    for i in range(0, size - 2):
        for j in range(i + 1, size - 1):
            for k in range(j + 1, size):
                if numbers[i] + numbers[j] + numbers[k] == 0:
                    print(f'{numbers[i]} + {numbers[j]} + {numbers[k]} == 0')
                    print('Triplets found!')
                else:
                    print(f'{numbers[i]} + {numbers[j]} + {numbers[k]} != 0')
                    print('No Triplets available!')


try:
    # Taking the size of list as user input.
    size = int(input('Enter size of list: '))
    # Initializing a blank list for getting the elements from user.
    numbers = []
    # This for loop prompts user to input the values to store in the numbers list.
    for i in range(0, size):
        item = int(input('> '))
        numbers.append(item)
    # The adder function send the numbers list and size for further processing.
    adder(numbers, size)
except Exception:
    print('Invalid Input! Try Again!')
