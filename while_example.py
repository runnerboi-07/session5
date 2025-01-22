# You have 3 lives, you roll a dice, if you get a 6 you win
# If you do not get a 6, you lose 1 life
from random import randint

lives = 3
while True: # As long as I have more lives
    # Roll the dice
    dice = randint(1, 6)
    if dice == 6:
        print("You rolled a 6! You win!")
        break
    lives = lives - 1
    print("You rolled a", dice, "you have", lives, "left")
    if lives == 0:
        print("You lose!")
        break