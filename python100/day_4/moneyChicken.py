"""
Baiqian Baiji" is a mathematical problem proposed by the ancient Chinese mathematician Zhang Qiujian in the book "Suanjing": A rooster costs five coins, a hen costs three coins, and three chicks cost one coin. If you want to buy 100 chickens with 100 coins, how many roosters, hens and chicks should you buy?
"""

rooster_cost = 5
hen_cost = 3
chick_cost = 1/3

for rooster_num in range(1, 20):
    for hen_num in range(1, 33):
        chick_num = 100 - rooster_num - hen_num
        if rooster_num * rooster_cost + hen_num * hen_cost + chick_num * chick_cost == 100:
            print(f"There are {rooster_num} roosters, {hen_num} hens, and {chick_num} chicks.")




