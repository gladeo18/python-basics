import random
import re
from django.shortcuts import render

# CHALLENGE: Check if string is a float, integer, or complex
# SOLUTION #1: use isinstance() function BUT the real problem is string -> int, float, complex
# SOLUTION #2: use REGEX -> give this a try to get a better understanding of REGEX
# Try to solve this next time :)

def conversion():
    num = input("\nEnter a valid number you want to convert: ")
    is_num = re.match("[-+]?\d+$", num)
    is_range = False

    if is_num:
        conversion_list = {"a": int(float(num)), "b": float(num), "c": complex(num)}
        print("How would you like to convert this number: [a] integer [b] float [c] complex ")
        num_type = input("Answer: ").lower()

        for i in range(ord('a'), ord('d')):
            if num_type == chr(i):
                print("\nFrom ", num, " to ", conversion_list[num_type])
                print("The number was converted successfully!")
                is_range = True 
        
        if not is_range:
            print("\nAnswer is not within range!")
            conversion()
    else:
        print("Invalid input.")  # Rephrase this LOL
        conversion()

def random_num():
    print("\nHere is a Random Number: ", random.randrange(0,10000))

def inputs(choice):
    choices_list = {"a": conversion, "b": random_num}
    choices_list[choice]()

choice = " "

while choice != "c":
    within_range = False
    print("\nLet's play with numbers!")
    print("\n[a] Convert numbers into another number type [b] Generate Random Number [c] Exit ")
    choice = input("Answer: ").lower()

    for i in range(ord('a'), ord('c')):
        if choice == chr(i):
            inputs(choice)
            within_range = True
    
    if choice != "c" and not within_range:
        print("\nAnswer is not in the choices. How would you like to play?")

print("\nThanks for playing")
        


