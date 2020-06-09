# 题目：判断101-200之间有多少个素数，并输出所有素数

# 分析：
# 判断素数的方法：一个大于1的正整数，如果除了1和它本身以外，不能被其他正整数整除，就叫素数.

prime_number = []

for i in range(101, 200):
    for k in range(2, i + 1):
        if i % k == 0:
            break
        else:
            prime_number.append(i)
        break

print(prime_number)