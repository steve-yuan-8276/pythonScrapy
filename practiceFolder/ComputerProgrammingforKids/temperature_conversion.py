print(""" This is a Teamperature conversion.
You can convert temperatures to and from celsius, fahrenheit.
Please enjoy it.
""")

your_option = int(input("""If you want to convert temperatures to celsius from fahrenheit, Press 1;
If you want to convert temperatures to fahrenheit from celsius, Press 2; 
Or Do nothing, Press 3. 
"""))

your_value = int(input("Please input the value: "))

def value_of_celsius(your_value):
    value_of_celsius = round(5/9*(your_value - 32))       # 此处使用round函数四舍五入
    # value_of_celsius = float(5)/9*(your_value - 32)
    return value_of_celsius

def value_of_fahrenheit(your_value):
    value_of_fahrenheit = your_value * 9//5 + 32
    return value_of_fahrenheit

if your_option == 1:
    print(f"The value of celsius is {value_of_celsius(your_value)} ºC. ")
elif your_option == 2:
    print(f"The value of fahrenheit is {value_of_fahrenheit(your_value)} ºF. ")
elif your_option == 3:             # 待解决问题：当输入3时，理想情况时结束程序，当时现在还会继续执行
    print("OK, Bye.")
