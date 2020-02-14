# The following programe provides the user with an output that varies upon
# whether the program is run during the week or at the weekend

 
import datetime # "The datetime module supplies classes for manipulating dates and times." - docs.python.org - /module-datetime
x = datetime.datetime.now() # This Command is used to provide information on the datetime values attached to "today"

# datetime.weekday values range from 0-6, monday being 0, sunday being 6

if x.weekday() < 5: # if the output is within the range of values attached to the week days
    print("Yes, unfortunately today is a weekday.") # Then print this statement
elif x.weekday() > 4: # If the output is within the range of values attached to the weekend
    print("It is the weekend, yay!") # Then print this statement

    #References
    # https://docs.python.org/3/library/datetime.html#module-datetime
    # https://kite.com/python/docs/datetime.datetime.weekday
