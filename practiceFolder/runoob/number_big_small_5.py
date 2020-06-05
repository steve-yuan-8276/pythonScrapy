# 题目：输入三个整数x,y,z，请把这三个数由小到大输出

# 分析：
# 利用数列排序 sort

list_user = []

for i in range(1, 4):
    item_user = int(input(f"Enter a integer number. number{i}:  "))
    list_user.append(item_user)
    i += 1

list_sorted = list_user[:]
list_sorted.sort(reverse=True)


print(f"Here is your input: {list_user}")
print(f"Here is sorted result: {list_sorted}.")


