from django.shortcuts import render

def check_age():

    your_age = " "
    friend_age = " "

    try:
        your_age = int(input("How old are you? "))
        friend_age = int(input("How about your friend's age? "))
    except ValueError:
        print("\nYou've entered a non-numeric value. ", end = " ")
        check_age()
    
    if your_age == friend_age:
        print("\nHey", (your_name),", you're the same age as", (friend_name))
    elif your_age > friend_age:
        print("\nHey", (your_name),", you're older than", (friend_name))
    else:
        print("\nHey", (your_name),", you're younger than", (friend_name))


print("\nTake a guess: Are you younger or older than your colleague?")
play = ""

while play != "N":
    is_play = False

    play = input("\nDo you want to play? [Y] [N] ").upper()

    if play == "Y":
        your_name = input("\nWhat is your name? ")
        friend_name = input("What is the name of your friend? ")
        print(" ")

        check_age()
        is_play = True

    elif play != "N" and not is_play:
        print("\nInvalid input.", end = " ")

print("\nThanks for playing :)")