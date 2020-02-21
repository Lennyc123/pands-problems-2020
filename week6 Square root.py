# The following program takes a positive floating-point number as an input then,
# Outputs an approximation of its square root.

def sqrt(x): # Creation of a function named "sqrt" given the value x
    r = x # r = approximate root for the orginal value x
    precision = 10 ** (-10)

    while abs(x -r * r) > precision: # Continue until the difference in r is less than precision value
        r = (r + x / r) / 2 #Addition of the approximate root with the orginal input divided by r - result is then divided by 2. 

    return r # End execution of function and provides result

x = float(input("Enter any positive decimal number")) # User is prompted to provide an input
print("The square root of" , x , "is approx." , sqrt(x)) # Approximation of initial input is provided

# References
# "Defining and Using Functions" section of A Whirlwind Tour of Python by Jake Vanderplas.
# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# https://www.geeksforgeeks.org/python-return-statement/
