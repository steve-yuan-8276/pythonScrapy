# 题目：对10个数进行排序

number_list = []

for i in range(1, 11):
    print(f" times:{i}")
    number_input = int(input(f"Enter a integer number:  "))
    number_list.append(number_input)

number_list_new = number_list[:]
number_list_sorted = sorted(number_list_new)
print(f"From lower number to greater number: {number_list_sorted}.")

number_list_reverse = number_list_sorted[::-1]
print(f"From Greatest number to lower number: {number_list_reverse}.")