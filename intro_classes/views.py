import re
from django.shortcuts import render

# Pending: Error handling

choice = ""

class UserRegistration:

    users_list = []
    global index

    def __init__(self, first_name, last_name, full_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.email = email
        self.users_list.append(self)

    def syntax_email(email): # Checks email syntax
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        if re.fullmatch(regex, email):
            if len(UserRegistration.users_list) == 0: return True
            elif len(UserRegistration.users_list) >= 1:
                if UserRegistration.duplicate_email(email): return True
                else: return False
        else: return False

    def duplicate_email(email): # Checks for any duplicate emails
        for x in UserRegistration.users_list:
            if email == x.email: return False
            else: return True 

    def add():  # Add user

        first_name = input("\nEnter the Name of the user: ")
        last_name = input("Enter the Surname of the user: ")
        full_name = first_name + " " + last_name
        email = input("Enter the email of the user: ")

        while not UserRegistration.syntax_email(email):
            email = input("\nInvalid Email! The email must not be a duplicate and has a valid email syntax [example@example.com]: ")
            UserRegistration.syntax_email(email)
        
        UserRegistration(first_name, last_name, full_name, email)

        print("\nA user has been added!")

    def show():  # Prints all instances
        index = 1
        print("\nHere is your list of users:")

        for x in UserRegistration.users_list:
            print("\nUser #", index)
            print("Name: ", x.first_name)
            print("Surname: ", x.last_name)
            print("Full Name: ", x.full_name)
            print("Email: ", x.email)

            index+=1
    
    def remove():
        index = 0
        email_list = False
        delete_user = input("\nEnter the email address of the user you want to delete: ")

        for x in UserRegistration.users_list:
                if delete_user == x.email:
                    del_validation = input("Are you sure you want to delete the information of this email address? [Y] [N]: ").lower()
                    
                    if del_validation == "y":
                        for x in UserRegistration.users_list:
                            if delete_user == x.email:
                                print("The user with the email address ", x.email, "has been deleted")
                                del x.users_list[index]
                            
                            index+=1 
                    else: UserRegistration.remove()
                    email_list = True
        
        if not email_list:
            print("The email you entered is not in the database!")
            UserRegistration.remove()

    def update():
        update_user = input("\nEnter the email address of the user you want to update: ")
        index = 0
        email_list = False

        for x in UserRegistration.users_list:
            if update_user == x.email:
                first_name = input("Enter the new first name: ")
                last_name = input("Enter the new last name: ")
                x.users_list[index].first_name = first_name
                x.users_list[index].last_name = last_name
                x.users_list[index].full_name = first_name + " " + last_name
                email_list = True

                print("The user with the email address ", x.email, "has been updated")
            
            index+=1
    
        if not email_list:
            print("This email address is not in the database!")
            UserRegistration.update()
      
def selection(choice):
    user = UserRegistration
    choices = {"a": user.add, "b": user.show, "c": user.remove, "d": user.update}

    choices[choice]()

while choice != "e":
    index = 0
    within_range = False

    print("\nSelect the feature that you want to try >> [a] Add a user [b] Show list of users [c] Remove a user [d] Update a user [e] Exit")
    choice = input("Choose your preference: ").lower()

    for i in range(ord('a'), ord('e')):  # The last letter (e) will not be included in the loop
        if choice == chr(i):
            selection(choice)
            within_range = True
    
    if choice != "e" and not within_range:
        print("\nInvalid input!", end = " ")

print("\nExit")



