import easygui

for i in range(1,6):   # 显示5次
    easygui.msgbox(f"Hi, Steve. This is {i}")

for i in range(1, 6, 2): # 显示1，3，5
    easygui.msgbox(f"Hi, This is {i}")