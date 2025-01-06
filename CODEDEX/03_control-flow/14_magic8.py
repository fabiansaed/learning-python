#Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.

#Importing random module to generate a random number from a range
import random

#Saving the random number in a variable
random_number = random.randint(1, 9)

#Catching the user question. Just a simulation haha
question = input("Question: ")

#Answering according the random number
if random_number == 9:
    answer = "Yes - definitely"
elif random_number == 8:
    answer = "It is decidedly so"
elif random_number == 7:
    answer = "Without a doubt"
elif random_number == 6:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 4:
    answer = "Better not tell you now"
elif random_number == 3:
    answer = "My sources say no"
elif random_number == 2:
    answer = "Outlook not so good"
else:
    answer = "Very doubtful"

print("Magic 8 Ball say... " + answer)