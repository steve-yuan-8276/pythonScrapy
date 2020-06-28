# 题目：按相反的顺序输出列表的值

# 方法一：
list_original = [1, 2, 3, 4, 5]
list_reverse = list_original[::-1]
print(list_reverse)

# 方法二：
list_reverse2 = list_original[:]
list_reverse2.reverse()
print(list_reverse2)