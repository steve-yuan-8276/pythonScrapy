# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制

# 分析：S 可以看作一个数列，难点是构造数列当中每一项的值。
# 这里的解决办法是，把题目中的a当作一个str，通过字符串拼接得到 s[i] = a * i
# 之后，sn 转化为整数加入数列进行求和即可

number = input("Enter a ingter number(1-9): ")
times = int(input("Enter times: "))

list_number = []
sn = 0
for i in range(1, times + 1):
    sn = int(number * i)
    list_number.append(sn)
    i += 1

print(f"根据输入数字构造的数列为{list_number},由此推测该数字为{sum(list_number)}.")



