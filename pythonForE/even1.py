#for num in range(1, 100):
#    if num % 2 == 0:
#        print('Found a even number', num)
#        continue
#    print('Found a odd number', num)

lst = [x for x in range(100) if x % 2 == 0 and x != 0]
print(lst)