#Create a hypotenuse.py program that asks the user for two numbers, a and b, and then calculates the hypotenuse c.
#The hypotenuse is the longest side of the right triangle.

side_a = float(input("Side A of the triangle: "))
side_b = float(input("Side B of the tiangle: "))

hypo_c = (side_a ** 2 + side_b ** 2) ** 0.5
print("The hypotenuse is:", hypo_c)