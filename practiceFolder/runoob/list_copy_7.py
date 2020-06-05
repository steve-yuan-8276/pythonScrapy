# 题目：将一个列表的数据复制到另一个列表中

list_original = []
choices_or_user = ["y", "q"]

choice_or_user = input("""
Enter y to begin:
Enter q to quit:
""")

while True:
    if choice_or_user == choices_or_user[0]:
        for i in range(5):
            item_of_the_list = input("Please enter something:  You have 5 times.")
            list_original.append(item_of_the_list)
            i += 1
    elif choice_or_user == choices_or_user[1]:
        print("OK, Time to stop.")
    break

list_copy = sorted(list_original[:])

print(f"This is original list {list_original} .")
print(f"This is copy list {list_copy}, As you see, it's sorted.")



