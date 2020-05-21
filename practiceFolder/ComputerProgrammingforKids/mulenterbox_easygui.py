import easygui

title = "USER INFORMATION"
msg_intro = "Please input user information:"
filed_name = ["NAME", "CONTARY", "PROVICE", "CITY", "ZIPCODE"]
#filed_values = []

filed_values = easygui.multenterbox(title, msg_intro,filed_name)
msg_err = "you must input something."

if filed_values != None:
    easygui.msgbox(filed_values)
else:
    easygui.msgbox(msg_err)

