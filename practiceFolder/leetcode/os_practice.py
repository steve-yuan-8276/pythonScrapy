import os

# create directory
 os.mkdir("aa")
# remove directory
 os.rmdir("aa")
# change directory
 os.chdir("aa")
 os.mkdir("bb")
# get directory information
 d_name = os.getcwd()
 print(d_name)
# get the list of directory
l_name = os.listdir("aa")
print(l_name)
