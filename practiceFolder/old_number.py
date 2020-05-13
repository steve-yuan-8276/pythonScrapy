while True:
    number_1 = int(input("please input a number："))
    number_2 = int(input("Please input another number: "))
    if number_1 >= number_2:
        print("Sorry, you should input again.")
        break
    else:
        for i in range(number_1, number_2 + 1 ):
            if i % 2 != 0:
                print(i)
2