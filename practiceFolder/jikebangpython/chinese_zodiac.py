# 练习题目：根据用户输入判断生肖和星座

# 公元元年对应的是鸡年，所以这里也从鸡年开头，减少后面运算的复杂度
chinese_zodiac = ["Rooster 鸡年", "Dog 狗年", "Pig 猪年", "Rat 鼠年", "Ox 牛年", "Tiger 虎年", "Rabbit 兔年", "Dragon 龙年",
                  "Snake 蛇年", "Horse 马年", "Sheep 羊年", "Monkey 猴年"]
# 十二星座
star_sign = ["Aquarius 水瓶座", "Pisces 双鱼座", "Aries 牧羊座", "Taurus 金牛座", "Gemini 双子座", "Cancer 巨蟹座",
             "Leo 狮子座", "Virgo 处女座", "Libra 天秤座", "Scorpio 天蝎座", "Sagittarius 射手座", "Capricorn 摩羯座"]
# 十二生肖对应的日期
date_star_sign = ((1, 21), (2, 20), (3, 21), (4, 20), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 24), (11, 22),
                  (12, 21))

print("程序说明：根据用户输入判断生肖和星座")

year_input = int(input("Enter year: "))
month_input = int(input("enter month: "))
date_input = int(input("Enter day: "))


while year_input:
    if 1 <= year_input <= 12:
        i = (year_input + 12) % 12
        break
    else:
        i = year_input % 12
        break

print(f"The chinese zodic is {chinese_zodiac[i - 1]}")

print(len(date_star_sign))

for i in range(len(date_star_sign)):
    if date_star_sign[i] >= (month_input, date_input):
        print(f"The star sign is {star_sign[i - 1]} .")
        break

    elif month_input == 12 and date_input > 23:
        print(f"The star sign is {star_sign[0]} .")
        break

