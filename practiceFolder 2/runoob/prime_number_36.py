# 题目：求任意正整数区间之内的素数

from math import sqrt

number_lower = int(input("请输入起始整数： "))
number_greater = int(input("请输入结束数字： "))
list_prime_number = []

for i in range(number_lower, number_greater + 1):
    j = int(sqrt(i) + 1)
    for k in range(2, j):
        if i % k == 0:
            break
        else:
            list_prime_number.append(i)
        break

print(f"The prime number are {list_prime_number}.")