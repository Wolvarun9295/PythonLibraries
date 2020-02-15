# Creating a class MonthlyPay with a function monthlyPayment to calculate the Monthly Payment
class MonthlyPay:
    # monthlyPayment function takes principal amount, rate of interest,
    # time period of interest to be compounded and time period in years.
    def monthlyPayment(self, principal, rate, interestCompounded, timePeriod):
        # Calculating the Monthly Compound Interest.
        payment = principal * ((1 + (rate / interestCompounded)) ** (interestCompounded * timePeriod))
        return payment


try:
    # Taking the principal, rate of interest,
    # time period of interest to be compounded in months and time period in years.
    principal = int(input('Enter the Principal amount: Rs.'))
    rate = float(input('Enter the Interest Rate: ')) / 100
    interestCompounded = float(input('Enter Time Period of Interest to be Compounded in Months:'))
    timePeriod = float(input('Enter the Time Period in Years: '))
    # Creating an object payment of class MonthlyPay.
    payment = MonthlyPay()
    # Calling the monthlyPayment function by using the object payment.

    print(
        f'The monthly payment is: Rs.{round(payment.monthlyPayment(principal, rate, interestCompounded, timePeriod), 2)}')

except:
    print('Invalid Input! Try Again!')
