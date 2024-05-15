# 题目：求1+2!+3!+...+20!的和

sum_list = []
int_number_input = int(input("Enter a integer nunber: "))

sn = 1
for i in range(1, int_number_input + 1):
    sn *= i
    sum_list.append(sn)

print(sum_list)
print("1! + 2! + 3! + …… + 20！ = %d" % sum(sum_list))