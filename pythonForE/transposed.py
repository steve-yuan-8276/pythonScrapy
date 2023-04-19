matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# method A: 嵌套列表推导式
#transposed = [[row[i] for row in matrix] for i in range(4)]

# method B：for loop
#transposed = []
#for i in range(4):
#    transposed_row = []
#    for row in matrix:
#        transposed_row.append(row[i])
#    transposed.append(transposed_row)

#method C：zip函数
transposed = list(zip(*matrix))

print(transposed)