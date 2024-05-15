from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def main():
    while left_is_clear():
        fill_the_row()
        reset_to_next_row()
    fill_the_row()

def fill_the_row():

    """
    Karel puts down beepers until she faces the wall 
    Pre: Karel is at the end of a row, facing east
    Post: Karel is back where she started at the end of the a row, facing east
    """
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()

def reset_to_next_row():
    """
    Pre: Karel is at the end of a row, facing right (east)
    Post: Karel is at the start of the next row, facing right (east)
    """
    turn_around()
    move_to_wall()
    turn_right()
    move()
    turn_right()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()

if __name__ == '__main__':
    main()
