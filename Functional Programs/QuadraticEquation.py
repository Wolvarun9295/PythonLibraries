# NOTE: The math module supplies mathematical functions on floating-point numbers,
# while the cmath module supplies equivalent functions on complex numbers.
import cmath
import math

try:
    # Taking the values of a, b and c from the user.
    valueOfa = int(input('Enter the value of a: '))
    valueOfb = int(input('Enter the value of b: '))
    valueOfc = int(input('Enter the value of c: '))
    # Calculating the discriminant.
    discriminant = (math.pow(valueOfb, 2)) - (4 * valueOfa * valueOfc)
    # Calculating the roots from the input values and the discriminant.
    root1 = (-valueOfb + cmath.sqrt(discriminant)) / (2 * valueOfa)
    root2 = (-valueOfb - cmath.sqrt(discriminant)) / (2 * valueOfa)

    print(f'The roots of Quadratic Equation ax^2 + bx + c are: {root1} and {root2}')
except Exception:
    print("Error! Try Again!")
