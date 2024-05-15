# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和

list = []

a, b = 2, 1
for i in range(1, 21):
    if i == 1:
        a, b = 2, 1
    else:
        a, b = a + b, a
        i += 1
    sn = a/b
    list.append(sn)

print(list)
print(f"The sum are {sum(list)}")

