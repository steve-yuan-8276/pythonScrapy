import easygui, random

greeting_words = """Hello There.
My name is Pirate Roberts, and I have a number puzzle.
Would you want to play a puzzle game?
"""
title_ynbox = "NUMBER PUZZLE"

if easygui.ynbox(greeting_words, title_ynbox):
    easygui.msgbox("OK, Let's play.\nIt's a secret number from 1 to 99.\nYou have 6 tries.")
else:
    easygui.msgbox("Bye.")
    sys.exit(0)

secret_number = random.randint(1,99)
try_times = 0
guess_number = easygui.integerbox(msg="Let's begin. Please guess a integer number: ", lowerbound=0, upperbound=99)
#print("Hello! My name is Pirate Roberts, and I have a number puzzle.")
#print("Would you want to play a puzzle game? OK, You have 6 tries.")

while try_times <= 6:
    if guess_number < secret_number:
        easygui.integerbox(msg="Too low. Please try again. Give me another number: ", lowerbound=0, upperbound=99)
    elif guess_number > secret_number:
        easygui.integerbox(msg="Too high. Please try again. Give me another number: ", lowerbound=0, upperbound=99)
    try_times = try_times + 1

if guess_number == secret_number:
    easygui.msgbox(f"You are correct. The number is {secret_number}. ")
else:
    easygui.msgbox(f"No more guess. Wish you have a better luck!\nThe secret number is {secret_number}")



