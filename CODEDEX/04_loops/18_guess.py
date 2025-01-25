#Run the code a few times so that you understand what it does.

guess = 0
tries = 0

while guess != 6 and tries < 4:
    guess = int(input("Guess the number: "))
    tries += 1

if guess != 6:
    print("You have no more attempts")
else:
    print("You got it!")