#Create a grades.py program that checks whether a grade is above or below 55.
#If grade is greater than or equal to 55, then print "You passed."
#Else, print "You failed."

import random

grade = random.randint(0, 100)

print("Your grade was: " + str(grade))

if grade >= 55:
    print("You passed!")
else:
    print("You failed!")