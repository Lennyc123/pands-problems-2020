import datetime
x = datetime.datetime.now()

if x.weekday() < 5:
    print("Yes, unfortunately today is a weekday.")
elif x.weekday() > 4:
    print("It is the weekend, yay!")
