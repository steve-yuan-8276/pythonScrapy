from karel.stanfordkarel import *

def main():
    move()  # Move to the second corner with the pile of beepers
    num_beepers = pick_up_beepers()  # Pick up all beepers from the pile

    # Move forward and put down beepers based on the number of beepers picked up
    for _ in range(num_beepers):
        move()
        put_beeper()

    # Return Karel to the starting position
    return_to_start()

def pick_up_beepers():
    n = 0
    while beepers_present():
        pick_beeper()
        n += 1
    return n

def return_to_start():
    turn_around()
    while front_is_clear():
        move()
    turn_around()

def turn_around():
    for i in range(2):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()

