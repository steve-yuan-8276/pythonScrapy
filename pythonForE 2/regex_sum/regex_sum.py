import re

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1785719.txt"
handle = open(name)

num = list()
for line in handle:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    for s in stuff:
        n = int(s)
        num.append(n)

print("The total number is ", sum(num))

