from random import choice
drinks = ["gin", "vodka", "whiskey", "rum", "tequila", "absinthe", "sake"]
# print(choice(drinks))
name = input("I am the virtual bartender. What is your name? \n")
try:
    age = input("What is your age? \n")
    age = int(age)
    country = input("What is your country \n")
    legal = False
    if age >= 21:
        legal = True
    elif age >= 18 and (country != "USA" and country != "UAE"):
        legal = True
    elif age >= 16 and country == "Luxembourg":
        legal = True
except ValueError:
    print("Do not play games with me")

# Outside the except
if legal:
    print("It's my pleasure to serve you", choice(drinks))
else:
    print("Dear", name, "unfortunately I cannot serve you")