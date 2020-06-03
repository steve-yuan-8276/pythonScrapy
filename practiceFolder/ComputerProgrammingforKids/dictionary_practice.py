# 程序说明
print("""字典程序：
用户可以添加单词及定义，
也可进行查询，当单词存在时，给出相应定义；不在在时，提示用户查询单词不存在。
""")

dictionary_user = {}
choices_user = ["a", "l", "q"]

while True:
    choice_user = input("Add or look up a word?\n Please input a/l/q: \na means Add\nl means look up\nq means quit.")
    if choice_user == choices_user[0]:
        word_dic = input("Tpye the word: ")
        definition_input = input("Type the definition: ")
        dictionary_user[word_dic] = definition_input
        print("Word added!")
    elif choice_user == choices_user[1]:
        word_lookup = input("Type the word: ")
        if word_lookup in dictionary_user.keys():
            print(dictionary_user[word_lookup])
        else:
            print("That word is't in the dictionary yet.")
    elif choice_user == choices_user[2]:
        print("OK, See you, Bye.")
        break