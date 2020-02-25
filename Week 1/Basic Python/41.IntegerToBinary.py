# Taking user input.
integer = int(input('Enter the integer value: '))
# Copying the integer into another variable for further printing purpose.
forPrint = integer
# Taking number of zeros input for adding the leading zeros to our output.
zeros = int(input("Enter the number of leading zero's you want: "))
# Initializing two variables.
remainder1 = 0
remainder2 = 1
# Initializing a blank list.
binary = []
# Logic to get the binary output.
while integer != 0:
    if integer % 2 == remainder1:
        integer = integer // 2
        binary.append(remainder1)
    elif integer % 2 == remainder2:
        integer = integer // 2
        binary.append(remainder2)
# Reversing the output to get the proper result.
binary.reverse()
print(f'The binary equivalent of {forPrint} is: ', end='')
# Initializing a blank string for adding leading zeros.
zeroFiller = " "
# Printing the leading zeros as follow.
print(zeroFiller.zfill(zeros + len(zeroFiller)), end='')
# Printing the rest of the result.
for digits in binary:
    print(digits, end=' ')
