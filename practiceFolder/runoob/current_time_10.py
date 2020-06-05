# 题目：暂停一秒输出，并格式化当前时间
import time
from time import localtime, strftime

print("Wait a second, please.")

time.sleep(1)

print("Current time: ")
print(strftime("%a, %d, %b, %Y, %p，%H:%M:%S", localtime()))