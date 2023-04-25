"""
Enter a positive integer to determine if it is a prime number.

Enter a positive integer to determine if it is a prime number.
"""
from math import sqrt 

input_num = int(input("Please enter a integer number: "))
end_num = int(sqrt(input_num))
is_prime = True
for i in range(2, end_num + 1):
    if input_num % end_num == 0:
        is_prime = False
        break
if is_prime and input_num != 1:
    print("Bingo, This is a prime number.")
else:
    print("Ops, Thisn't a prime numnber." )
