# 打印出菱形案：

symbol_a = " "
symbol_b = "*"
# 有bug
for i in range(1, 8, 1):
    for i in range(1, 5):
        a = 3
        b = 1
        print(symbol_a * a, symbol_b * b)
        a -= 1
        b += 2
    for i in range(5,8):
        a, b = 1, 5
        print(symbol_a * a, symbol_b * b)
        a += 1
        b -= 2


