import sys

contacts = []

def menu_display():
    print(        
    '''
    Phonebook Menu
    ____________________________
    ****************************
    Press 1-7 to select option
    ****************************
    1: View saved contact(s)
    2: Add contact
    3: Find contact
    4: Delete contact
    5: Reset phonebook    
    6: Exit app
    
    '''
    )

def title_display():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$                                            $$$$")
    print("$$$$              PHONEBOOK MANAGER V1.0        $$$$")
    print("$$$$                                            $$$$")    
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    name = input("\n\nEnter Your name: ")

    print("        _________________________________________")
    print(f"        Hello {name}, welcome to your phonebook    ")
    print("        -----------------------------------------")
    print("\nPress Enter to access menu")
    input()
    menu_display()

title_display()


def main():
    pass
    
def add_contact():
    pass

def display_saved_contact():
    pass

def search_contact():
    pass
    
def delete_contact():
    pass
    
def reset_phonebook():
    pass
    
   

main()