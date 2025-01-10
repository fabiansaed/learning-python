#The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to.

#Defining houses
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

#Question 1
question1 = int(input("Q1. Do you like Dawn or Dusk? \n1) Dawn \n2) Dusk \n"))

if question1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif question1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input")

#Question 2
question2 = int(input("Q2. When I'm dead, I want people to remember me as: \n1) The Good \n2) The Great \n3) The Wise \n4) The Bold \n"))

if question2 == 1:
    hufflepuff += 2
elif question2 == 2:
    slytherin += 2
elif question2 == 3:
    ravenclaw += 2
elif question2 == 4:
    gryffindor += 2
else:
    print("Wrong input")

#Question 3
question3 = int(input("Q3. Which kind of instrument most pleases your ear? \n1) The violin \n2) The trumpet \n3) The piano \n4) The drum \n"))

if question3 == 1:
    slytherin += 4
elif question3 == 2:
    hufflepuff += 4
elif question3 == 3:
    ravenclaw += 4
elif question3 == 4:
    gryffindor += 4
else:
    print("Wrong input")

#Total points per house
print("Total points:" + "\n Gryffindor: ", gryffindor, "\n Ravenclaw: ", ravenclaw, "\n Hufflepuff: ", hufflepuff, "\n Slytherin: ", slytherin)

#The winner
if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
    print("Gryffindor 🦁  is the winner!")
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
    print("Ravenclaw 🦅  is the winner!")
elif hufflepuff >= slytherin:
    print("Hufflepuff 🦡  is the winner!")
else:
    print("Slytherin 🐍  is the winner!")