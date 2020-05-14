n = int(input("Please input a integer(Input number must greater than 0.): "))

def fib(n):
    a, b = 0, 1
    for i in range(n + 1):
        a, b = b, a + b
    return a

for i in range(n):
    print(fib(i), end=' ')
