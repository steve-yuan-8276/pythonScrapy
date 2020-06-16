# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

str_input = input("Enter a string(more the 5 words): ")
number_str = len(str_input)

def string_revise(str_input, number_str):
    if number_str == 0:
        return
    print(str_input[number_str - 1])
    string_revise(str_input, number_str - 1)

string_revise(str_input, number_str)

