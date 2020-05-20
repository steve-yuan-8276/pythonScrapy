import easygui

# msgbox
easygui.msgbox("Hello There! ")

# enterbox
msg_enterbox = easygui.enterbox("What's your name?")
easygui.msgbox(f"Hello, {msg_enterbox.title()}")


# ccbox
msg_ccbox = "Do you want to continue?"
title_ccbox = "Please confirm:"
if easygui.ccbox(msg_ccbox, title_ccbox):
    pass
else:
    sys.exit(0)

# ynbox
msg_ynbox = "Do you like me?"
title_ynbox = "Please confirm:"
if easygui.ynbox(msg_ynbox, title_ynbox):
    pass
else:
    sys.exit(0)

# buttonbox
question_flavor = "whhich is your favorite ice cream?"
title_buttonbox = "Ice Cream Survey"
choices_buttonbox = ["vanilla", "chocolate", "strawberry", "lala"]
if easygui.buttonbox(question_flavor, title_buttonbox, choices_buttonbox):
    pass
else:
    sys.exit(0)

# choicebox
msg_choicebox = "Do you like this picture?"
img_choicebox = "giphy.gif"
option_choicebox = ["Yeah", "No", "No Idea"]
reply = easygui.buttonbox(msg_choicebox,image=img_choicebox,choices=option_choicebox)
#replay =  easygvi.buttonbox(msg_enterbox, image=img_choicebox, option_choicebox)
