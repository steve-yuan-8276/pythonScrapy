# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

# 周一：Monday
# 周二：Tuesday
# 周三：Wednesday
# 周四：Thursday
# 周五：Friday
# 周六：Saturday
# 周日：Sunday

print("根据第一个字母来判断一下是星期几;\n如果第一个字母一样，则继续判断第二个字母.")

words_input_1 = input("Please enter a letter: ")

while words_input_1:
    if words_input_1 == "m":
        print("It is Monday.")
    elif words_input_1 == "w":
        print("It is Wednesday.")
    elif words_input_1 == "f":
        print("It's Friday.")
    elif words_input_1 == "t":
        words_input_2 = input("Please enter another letter: ")
        if words_input_2 == "u":
            print("It's Tuesday.")
        else:
            print("It's Thusday.")
    elif words_input_1 == "s":
        words_input_2 = input("Please enter another letter: ")
        if words_input_2 == "a":
            print("It's Saturday.")
        else:
            print("It's Sunday.")
    break