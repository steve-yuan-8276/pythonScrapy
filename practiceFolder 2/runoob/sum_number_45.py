# 题目：统计 1 到 100 之和

number_input = int(input("Please enter a integer number: "))

# 方法一：
# sum_number = 0
# for i in range(number_input + 1):
#     sum_number += i
#
# print(f"The sum is {sum_number}.")

# 方法二：
sum_number = []
for i in range(number_input + 1):
    sum_number.append(i)
    i += 1

print(f"The sum is {sum(sum_number)}.")