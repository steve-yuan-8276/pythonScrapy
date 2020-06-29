# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

list = [1, 2, 4, 6, 8, 10]
n = int(input("Enter a integer number: "))

list.append(n)
print(sorted(list))
