import easygui

msg_pay_each_intro = """这个小程序可以计算AA制餐费，
您告诉我总价和人数，
我告诉您每人需要付多少钱。
希望可以帮到您。
"""

easygui.msgbox(msg_pay_each_intro)
total_pay = easygui.integerbox(msg="How much is this lauch?" , lowerbound=0)
person_number = easygui.integerbox(msg="How many people?" , lowerbound=1)

pay_each = (total_pay + total_pay*0.15)//person_number

easygui.msgbox(f"{pay_each} for each, Please give the money.")
