# Initializing a list of numbers.
numbers = [45, 15, 30, 23, 67]
# Initializing variables.
divisor = 15
remainder = 1
# Initializing a blank list.
dividedNumbers = []
# Using anonymous function to check which numbers are divisible by 15.
for i in numbers:
    remainder = lambda a: i % a
    if remainder(divisor) == 0:
        dividedNumbers.append(i)
print(f'The numbers divided by {divisor} are {dividedNumbers}')
