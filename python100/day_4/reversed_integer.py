"""
Integer reversal is the process of reversing the order of digits in an integer, for example, reversing 123 to become
321. The following are the steps to reverse an integer:

1. Create a variable called reversed_num to store the reversed number with
 an initial value of 0.
2. Get the ones digit of the original integer using modulo operator (%),
and store it as the ones digit of reversed_num.
3. Divide the original integer by 10 using floor division (//) to remove
its ones digit, e.g., dividing 123 by 10 gives you 12.
4. Multiply reversed_num by 10 to shift all digits one place left and make
 room for adding next digit from step #2.
5. Add both numbers obtained in step #2 and step #4 together, which adds
current ones digit into reversed_num.
6. Repeat steps #2-#5 until there are no more digits left in original
integer (i.e., when it becomes zero).
7. Finally, reversed_num will contain the desired result - i.e.,the given
input's digits have been flipped or "reversed".
"""

num = int(input("Enter a integer number: "))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num = num // 10
print(f"The reversed number is {reversed_num}.")