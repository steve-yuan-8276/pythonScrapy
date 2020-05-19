print("""This is a program to evaluate traval time.
Tell me traval distance and speed, and I will give you answear.
""")

distance_of_traval = int(input("Tell me traval distance: "))
speed = int(input("Tell me the average speed: "))

def time_of_traval(distance_of_traval, speed):
    time_of_traval = round(distance_of_traval/speed, 2)
    return time_of_traval

print(f"I guess {time_of_traval(distance_of_traval, speed)} hours.")
