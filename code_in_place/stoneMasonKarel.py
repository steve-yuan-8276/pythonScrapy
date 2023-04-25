from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    repair_column()

def repair_column():
    turn_left()
    ascend_column()
    turn_around()
    descend_column()
    turn_left()
    if front_is_clear():
        move_to_next_column()
        repair_column()

def ascend_column():
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
    if no_beepers_present():
        put_beeper()

def descend_column():
    while front_is_clear():
        move()

def move_to_next_column():
    for i in range(4):
        move()

def turn_around():
    for i in range(2):
        turn_left()

if __name__ == '__main__':
    main()
