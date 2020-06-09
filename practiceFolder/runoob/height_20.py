# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

height_single = []

height_original = 100
time_jump = 10

for i in range(1, time_jump + 1):
    if i == 1:
        height_single.append(100)
    else:
        height_single.append(height_original * 2)
    height_original = height_original/2

print(f"Afrer 10 times, The total height is {sum(height_single)} meters, and you jump {height_single[-1]} meters at last time.")
