# 石头剪刀布游戏

from random import randint

num_computer = randint(1,3)
num_user = int(input("Options: 1:Rock; 2:Paper; 3:Scissor\nYour Chioces:  "))

if (num_computer == 1 and num_user == 3) or (num_computer == 2 and num_user == 1) or (num_computer == 3 and num_user == 1):
    print("Computer WIN !!!")
elif num_computer == num_user:
    print("Deuce.")
else:
    print("You WIN !!! Good job.")