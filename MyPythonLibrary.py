def cash_machine():
    p = True
    # Cash machine program that return exact change for float amount entered 
    while p != 0:
         p = eval(input("Enter cash amount or Zero to Quit: "))
         if p == 0:
              continue
         cash = ""
         if p >= 100: 
              cash = str(int(p // 100)) + " - $100, "
              p -= (p // 100) * 100
         if p >= 50: 
             cash += str(int(p // 50)) + " - $50, "
             p -= (p // 50) * 50
         if p >= 20: 
             cash += str(int(p // 20)) + " - $20, "
             p -= (p // 20) * 20
         if p >= 10: 
             cash += str(int(p // 10)) + " - $10, "
             p -= (p // 10) * 10
         if p >= 5: 
             cash += str(int(p // 5)) + " - $5, "
             p -= (p // 5) * 5
         if p >= 1.00: 
             cash += str(int(p // 1.00)) + " - $1, "
             p -= (p // 1.00) 
         if p >= 0.25: 
             cash += str(int(p // 0.25)) + " - quarters, "
             p -= (p // 0.25) * 0.25
         if p >= 0.10: 
             cash += str(int(p // 0.10)) + " - 10 cents, "
             p -= (p // 0.10) * 0.10
         if p >= 0.05: 
             cash += str(int(p // 0.05)) + " - Dime, "
             p -= (p // 0.05) * 0.05
         # print (int (round (p * 100)))
         if p >= 0.01: 
             cash += str(int (round (p * 100))) + " - pennies"              
         print("Exact Cash is: ", cash)
    else:      
         print("From Cash Machine - Have a nice day")

def dice():
    # This program simulates the rolling of dice.
    import random

    # Constants for the minimum and maximum random numbers
    MIN = 1
    MAX = 6
 
    # Create a variable to control the loop.
    again = 'y'

    # Simulate rolling the dice.
    while again == 'y' or again == 'Y':
        print('Rolling the dice...')
        print('Their values are:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        # Do another roll of the dice?
        again = input('Roll them again? (y = yes): ')

def futureValue(p, r, m, t):
    # p  principal, the amount deposited
    # r  annual rate of interest in decimal form
    # m  number of times interest is compounded per year
    # t  number of years
    i = r / m   # interest rate per period
    n = m * t   # total number of times interest is compounded
    amount =  p * ((1 + i) ** n)
    return amount

## Find the future value for a saving account deposit
def MainFutureValue():
    p = eval(input("Enter amount deposited: "))
    r = eval(input("Enter annual rate of interest in decimal form: "))
    m = eval(input("Enter number of times interest is compounded per year: "))
    t = int(input("Enter number of years: "))
    balance = futureValue(p, r, m, t)
    print("Balance after", t, "years: ${0:,.2f}".format(balance))
         
