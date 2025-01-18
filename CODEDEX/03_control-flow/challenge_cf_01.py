#⭐️ Food Ratings
#In a five-star restaurant review system (⭐️⭐️⭐️⭐️⭐️), the stars typically represent the different levels of satisfaction.
#Make a rating system using an if/elif/else statement.

rating = float(input("Rate our restaurant: "))

if rating > 4.5:
    print("Extraordinary ⭐️⭐️⭐️⭐️⭐️")
elif rating > 4:
    print("Excellent ⭐️⭐️⭐️⭐️")
elif rating > 3:
    print("Good ⭐️⭐️⭐️")
elif rating > 2:
    print("Fair ⭐️⭐️")
else:
    print("Poor ⭐️")