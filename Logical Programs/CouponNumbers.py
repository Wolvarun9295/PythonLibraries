# Importing random module to generate random numbers.
import random


# Defined a function randomCoupon in a class CouponGenerator to generate the unique random coupon numbers.
class CouponGenerator:
    # The function randomCoupon takes number of values as parameter.
    def randomCoupon(self, numberOfValues):
        # Initializing a blank list to be filled by random coupon numbers.
        uniqueCoupon = []
        # Logic for generating unique random coupon numbers.
        for i in range(numberOfValues):
            randomNumber = random.randrange(10000, 20000)
            if randomNumber not in uniqueCoupon:
                uniqueCoupon.append(randomNumber)
        print(uniqueCoupon)


# Taking user input of the N number of coupons to be generated.
numberOfValues = int(input('Enter your coupon number: '))
# Creating object generate of class CouponGenerator.
generate = CouponGenerator()
# Calling the randomCoupon function by passing the numberOfValues as parameter.
generate.randomCoupon(numberOfValues)
