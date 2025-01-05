#Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

co_pesos = int(input("What do you have left in pesos? "))
pe_soles = int(input("What do you have left in soles? "))
br_reais = int(input("What do you have left in reais? "))

conversion_to_usd = (co_pesos * 0.00023 + pe_soles * 0.27 + br_reais * 0.16167)
print("You have", conversion_to_usd, "USD dollars")