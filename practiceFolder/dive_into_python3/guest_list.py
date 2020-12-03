# 创建客户名单列表，并根据要求进行修改

# guest lists
guest_list = ["lily", "harry", "ron"]

# show guest names
# print("Here are the guest name: " )
# for i in guest_list:
#     print(i.title())

# modify list
# guest_cannot_come = guest_list.pop()
# print(guest_cannot_come.title() + " " + "could not attend this meeting.")
# print("Here are the guest name: " )
# for i in guest_list:
#     print(i.title())

# add guest
new_guest = input("Please enter new guest: ")
# add name to the end of the line
# guest_list.append(new_guest)
# add name to the begin of the line
# guest_list.insert(0, new_guest)
# add name to the middle of the line
guest_list.insert(2, new_guest)
print("Here are the guest name: " )
for i in guest_list:
    print(i.title())

# delete name
for n in range(len(guest_list)):
    del_name = guest_list.pop()
    print(del_name.title() + " " + "could't attend this meeting.")
    # delete names untill there are only 2 guests, and show their names
    # if len(guest_list) <= 2:
    #     print("There are only 2 guests: ")
    #     for i in guest_list:
    #         print(i.title())
    #     break
    # delete names untill no one left.
    if len(guest_list) == 0:
        print("Now you can see, no one would come. SAD!!!")
        print(guest_list)

