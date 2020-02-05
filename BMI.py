#Programme for calculating ones BMI


weight = int(input("Enter weight:")) # User is promted to enter weight
height = int(input("Enter height:")) # User is promted to enter height

bmi = (weight / (height / 100) ** 2) # User inputs are utilised in order to calculate ones BMI

print(round(bmi,2)) # The (BMI) output value of the formula is rounded to 2 decimal places.