# 题目：暂停一秒输出

import time

user_name = input("What's your name?")

print("Wait a second, please.")
time.sleep(1)
print(f"Nice to meet you, {user_name.capitalize()}. It's me WALL-E.")