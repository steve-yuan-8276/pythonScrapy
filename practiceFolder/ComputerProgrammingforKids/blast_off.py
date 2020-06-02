import time

countdown_timer = int(input("Give a countdown number:"))

for i in range(countdown_timer, 0, -1):
    print(i, "* " * i)
    time.sleep(1)
print("Blast Off!")

# for i in range(countdown_timer, 0, -1):
#    print("* " * i)
#    time.sleep(1)