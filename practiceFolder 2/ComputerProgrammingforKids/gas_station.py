import easygui

km_per_liter = 10

size_tank = easygui.integerbox(msg="What size of your tank?", lowerbound=1)
percent_full = easygui.integerbox(msg="How many percent of your tank remains?", lowerbound=0)
distance_another_gas_station = easygui.integerbox(msg="How many kilometers away from here?",lowerbound=1, upperbound=500)

distance_can_go = percent_full/100 * size_tank * km_per_liter

while True:
    if distance_can_go >= distance_another_gas_station + 10:
        easygui.msgbox(f"""
        Size of tank:  {size_tank},\n
        percent full: {percent_full},\n
        km per liter: 10,\n
        You can go another {distance_can_go} km.\n
        The next gas stition is {distance_another_gas_station} km away, You can wait for the next station.
        """)
    else:
        easygui.msgbox(f"""Size of tank:  {size_tank},
        percent full: {percent_full},
        km per liter: 10,
        You can go another {distance_can_go} km.
        The next gas stition is {distance_another_gas_station} km away, 
        So you can't get there. We suggest you should charge in this station.
        """)
    break

