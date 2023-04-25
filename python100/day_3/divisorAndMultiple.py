"""
Enter two positive integers and calculate their greatest common divisor and least common multiple.

The greatest common divisor of two numbers is the largest number among their common factors; the least common multiple of two numbers is the smallest number that can be divided by both of them.

计算两个正整数的最大公约数和最小公倍数的最简单算法是使用欧几里得算法，也称为辗转相除法。该算法基于以下定理：两个整数a和b（a>b）的最大公约数等于a除以b的余数c和b之间的最大公约数。具体实现方法如下：

如果a小于b，则交换a和b，保证a始终大于等于b。
计算a除以b的余数c，将a的值更新为b，将b的值更新为c。
重复执行步骤2，直到c等于0。
此时，a的值即为原始两数的最大公约数。
通过公式a*b/最大公约数，可以计算出原始两数的最小公倍数。

The simplest algorithm for calculating the greatest common divisor and least common multiple of two positive integers is to use the Euclidean algorithm, also known as the division algorithm. The algorithm is based on the following theorem: The greatest common divisor of two integers a and b (a>b) is equal to the greatest common divisor between c, which is the remainder when a is divided by b, and b. The specific implementation method is as follows:

If a<b, swap a and b to ensure that a is always greater than or equal to b.
Calculate the remainder c when dividing a by b, update the value of a with b, and update the value of b with c.
Repeat step 2 until c equals 0.
At this point, the value of a is equal to the greatest common divisor of original two numbers.
The least common multiple can be calculated using formula: (a*b)/greatest common divisor.
"""

# program to find the greatest common divisor and least common multiple of two numbers
a = int(input("Enter a integer number: "))
b = int(input("Enter another integer number: "))

if a > b:
    a, b = b, a

# find greatest common divisor
for factor in range(a, 0, -1):
    if a % factor == 0 and b % factor == 0:
        print(f"The greatest common divisor is {factor}.")
        break

# find least common multiple
lcm = (a * b) // factor
print(f"The least common multiple is {lcm}.")

