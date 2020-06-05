# 题目2：
# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
# 高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

profits_user = int(input("Please enter the profits: "))

# 目前的办法是笨办法
def bonus(profits_user):
    if profits_user <= 100000:
        bonus = profits_user/10000 * 0.1 * 10000
    elif 100000 < profits_user <= 200000:
        bonus = (10 * 0.1 + (profits_user/10000 - 10) * 0.075) * 10000
    elif 200000 < profits_user <= 400000:
        bonus = (10 * 0.1 + 10 * 0.075 + (profits_user/10000 - 20) * 0.05) * 10000
    elif 400000 < profits_user <= 600000:
        bonus = (10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (profits_user/10000 - 40) * 0.03) * 10000
    elif 600000 < profits_user <= 1000000:
        bonus = (10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (profits_user/10000 - 60) * 0.015) * 10000
    elif profits_user > 1000000:
        bonus = (10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (profits_user/10000 - 100) * 0.01)\
                * 10000
    return bonus

while True:
    if profits_user > 0:
        print(f"Congratulations! Your bonus are {bonus(profits_user)} YUAN.")
        break
    elif profits_user <= 0:
        print(f"Sorry, No bonus. You need to work harder.")
        break
