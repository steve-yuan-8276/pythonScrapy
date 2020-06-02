import easygui

title = "PASSWORD INFORMATIONS"
msg = "Please enter the password: "
password_default = ["111", "222", "333", "444"]

i = 0
while i < 5:
    password_input = easygui.passwordbox(title, msg)
    if password_input in password_default:
        easygui.msgbox("OK, You are in.")
        break
    elif password_input not in password_default and i < 4:
        easygui.msgbox(" please try again. You have 5 times max.")
    elif password_input not in password_default and i == 5:
        break
    i += 1

if i == 5:
    easygui.msgbox("Sorry, The password is incorrect.")
