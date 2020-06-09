# 题目：打印出所有的"水仙花数"

# 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

# 方法1：
#for n in range(100, 1000):
#    i = int(n/100)
#    k = int((n - 100 * i)/10)
#    j = int(n - 100 * i - 10 * k)
#    if 100 * i + 10 * k + j == i * i * i + k * k * k + j * j * j:
#        print(n)


# 方法2：
for i in range(1, 10):
    for k in range(0, 10):
        for j in range(0, 10):
            if 100 * i + 10 * k + j == i * i * i + k * k * k + j * j * j:
                n = 100 * i + 10 * k + j
                print(n)
