# 题目：练习函数调用

# 函数调用
def greeting():
    print("Hello World!")

def cubic_greetiung():
    for i in range(3):
        greeting()
        i += 1

if __name__ ==  "__main__":
    cubic_greetiung()

# 匿名函数
m = int(input("Enter a integer number: "))
n = int(input("Enter a integer number: "))
sum = lambda m, n: m + n
print("The sum is ", sum(m, n))

# 不定长参数
def printvar(arg1, *vars):
    print(arg1)
    for var in vars:
        print(var)

printvar(10)
printvar(10, "Hi", "This is a test.")