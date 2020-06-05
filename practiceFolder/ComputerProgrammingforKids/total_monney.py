# 程序说明
print("程序：利用函数计算零钱总值")

choices_user = ["y", "n"]
choice_user = input("enter 'y' to continue;\nenter 'n' to quit.\nYour choice: ")

def total_money(number_of_5_cents, number_of_2_cents, number_of_1_cents):
    total_money = number_of_1_cents + number_of_2_cents * 2 + number_of_5_cents * 5
    dollors = int(total_money / 100)
    cents = total_money % 100
    print(f"OK, You have {dollors} dollor {cents} cents.")

while True:
    if choice_user == choices_user[0]:
        number_of_5_cents = int(input("How many 5 cents do you have?"))
        number_of_2_cents = int(input("How many 2 cents do you have?"))
        number_of_1_cents = int(input("How many 1 cent do you have?"))
        total_money(number_of_5_cents, number_of_2_cents, number_of_1_cents)
        break
    elif choice_user == choices_user[1]:
        print("OK, Bye.")
        break
    elif choice_user not in choices_user:
        print("Input err.")
        break


print(total_money)
