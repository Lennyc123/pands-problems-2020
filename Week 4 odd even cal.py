#The following program promts a user to input any positive integer
# - then outputs the successive values of the following calculation

# If - even, divide by 2
# otherwise (else) odd - multiply by 3 and add 1.

# The program is then set to end if the current value is one.

x = int(input("Enter any positive integer:")) # User is prompted to input any positive integer
while x != 1: # While loop will end upon reaching 1.
    if x % 2 == 0: # Provides a sequence on what to do if the calculation is even. i.e. is divisable by 2 or leaves no remainder
        print(round(x)) # value of x is displayed for the user and is rounded.
        x = x / 2 # the value of x is divided by 2
    #elif x % 2 != 0: # explanation of what the else command is calculating. i.e. if the number cannot be divided by 2 equally, it is odd.
    else:
        print(round(x)) # value of x is displayed for the user and is rounded.
        x = x * 3 + 1 # value of x is multiplyed by 3 and 1 is added.
print("1") # value of 1 is printed.
        

