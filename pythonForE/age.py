from datetime import date

def calculate_age(born):
    """
    计算年龄的函数，输入生日日期，返回年龄
    """
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

# 输入出生日期，格式为年-月-日
birthday = input("请输入您的出生日期(格式为yyyy-mm-dd): ")

# 将输入的字符串转换为日期类型
born = date.fromisoformat(birthday)

# 调用函数计算年龄并输出结果
age = calculate_age(born)
print(f"您的年龄是{age}岁")

