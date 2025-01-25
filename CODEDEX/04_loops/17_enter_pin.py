#Before we dive deep into while loop, let's see a demo using a bank's ATM. 🏦

print("FABIAN\'S BANK")

pin = int(input("Enter your PIN: "))

while pin != 1234:
    pin = int(input("Incorrect PIN. Enter your PIN again: "))

if pin == 1234:
    print("Correct PIN!")