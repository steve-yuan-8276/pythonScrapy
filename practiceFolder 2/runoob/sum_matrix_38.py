# 题目：求一个3*3矩阵主对角线元素之和

# 在数学中，矩阵（Matrix）是一个按照长方阵列排列的复数或实数集合 ，最早来自于方程组的系数及常数所构成的方阵。
# 主对角线即左上到右下的那一条斜线，如list[1][1], list[2][2]
# 副对角线即左下到右上的斜线

import random

list_n = []
sum = 0

for i in range(3):
    list_n.append([])
    for j in range(3):
        list_n[i].append(random.randint(1, 99))
    sum += list_n[i][i]

print(list_n)
print(sum)