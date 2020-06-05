# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子
# 假如兔子都不死，问每个月的兔子总数为多少？

# 提示：兔子数量问题，本质上就是斐波纳切数列

print("Classic rabbit number:\nTell me the month number, And I will tell you number of rabbits.")
number_month = int(input("Which month: "))

def fib(number_month):
    a, b = 0, 1
    for i in range(number_month + 1):
        a, b = b, a + b
    return a

print(f"OK, The number of rabbits are {fib(number_month)}. ")
