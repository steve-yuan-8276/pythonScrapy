list_1 = [1, 3,  5, 7, 9]
list_2 = [12, 23, 43, 45, 56, 456, 6545, 36566]
sum_list = []

def sum(list_1, list_2, sum_list):
    for i in range(len(list_1)):
        a = list_1[i] + list_2[i]
        sum_list.append(a)
    for i in range(len(list_1), len(list_2)):
        a = 0 + list_2[i]
        sum_list.append(a)

sum(list_1, list_2, sum_list)
print(sum_list)