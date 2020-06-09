# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数

string_user = input("Enter something: ")

number_letter = 0
number_space = 0
number_digit = 0
number_other = 0

for letter in string_user:
    if letter.isalpha():
        number_letter += 1
    elif letter.isspace():
        number_space += 1
    elif letter.isdigit():
        number_digit += 1
    else:
        number_other += 1

print(string_user)
print(f"letters = {number_letter}, spaces = {number_space}, digits = {number_digit}, others = {number_other}")
