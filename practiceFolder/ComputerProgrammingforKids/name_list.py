names = []

for i in range(0, 5):
    name = input("Please input a name: ")
    names.append(name)
    i += 1

new_names = sorted(names)

print(f"Here is your inputs:  {new_names}")
#for name in names:
#    print(name)