import easygui

greeting_words = """This is a Teamperature conversion.
You can convert temperatures to and from celsius, fahrenheit.
Please enjoy it.
"""

easygui.msgbox(greeting_words)

your_option_intro = """If you want to convert temperatures to celsius from fahrenheit, Press 1;
If you want to convert temperatures to fahrenheit from celsius, Press 2; 
Or Do nothing, Press 3. 
"""
your_option_number = ["1",  "2", "3"]
title_option = "Please confirm:"

your_value = easygui.integerbox(msg="Please input the value: " , lowerbound = -274)
your_option = easygui.choicebox(your_option_intro, title_option, your_option_number)

def value_of_celsius(your_value):
    value_of_celsius = round(5/9*(your_value - 32))       # 此处使用round函数四舍五入
    # value_of_celsius = float(5)/9*(your_value - 32)
    return value_of_celsius

def value_of_fahrenheit(your_value):
    value_of_fahrenheit = your_value * 9//5 + 32
    return value_of_fahrenheit

while your_option:
    if your_option == "1":
        easygui.msgbox(f"The value of celsius is {value_of_celsius(your_value)} ºC. ")
    elif your_option == "2":
        easygui.msgbox(f"The value of fahrenheit is {value_of_fahrenheit(your_value)} ºF. ")
    elif your_option == "3":
        easygui.msgbox("OK, Bye.")
    break





