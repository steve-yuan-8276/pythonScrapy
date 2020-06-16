# 题目：利用递归方法求5!

# 解题思路：
# 归递有两个特性：
# 1、一个基本特例，也称作平凡（一般）情况，它是递归终止的情形
# 2、一个已定义好的规则来使其它非基本的情形转化为基本情形

n = int(input("Enter a integer number: "))

def multiply(n):
    if n == 1:
        return
    return multiply(n - 1) * n     # 定义用到了自己本身的定义，就构成了递归

print(f"The result is {multiply(n)}.")