# Declared a function toBinary in class DecimalToBinary.
class DecimalToBinary:
    # toBinary function takes decimalNumber as parameter for conversion process.
    def toBinary(self, decimalNumber):
        # Initializing a blank binary[] list for storing the binary values.
        binary = []
        # Logic for converting the decimal number to binary number.
        for i in range(decimalNumber):
            while decimalNumber != 0:
                # If when divided by 2 the remainder is 0, the output will be 0.
                if decimalNumber % 2 == 0:
                    # The output is appended in the blank list.
                    binary.append('0')
                    # The decimalNumber is further divided by 2.
                    decimalNumber = decimalNumber // 2
                # If when divided by 2 the remainder is 1, the output will be 1.
                elif decimalNumber % 2 == 1:
                    binary.append('1')
                    decimalNumber = decimalNumber // 2

        # The binary[] list stores the values as it gets, so we reverse the list to get the desired output.
        binary.reverse()
        return binary


try:
    # Taking decimal value as user input.
    decimal = int(input('Enter the decimal number: '))
    # Creating an object convert of class DecimalToBinary.
    convert = DecimalToBinary()
    # Calling the function toBinary with by using object convert of class DecimalToBinary.
    print(f'The Binary Equivalent of {decimal} is: {convert.toBinary(decimal)}')
except:
    print('Invalid Input! Try Again!')
