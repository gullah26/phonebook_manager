import sys

contacts = []


def title():
    print("\n             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("             $$$$                                            $$$$")
    print("             $$$$           PHONEBOOK MANAGER V1.0           $$$$")
    print("             $$$$                                            $$$$")
    print("             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    name = input("                       \nEnter your name: ")
    print("                ---------------------------------------------")
    print(f"                   Hello {name}, welcome to your phonebook  ")
    print("                ---------------------------------------------")
    print("\n                    <<<<<< Press Enter to access menu >>>>>    ")
    input()


title()


directory_file = open("phonebook.txt", "r")
directory_file.close


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
        print("                     =========================""\n")      
        add_contact()
    elif option == "2":
        print("                     =========================")
        print("                  <<<<<<<< VIEW CONTACT(S) >>>>>>>>  ")
        print("                     =========================""\n")
        display_saved_contact()
    elif option == "3":
        print("                     =========================")
        print("                 <<<<<<<< SEARCH CONTACT >>>>>>>>  ")
        print("                     =========================""\n")
        search_contact()
    elif option == "4":
        print("                     =========================")
        print("                   <<<<<<<< DELETE CONTACT >>>>>>>>  ")
        print("                     =========================""\n")
        delete_contact()
    elif option == "5":
        print("                     =========================")
        print("                 <<<<<<<< RESET PHONEBOOK >>>>>>>>  ")
        print("                     =========================""\n")
        reset_phonebook()
    elif option == "6":
        print("                     =========================")
        print("                   <<<<<<< EXIT PROGRAM >>>>>>>   ")
        print("                     =========================""\n")
        print("Press Enter to Exit")
        input()
        sys.exit("**** THANK YOU FOR YOUR TIME ***")
    else:
        print("Invalid option selected, RETRY!!!")
        print("Press enter to Return to Menu")
        input()
        option_menu()


def add_contact():
    global contacts
    fname = input("\n\nEnter first name: ")
    lname = input("Enter last name: ")    
    email = input("Enter email address: ")
    if str("@") not in email and str(".") not in email:
        print("Enter correct email")
        add_contact()        
    phone = int(input("Enter Phone #: "))
    if type(phone) != int:
        print("Please enter a number")
    elif len(str(phone)) < 10 and len(str(phone)) > 10:
        print("Number should not be less or greater than 10 digit")
        add_contact()
    details = f"\nfname:{fname}\nlname:{lname}\nphone#:{phone}\nEmail:{email}"
    contacts.append(details)
    directory_file = open("phonebook.txt", "a")
    directory_file.write(details)
    directory_file.write('\n')
    directory_file.close()

    
    print("\n"              "*** ADD CONTACT SUCCESSFUL ***""\n")
    print("\nPress enter to return to Menu""\n")
    input()
    option_menu()


def display_saved_contact():
    global contacts
    if len(contacts) == 0:
        print("\n                    Oops!!! Nothing to display")
        print("\n                  Press Enter to return to Menu")
        input()
        option_menu()
    else:
        directory_file = open("phonebook.txt", "r")
        contacts = directory_file.read()
        print(*contacts)
        directory_file.close
        print("\nPress Enter to return to Menu")
        input()
        option_menu()


def search_contact():
    """find a specific contact in phone directory"""
    find_contact = input("search directory: ")
    directory_file = open("phonebook.txt", "r")
    contacts = directory_file.read()
    if find_contact in contacts:
        print(f" {find_contact}  is in  the phonebook")
        print("Press enter to return to Menu")
        input()
        option_menu()
    else:
        print(f" No record of {find_contact} in directory")
        print("Press enter to return to Menu")
        input()
        option_menu()
  


#def delete_contact():
     

option_menu()


display_saved_contact()


search_contact()


#def reset_phonebook():
# pass
