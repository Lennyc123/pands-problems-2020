#Input any positive integer 
# - Then output succcessive values of a calculation

#At each step calculate the next value by taking the current value and -
#If  - even divide by two,
#else -  odd multiply by 3 and add 1

#End program if current value is 1

x = int(input("Enter any positive integer:"))
while x != 1:
    if x % 2 == 0:
        print(round(x))
        x = x / 2
    #elif x % 2 != 0:
    else:
        print(round(x))
        x = x * 3 + 1
print("1")
        

