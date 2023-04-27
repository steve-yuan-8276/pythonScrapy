
num = int(input("Please enter a integer: "))

lst1 = []
def flibsTwo(num):
    for i in range(num):
        if i <= 1:
            lst1.append(1)
        else:
            lst1.append(lst1[-2] + lst1[-1])
    return lst1

print(flibsTwo(num))
