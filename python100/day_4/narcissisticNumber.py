"""
Search for narcissistic numbers
Narcissistic number, also known as a super-perfect digital invariant,
self-love number, self-power number or Armstrong's number. It is a
three-digit number where the sum of each digit raised to the power of
three equals the original number. For example: $1^3 + 5^3+ 3^3=153$.
"""

nar_lst = []
for num in range(100, 1000):
    ones_place_num = num % 10
    tens_place_num = (num//10) % 10
    hundreds_place_num = num // 100
    if num == hundreds_place_num ** 3 + tens_place_num ** 3 + ones_place_num ** 3:
        nar_lst.append(num)

print(f"The narcissistic numbers is {nar_lst}.")
