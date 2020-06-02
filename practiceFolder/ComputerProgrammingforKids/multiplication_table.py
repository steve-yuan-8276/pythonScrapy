print("Which multiplication table would you like? ")

number_input = int(input("Please input a interger number: "))
number_high = int(input("Please input a interger number: "))

i = 1
print("Here is you table:")
# while loop
# while i <= number_high:
# for loop
for i in range(1, number_high+1):
    print("{}*{}={}\n".format(number_input, i, number_input*i), end = "")
    i += 1
