while True:
    number_1 = int(input("Please input a integer: "))
    number_2 = int(input("Please input another integer: "))
    if number_1 >= number_2:
        print("Please input again.")
        break
    else:
        for i in range(number_1,number_2):
            if i % 2 == 0:
                print(f"We have found a enen number {i}")
                continue
            print(f"We have found a old number {i}")