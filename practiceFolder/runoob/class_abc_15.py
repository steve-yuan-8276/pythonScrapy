# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示

choice_user = input("Enter y to start,Enter q to quit.\nYour choice: ")

while True:
    if choice_user == "y":
        score_user = float(input("Enter your score: "))
        if score_user >= 90:
            print("Congrats! You've got A!")
        elif 60 <= score_user <= 89:
            print("You've got B. Keep working.")
        elif score_user < 60:
            print("Sorry, You need work harder.")
    elif choice_user == "q":
        print("Bye.")
    break




