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
    print("             \n<<<<<< Press Enter to access menu >>>>>")
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
        print("                     =========================")
        print("                   <<<<<<<< ADD CONTACT >>>>>>>>       ")
        print("                     =========================")      
        add_contact()
    elif option == "2":
        print("                     =========================")
        print("                  <<<<<<<< VIEW CONTACT(S) >>>>>>>>  ")
        print("                     =========================")
        display_saved_contact()
    elif option == "3":
        print("                     =========================")
        print("                 <<<<<<<< SEARCH CONTACT >>>>>>>>  ")
        print("                     =========================")
        search_contact()
    elif option == "4":
        print("                     =========================")
        print("                   <<<<<<<< DELETE CONTACT >>>>>>>>  ")
        print("                     =========================")
        delete_contact()
    elif option == "5":
        print("                     =========================")
        print("                 <<<<<<<< RESET PHONEBOOK >>>>>>>>  ")
        print("                     =========================")
        reset_phonebook()
    elif option == "6":
        print("                     =========================")
        print("                      ((((( EXIT PROGRAM )))))   ")
        print("                     =========================")
        print("Press Enter to Exit")
        input()
        sys.exit(" Thank you for using the program")
    else:
        print("Invalid option selected, RETRY!!!")
        print("Press enter to Return to Menu")
        input()
        option_menu()


option_menu()


def add_contact():
    global contacts
    fname = input("Enter first name: ")
    fname.title()
    lname = input("Enter last name: ")
    lname.title()
    phone = int(input("Enter Phone#: "))
    email = input("Enter email address: ")   
    details = [(f"{fname} {lname} | {phone} | {email}""\n")]
    contacts.append(details)
    file = open("phonebook.txt", "a")
    file.write(details)
    file.close
    print("Contact added to Phonebook")
    print("Press enter to return to Menu")
    option_menu()



#def display_saved_contact():
   # pass


#def search_contact():
   # pass


#def delete_contact():
  #  pass


#def reset_phonebook():
   # pass