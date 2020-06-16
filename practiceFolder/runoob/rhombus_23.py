# 打印出菱形案：

symbol_a = " "
symbol_b = "*"

a, b = 3, 1
for i in range(1, 5):
    print(symbol_a * a, symbol_b * b)
    a -= 1
    b += 2

a, b = 1, 5
for i in range(3):
    print(symbol_a * a, symbol_b * b)
    a += 1
    b -= 2




