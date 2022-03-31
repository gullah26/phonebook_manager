import sys

contacts = {}

directory_file = open("phonebook.txt", "r")
directory_file.close()


def title():
    print("""\n
              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            $$$$                                       $$$$
        $$$$           PHONEBOOK MANAGER V1.0              $$$$
            $$$$                                       $$$$
              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        """)
    name = input("           \nEnter your name: ")
    print("      ---------------------------------------------")
    print(f"        Hello {name}, welcome to your phonebook  ")
    print("      ---------------------------------------------")
    print("\n       <<< Press Enter to access menu >>>    ")
    input()


title()


def option_menu():
    print("    <<<<<<<< OPTION MENU >>>>>>>>   ")
    print("    ****************************")
    print("    Press 1 - 6 to select option")
    print("    ****************************")
    print("     1: Add contact")
    print("     2: View saved contact(s)")
    print("     3: Search contact")
    print("     4: Delete contact")
    print("     5: Reset phonebook  ")
    print("     6: Exit app ""\n")
    option = input("Select option: ")
    if option == "1":
        print("    =========================")
        print("    <<      Add Contact    >>")
        print("    =========================""\n")
        add_contact()
    elif option == "2":
        print("    =========================")
        print("    <<    View Contact(s)  >>  ")
        print("    =========================""\n")
        display_saved_contact()
    elif option == "3":
        print("     =========================")
        print("     <<    Search Contact   >>")
        print("     =========================""\n")
        search_contact()
    elif option == "4":
        print("     =========================")
        print("     <<    Delete Contact   >>")
        print("     =========================""\n")
        delete_contact()
    elif option == "5":
        print("     =========================")
        print("     <<   Reset Phonebook   >>")
        print("     =========================""\n")
        reset_phonebook()
    elif option == "6":
        print("     =========================")
        print("     <<     Exit program    >>")
        print("     =========================""\n")
        print("Press Enter to Exit")
        input()
        sys.exit(" **** Thank you for your time ***")
        title()
    else:
        print("Invalid option selected, RETRY!!!")
        print("Press enter to Return to Menu")
        input()
        option_menu()


def add_contact():
    contacts['first_name'] = input("Enter first name: ")
    contacts['last_name'] = input("Enter Last name: ")
    contacts['e_mail'] = input("Enter Email: ")
    contacts['phone'] = int(input("Enter phone #: "))
    directory_file = open("phonebook.txt", "a")
    directory_file.write(str(contacts))
    directory_file.write('\n')
    directory_file.close()
    print("\n""  *** Contact add successful ***""\n")
    print("\nPress enter to return to Menu""\n")
    input()
    option_menu()


def display_saved_contact():
    global contacts
    global directory_file
    if len(str(contacts)) == 0:
        print("\n   Oops! nothing to display")
        print("\n   Press Enter to return to Menu")
        input()
        option_menu()
    else:
        with open("phonebook.txt") as directory_file:
            for content in directory_file:
                print(content)      
                print("\nPress Enter to return to Menu")
                input()
                option_menu()


def search_contact():
    """find a specific contact in phone directory"""
    global contacts
    global directory_file   
    
    
    find_contact = input("Search Phonebook: ")
    with open("phonebook.txt") as directory_file:
        for content in directory_file:
            print(content)
    new_content = []
    line_index = 0
    for contact in contacts:
        if find_contact in contact:
            new_content.insert(line_index, contact)
            line_index += 1
    directory_file.close()    
    if len(new_content) == 0:
        print(f"\n{find_contact} is not found in phonebook!")
    else:
        contactLen = len(new_content)
        print("@" * 40)
        print(f"\n**** Lines containing {find_contact}****\n")
        print("@" * 40)
        for i in range(contactLen):
            print(end=new_content[i])
            print("Press enter to return to Menu")
            option_menu()


def delete_contact():
    pass


def reset_phonebook():
    global directory_file
    print("This will erase all contacts from the phonebook")
    answer = input("Press y/n to continue: ")
    if answer == "y":
        directory_file = open("phonebook.txt", "w")
        directory_file.close()
        print("All Contact(s) deleted")
        print("Press enter to return to Menu")
        input()
        option_menu()
    elif answer == "n":
        print("Press enter to return to Menu")
        input()
        option_menu()
    else:
        print("Press enter to return to Menu")
        input()
        option_menu()


option_menu()


display_saved_contact()


search_contact()


reset_phonebook()
