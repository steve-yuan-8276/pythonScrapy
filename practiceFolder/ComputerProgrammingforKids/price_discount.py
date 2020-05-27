import easygui

price_original = easygui.integerbox(msg="Please input the original price: ", lowerbound=0)

while price_original > 0:
    if price_original <= 10:
        easygui.msgbox(f"You can get 10% discount, and the final price is {price_original * 0.9} ")
    else:
        easygui.msgbox(f"You can get 20% discount, and the final price is {price_original * 0.8} ")
    break








