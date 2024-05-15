# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数

import math

for i in range(1, 1001):
    factors = []
    for j in range(1, math.floor(i/2) + 1):   # math.floor(x) Returns:  largest integer not greater than x.
        if i % j == 0:
            factors.append(j)
    if sum(factors) == i:
        print(f"{i} is perfect number, and the factors are {factors}.")