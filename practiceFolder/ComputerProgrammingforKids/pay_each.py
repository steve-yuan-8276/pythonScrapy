total_pay = int(input("How much is this lauch?"))
person_number = int(input("How many people?"))

pay_each = (total_pay + total_pay*0.15)//person_number

print(f"{pay_each} for each, Please give me money.")