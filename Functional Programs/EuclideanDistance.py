import math

try:
    # Taking the x2 and y2 coordinates respectively from the user.
    x2 = int(input('Enter the x coordinate: '))
    y2 = int(input('Enter the y coordinate: '))
    # Initializing the origin coordinates x1 and y1.
    x1 = 0
    y1 = 0
    # Calculating the Euclidean Distance from the points to the origin.
    euclideanDistance = math.sqrt((math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2)))
    print(f'The Euclidean Distance from point {x2, y2} to the origin {x1, y1} is {euclideanDistance}')
except Exception:
    print("Error! Try Again!")
