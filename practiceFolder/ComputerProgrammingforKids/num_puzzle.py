import random
secret_number = random.randint(1,99)
try_times = 0

print("Hello! My name is Pirate Roberts, and I have a number puzzle.")
print("Would you want to play a puzzle game? OK, You have 6 tries.")

while try_times <= 6:
    guess_number = int(input("Let's begin. Please guess a integer number: "))
    if guess_number < secret_number:
        print("Too low. Please try again. Give me another number: ")
    elif guess_number> secret_number:
        print("Too high. Please try again. Give me another number: ")
    try_times = try_times + 1

if guess_number == secret_number:
    print(f"You are correct. The number is {secret_number}. ")
else:
    print(f"No more guess. Wish you have a better luck!\nThe secret number is {secret_number}")



