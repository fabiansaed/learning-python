#Create a bmi.py program that calculates your own BMI.
#The body mass index (BMI) it's used by health and nutrition professionals to estimate human body fat in certain populations.
#It is computed by taking an individual's weight (mass) in kilograms and dividing it by the square of their height in meters.

mass_kg = 80
height_mts = 1.83

my_bmi = mass_kg / (height_mts ** 2) #Obtaining the square of the height
print("My Body Mass Index is:", my_bmi)