number_of_5_cents = int(input("How many 5 cents do you have?"))
number_of_2_cents = int(input("How many 2 cents do you have?"))
number_of_1_cents = int(input("How many 1 cent do you have?"))

total_money = number_of_1_cents + number_of_2_cents*2 + number_of_5_cents*5
dollors = int(total_money/100)
cents = total_money%100
print(total_money)
print(f"OK, You have {dollors} dollor {cents} cents.")