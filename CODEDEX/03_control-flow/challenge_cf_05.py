#🧑‍🚀 Planet Weights
#The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀
#Create a weight conversion program that: 1) Asks the user what their Earth weight is (as a float). 2) Asks the user for a planet number (as an int).
#Then, use an if/elif/else statement to calculate the user's weight on the destination planet.

earth_weight = float(input("What is your weight in the Earth? "))
planet = int(input("Which planet (1 to 7) is your destination? "))
destination_weight = 0

if planet == 1:
    planet = str("Mercury")
    destination_weight = earth_weight * 0.38
elif planet == 2:
    planet = str("Venus")
    destination_weight = earth_weight * 0.91
elif planet == 3:
    planet = str("Mars")
    destination_weight = earth_weight * 0.38
elif planet == 4:
    planet = str("Jupiter")
    destination_weight = earth_weight * 2.53
elif planet == 5:
    planet = str("Saturn")
    destination_weight = earth_weight * 1.07
elif planet == 6:
    planet = str("Uranus")
    destination_weight = earth_weight * 0.89
elif planet == 7:
    planet = str("Neptune")
    destination_weight = earth_weight * 1.14
else:
    print("Invalid planet number")

print("Your destination planet is " + planet)
print("Your destination weight is " + str(destination_weight))