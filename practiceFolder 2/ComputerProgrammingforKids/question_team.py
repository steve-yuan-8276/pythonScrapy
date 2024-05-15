import easygui

gender_title = "GENDER INFORMATION"
gender_chioces = ["male", "female"]
gender_msg = "Please confirm your gender:"

gender_user = easygui.choicebox(gender_msg, gender_title, gender_chioces)

while True:
    if gender_user == gender_chioces[1]:
        gender_age = easygui.integerbox("Please input your age: ", lowerbound=0)
        if 10 <= gender_age <= 12:
            easygui.msgbox("Congratulations! You could be a part of female foot team.")
        elif gender_age < 10:
            easygui.msgbox("Sorry, You are too young.")
        else:
            easygui.msgbox("Sorry, You are too old.")
        break
    elif gender_user == gender_chioces[0]:
        easygui.msgbox("Sorry, You can't join the female foot team.")
        break
