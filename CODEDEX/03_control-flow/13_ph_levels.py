#Create a ph_levels.py program that checks whether a pH level is basic, acidic, or neutral.
#If ph is greater than 7, output "Basic".
#If ph is less than 7, output "Acidic".
#Else, output "Neutral".

ph = float(input("What is the pH value? "))

if ph > 7:
    print("Basic")
elif ph < 7:
    print("Acidic")
else:
    print("Neutral")