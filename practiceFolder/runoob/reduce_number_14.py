# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

from math import sqrt

n = int(input("Enter a integer number(Greater than 2): "))

prime_number_list = []

for i in range(2, n + 1):
    if n % i == 0:
        prime_number_list.append(i)
        n = n/i

for k in range(len(prime_number_list)):
    print(f"{prime_number_list[k]} ", end=" ")