# 题目：输出指定格式的日期。
#
# 分析：此题实际是要求学习time 模块的用法

import time, datetime

# today
print(time.strftime("%Y, %m, %d"))
print(datetime.date.today())

# yesterday
today = datetime.date.today()
oneday = datetime.timedelta(days=1)
yesterday = today - oneday
print(f"Yesterday is {yesterday}.")
