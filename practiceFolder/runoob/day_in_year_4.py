# 题目：输入某年某月某日，判断这一天是这一年的第几天？

# 首先要区分平年还是闰年，平年265天，闰年366天；
# 在此基础上，之前月份的天数之和 + 当月的天数，即为当年的第几天

year_input = int(input("Please enter year: "))
month_input = int(input("Please enter month: "))
day_input = int(input("Please enter day: "))

# 平年计算方法
def days_in_common_year(month_input, day_input):
    day_in_common_year = [31, 30, 31, 28, 31, 30, 31, 31, 30, 31, 30, 31]
    sum_common = 0
    for i in  range(1, 13):
        if month_input == 1:
            days_in_common_year = day_input
        elif 1 < month_input <= 12:
            for i in range(1, month_input + 1):
                sum_common += day_in_common_year[i]
                days_in_common_year = sum_common + day_input - day_in_common_year[month_input]
                i += 1
        return days_in_common_year

# 闰年计算方法：
def days_in_leap_year(month_input, day_input):
    day_in_leap_year = [31, 30, 31, 29, 31, 30, 31, 31, 30, 31, 30, 31]
    sum_leap = 0
    for i in range(1, 13):
        if month_input == 1:
            days_in_leap_year = day_input
        elif 1 < month_input <= 12:
            for i in range(1, month_input + 1):
                sum_leap += day_in_leap_year[i]
                days_in_leap_year = sum_leap + day_input - day_in_leap_year[month_input]
                i += 1
        return days_in_leap_year

while True:
    if year_input > 1:
        if year_input % 4 == 0 and year_input % 100 != 0:
            print(f"This is the {days_in_leap_year(month_input, day_input)} days of this year.")
        elif year_input % 100 == 0 and year_input % 400 == 0:
            print(f"This is the {days_in_leap_year(month_input, day_input)} days of this year.")
        else:
            print(f"This is the {days_in_common_year(month_input, day_input)} days of this year.")
    else:
        print("Input Err, Bye.")
        break
    break







