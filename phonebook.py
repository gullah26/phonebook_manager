import sys

"""
=====================================
WELCOME TO PHONEBOOK MANAGER  - v1.0
=====================================

"""
name = input("Enter your name: ")
print()
print(f"     Hello {name}, welcome to Phonebook Manager v1.0")
print("""

    ***************************************
    To access each option, press 1 - 7
    ***************************************
    1. View phonebook
    2. Add new contact
    3. Find contact
    4. Delete contact
    5. Number of contact saved
    6. Empty phonebook
    7. Quit
""")
file = open(register.txt, "a+")
file.close

def phone_book():
    selected_option = input("Make a choice: ") # Ask the user to make a selection
    if selected_option == "1":
        file = open(register.txt, "r+")
        file_data = file.read()
            if len(file_data) == 0:
                print("No contact in directory")
            else:
                print(file_data)
            file.close
            show_contact_list()
    elif selected_option == "2":
        add_contact()        
    elif selected_option == "3":
        delete_contact()        
    elif selected_option == "4":
        find_contact()        
    elif selected_option == "5":
        num_of_contact()        
    elif selected_option == "6":
        empty_phonebook()
        
    elif selected_option == "7":
        sys.exit()
        
    else:
        print(" **** !!!!,Invalid entry ****")

contact_data =  [] 

#show_contact_list():
    #print("contact_data")
    #for contact in contact_data:
        #print("* " + contact)


#add_contact()


#delete_contact()

#find_contact()

#num_of_contact()

#add_contactempty_phonebook()

phone_book()