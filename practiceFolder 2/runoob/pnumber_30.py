# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同

number_input = input("Enter a integer number from 1 - 99999: ")

while number_input:
    if number_input == number_input[::-1]:
        print(f"{number_input} 是回文数。")
    else:
        print(f"{number_input} 不是回文数。")
    break

