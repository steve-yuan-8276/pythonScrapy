# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字

number_input = list(input("Enter a integer number between 1 to 99999: "))

print(f"这是 {len(number_input)}  位数；\n逆序打印各位数字 {sorted(number_input, reverse=True)}")