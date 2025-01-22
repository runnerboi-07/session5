name = input("What is your name? \n")
print("Hello", name)
age = input("How old are you? \n")

try:
    age = int(age) # I am converting it to a number
    # new_age = age / 0
except ValueError:
    print("You are trying to trick me")
    print("Better luck next time")
except ZeroDivisionError:
    print("You cannot divide by zero")
except:
    print("Something unexpected happened")
else: # This happens if no error occurred
    print("You were probably born in", 2024 - age)
finally:
    print("Thanks for playing")