"""
Guess number
author:steve
"""

import random

answear = random.randint(1, 100)
count = 0
while True:
    count += 1
    guess_number = int(input("Enter a integer: "))
    if guess_number > answear:
        print("Too high, guess again.")
    elif guess_number < answear:
        print("Too low, guess again.")
    else:
        print("Bingo, You got it.")
        break
print(f"The answear is {answear}, You have used {count} times.")
if count > 7:
    print("But you need to work harder.")
