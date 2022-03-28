import sys

contacts = []

def title():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$                                            $$$$")
    print("$$$$           PHONEBOOK MANAGER V1.0           $$$$")
    print("$$$$                                            $$$$")    
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    name = input("\n\nEnter Your name: ")

    print("  ---------------------------------------------")
    print(f"     Hello {name}, welcome to your phonebook  ")
    print("  ---------------------------------------------")
    print("\nPress Enter to access menu")
    input()


title()


def menu():
    print("     =========================")
    print("             Option Menu     ")
    print("     =========================")
    print("    Press 1 - 6 to select option")
    print("    ****************************")
    print("     1: View saved contact(s)")
    print("     2: Add contact")
    print("     3: Search contact")
    print("     4: Delete contact")
    print("     5: Reset phonebook  ")
    print("     6: Exit app ")
    option = input("Select option: ")
    if option == "1":
        print("=========================")
        print("     VIEW CONTACT(S)     ")
        print("=========================")
        display_saved_contact()
    elif option == "2":
        print("=========================")
        print("     ADD CONTACT         ")
        print("=========================")
        add_contact()
    elif option == "3":
        print("=========================")
        print("      SEARCH CONTACT     ")
        print("=========================")
        search_contact()
    elif option == "4":
        print("=========================")
        print("      DELETE CONTACT     ")
        print("=========================")
        delete_contact()
    elif option == "5":
        print("=========================")
        print("      RESET PHONEBOOK    ")
        print("=========================")
        reset_phonebook()
    elif option == "6":
        print("=========================")
        print("       EXIT PROGRAM      ")
        print("=========================")
        print("Press Enter to Exit")
        input()
        sys.exit(" Thank you for using the program")
    else:
        print("Invalid option selected, RETRY!!!")
        print("Press enter to Return to Menu")
        input()


menu()



def display_saved_contact():
    pass


def add_contact():
    pass


def search_contact():
    pass


def delete_contact():
    pass


def reset_phonebook():
    pass