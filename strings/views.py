from django.shortcuts import render

list_string = []
index = 0
choice = ""

def access_sing_char():
    global index
    not_empty = show_list()
    
    if not_empty:
        answer = input("\nAnswer: ")

        if answer in list_string: 
            print("\nThis is the String you wanted to explore: ", answer)
            print("\nAmong the ", len(answer), " characters of this string, which index (number) would you like to access?")

            try:
                index = int(input("Answer: "))
                if index == 0 or index > len(answer): raise ValueError
            except ValueError:
                print("\nThe index you entered is either not a number, beyond the string's length, or 0!")
                access_sing_char()

            print("\nThis is the",index,"x letter of the string: '", answer[index-1],"'")

        else: 
            print("\nThe item that you want to explore is not in the list!")
            access_sing_char()

def access_mult_char():
    not_empty = show_list()

    if not_empty:
        answer = input("\nAnswer: ")

        if answer in list_string: 
            print("\nThis is the String you wanted to explore: ", answer)
            print("\nWe are going to print a range of characters!") 

            try:
                answer1 = int(input("\nWhich index (number) would you like to start exploring: "))
                answer2 = int(input("The last index (number) that you want to access: "))

                if answer1 == 0 or answer1 > len(answer): raise ValueError
                if answer2 == 0 or answer2 > len(answer): raise ValueError
            except ValueError:
                print("\nThe index/indeces you entered is/are either not a number, beyond the string's length, or 0!")
                access_mult_char()

            print("\nHere's the",answer1,"-",answer2,"x letter of the string: \n")

            answer1 -= 1

            while answer1 < answer2:
                print(answer[answer1])
                answer1 += 1
        else: 
            print("\nThe item that you want to explore is not in the list!")
            access_mult_char()

def check_string():
    if not list_string:
        print("\nThe list is empty! Go and enter some strings first.")
    else:
        print("\nCheck whether the string you enter is in the list!")
        answer = input("Enter the string you like to check: ")

        if answer in list_string: print("\nThis string is in the list!")
        else: print("\nThis string is not in the list :(")

def insert_char():
    global index
    not_empty = show_list()

    if not_empty:
        answer = input("\nAnswer: ")

        if answer in list_string: 
            print("\nThis is the String you chose: ", answer)
            char_insert = input("Character/s you want to insert: ")

            try:
                index = int(input("Which index (number) do you want these characters to be inserted: "))
                if index == 0 or index > len(answer): raise ValueError
            except ValueError:
                print("\nThe index you entered is either not a number, beyond the string's length, or 0!")
                insert_char()
            
            new_string = answer[:index] + char_insert + answer[index:]
            print("\nThis is the new string: ", new_string)

        else:
            print("\nThis string is not in the list!")
            insert_char()

def del_char():
    not_empty = show_list()

    if not_empty:
        answer = input("\nAnswer: ")

        if answer in list_string: 
            try:
                index = int(input("\nWhich index (number) do you want to delete: "))
            except ValueError:
                print("The index is either not a number, beyond the string's length, or a 0!")
                del_char()

            new_string = answer.replace(answer[index-1], "")

            for i in range(len(list_string)):
                if list_string[i] == answer:
                    list_string[i] = new_string

            print("\nHere is the new string: ", new_string)
        else:
            print("\nThis string is not in the list!")
            del_char()

def add_list():
    if list_string:
        print("\nHere is/are the string/s in your list: ")
        for i in list_string:
            print("[",i,"]", end = ", ")
    
    my_string = input("\nEnter a string: ")
    print("String is added to the list successfully!")
    list_string.append(my_string)

def del_list():
    if not list_string:
        print("\nYour list is empty! Go and enter some string first.")
    else:
        print("\nEnter the string that you would like to delete?")
        print("Strings in your list: ", end = " ")
        for i in list_string:
            print("[",i,"]", end = ", ")

        answer = input("\nAnswer: ")

        if answer in list_string: 
            print("\n",answer, "was successfully removed from the list")
            list_string.remove(answer)
        else: 
            print("\nThe item that you want to delete is not in the list!")
            del_list()

def show_list():
    if not list_string:
        print("\nYour list is empty! Go and enter some string first.")
        return False
    else:
        print("\nEnter the string that you would like to explore")
        print("Strings in your list: ", end = " ")
        for i in list_string:
            print("[",i,"]", end = ", ")
        return True

def choices(choice):
    choices_list = {"a": add_list, "b": del_list, "c": access_sing_char, "d": access_mult_char, "e": check_string, "f": insert_char, "g": del_char}
    choices_list[choice]()

print("\nLearning Strings with Python!")

while choice != "h":

    is_range = False

    print("\nChoose one of these options:\n[a] Add string to the list [b] Remove string from the list [c] Access Single Character [d] Access Multiple Characters [e] Find me not! [f] Insert a character [g] Delete a character [h] Exit")
    choice = input("Answer: ").lower()

    for i in range(ord('a'), ord('h')):
        if chr(i) == choice:
            choices(choice)
            is_range = True

    if not is_range and choice != "h":
        print("Invalid input.", end = " ")

print("You've learned a lot! Keep it up~")




