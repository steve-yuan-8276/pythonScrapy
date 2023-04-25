"""
Print the triangle pattern as shown below.
"""

"""
 Model1:
*
**
***
****
*****
"""
row = int(input("Enter a integer number: "))
for i in range(row):
    for j in range(i):
        print("*", end = "")
    print()

"""
Model2:
    *
   **
  ***
 ****
*****
"""
for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(" ", end = "")
        else:
            print("*", end = "")
    print()

"""
Model 3:
    *
   ***
  *****
 *******
*********
首先定义了一个变量 n，表示金字塔的高度
接下来使用两个循环来控制输出的行数和每行的星号数目。
在第一个循环中，i 从 0 取到 n-1，表示金字塔的高度。
在第二个循环中，使用两个参数来控制每行的星号数目：
一个参数是 n-i-1，用来控制空格数目；
另一个参数是 2*i+1，用来控制星号数目。
最后，将空格和星号拼接起来，打印出来即可。
"""
for i in range(row):
    print(' ' * (row - i - 1) + '*' * (2 * i + 1))