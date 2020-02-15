# Defining the function newtonRaphson that takes number and numberOfIterations as parameters.
def newtonRaphson(number, numberOfIterations):
    # Storing the number in newNumber variable in float form to get decimal value.
    newNumber = float(number)
    # Logic for calculating root.
    for i in range(numberOfIterations):
        number = 0.5 * (number + newNumber / number)
    return number


# Taking input from the user.
number = int(input('Enter the number to find the root: '))
numberOfIterations = int(input('Enter the number of iterations: '))
print(f'The root of {number} is: {round(newtonRaphson(number, numberOfIterations), 5)}')
