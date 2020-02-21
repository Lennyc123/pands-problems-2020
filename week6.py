# $ python squareroot.py
# Please enter a positive number: 14.5
# The square root of 14.5 is approx. 3.8.

# Program that takes positive floating-point number as input
# Outputs approximation of its square root.
# Create function called sqrt

#Algorithm approximate root = x_i
# Add the approximate root with the original number divided by the approximate root and divide by 2.
# x_i := (x_i + n / x_i) / 2

x = float(input("Enter any positive decimal number"))

def sqrt(x):
    xr = x 
    return (xr + x / xr) / 2
    #while xr < x:
        #(xr + x / xr) / 2
    
print("The square root of" , x , "is approx." , sqrt(x))