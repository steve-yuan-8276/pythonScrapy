import easygui

msg_print = """This is a program to evaluate traval time.
Tell me traval distance and speed, and I will give you answear.
"""

easygui.msgbox(msg_print)

distance_of_traval = easygui.integerbox(msg="Tell me traval distance: ", lowerbound=0, upperbound=10000)
speed = easygui.integerbox(msg="Tell me the average speed: ", lowerbound=1, upperbound=300)

def time_of_traval(distance_of_traval, speed):
    time_of_traval = round(distance_of_traval/speed, 2)
    return time_of_traval

easygui.msgbox(f"I guess {time_of_traval(distance_of_traval, speed)} hours.")
