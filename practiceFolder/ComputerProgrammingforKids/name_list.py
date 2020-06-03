names = []

for i in range(0, 5):
    name = input("Please input a name: ")
    names.append(name)
    i += 1

# 显示输入的名字
print(f"The names are: {names}")

# 显示排序后的名字列表
new_names = sorted(names)
print(f"Here is your inputs:  {new_names}")

# 显示输入的第三个名字
print(f"The third name is {names[2]}")

# 用户替换列表
number_names_list = int(input("Replace one name. Which one? (1-5): "))
value_names_list = input("New name: ")

k = number_names_list - 1
if k <= 4:
    names[k] = value_names_list
    print(f"The names are: {names}")
else:
    print("Input err. Sorry.")



