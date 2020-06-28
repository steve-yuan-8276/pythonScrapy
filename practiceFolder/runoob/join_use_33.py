# 题目：按逗号分隔列表。

# 方法一：
list_data = [1, 2, 3, 4, 5]
str_1 = ",".join(str(n) for n in list_data)
print(str_1)
