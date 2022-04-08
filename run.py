import sys
from datetime import datetime

# An empty list that will contain user input
my_list = []
new_list = []


def greeting():
    this_hour = int(datetime.now().strftime('%H'))
    # The program title logo
    print("\n      %%%%%%%%%              %%%%%%%%%")
    print("      %%%                          %%%")
    print("      %%%    Shopping list  V1.0   %%%")
    print("      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# welcome message that greets the user based on time of the day
    while True:
        name = (input("\nPlease Enter your name:\n").title().strip())
        if any(char.isdigit() for char in name):
            print("\nInvalid input, letters only not numbers\n")
        elif not name:
            print("\nPlease enter a valid input\n")
        elif this_hour < 12:
            print(f"\nGood morning {name}, welcome to your shopping list")
            print("=-----------------------------------------------------=")
            input("\n<<< Press Enter to access menu:>>>\n")
        elif 12 <= this_hour < 18:
            print(f"\nGood afternoon {name}, welcome to your shopping list")
            print("=------------------------------------------------------=")
            input("\n<<< Press Enter to access menu:>>>\n")
            continue
        else:
            print(f"\nGood evening {name}, welcome to your shopping list")
            print("=----------------------------------------------------=")
            input("\n<<< Press Enter to access menu:>>>\n")
            break


# This is the main menu where user can pick a selection to execute a task
def option_menu():
    while True:
        # user can select option between 1 to 7
        print("%%%%%% OPTION MENU %%%%%%")
        print("  ")
        print("\nPress 1 - 7 to select option")
        print("  ")
        print("1: Add item")
        print("2: View list")
        print("3: Total item in list")
        print("4: Find item")
        print("5: Delete item")
        print("6: Empty list  ")
        print("7: Exit app ""\n")
        # User input to select an option
        option = input("Select option:\n")
        if option == "1":
            print("<<  Add item to list  >>")
            print("=========================""\n")
            add_item()
        elif option == "2":
            print("   <<  View list  >>")
            print("=======================""\n")
            view_list()
        elif option == "3":
            print("  << Number of items in list >>")
            print("================================""\n")
            item_total()
        elif option == "4":
            print("  <<  Find item >>")
            print("====================""\n")
            find_item()
        elif option == "5":
            print(" <<  Delete item  >>")
            print("======================""\n")
            delete_item()
        elif option == "6":
            print("   <<  Empty list >>")
            print("======================""\n")
            empty_list()
        elif option == "7":
            print("  <<  Exit program >>")
            print("=======================""\n")
            exit_program()
        elif not option:
            print("** Invalid input please enter 1-7 **")
            input("\nPress enter to return to Menu\n")
        else:
            print("** Invalid input please press enter")


# Takes user input , add and save to text file
def add_item():
    while True:
        item_add = (
            input("\nAdd item to list:\n")
            .title()
            .strip()
        )
        # checks to validate correct user input
        if any(char.isdigit() for char in item_add):
            print("\nPlease enter  words not numbers\n")
        # elif any(not char.isalnum() for char in item_add):
        #     print("\nPlease enter a valid input\n")
        elif not item_add:
            print("\nPlease enter a valid input\n")
            continue
        elif item_add + "\n" in my_list:
            print(f"\n{item_add} was previously added to list""\n")
            input("\nPress enter to continue\n")
            break
        else:
            print(f"\n \"{item_add}\" was added to list\n")
            input("\nPress enter to return to Menu\n")
            my_list.append(item_add + "\n")
            save_data()
            break


# The content of the shopping list is displayed by calling this function
def view_list():
    if len(my_list) > 0:
        with open("cart_data.txt", "r+", encoding='utf-8'):
            for i, item in enumerate(my_list, 1):
                print(f"   item {i}: {item}", end="")
            input("\nPress Enter to continue\n")
    else:
        print("\nlist is empty, Try adding an item\n")
        input("\nPress enter to return to Menu\n")


def item_total():
    print(f"\nTotal number of item(s) in your list is : {len(my_list)}\n")
    input("\nPress Enter to continue\n")


# This function opens the file to read from the saved data
def get_cart_data():
    with open("cart_data.txt", "r", encoding='utf-8') as file:
        for line in file:
            my_list.append(line)


# Save data in "W" write mode overwrites and clear any existing data
def save_data():
    list_list = new_list + my_list
    with open("cart_data.txt", "w", encoding='utf-8') as data_file:
        for x in list_list:
            if x != "\n":
                data_file.write(x)

    new_list.clear()
    my_list.clear()
    get_cart_data()


# Find item in the list based on user input and return a message
def find_item():
    while True:
        search_item = (
            input("Find item in list:\n")
            .title()
            .strip()
        )
        # checks to validate correct user input
        if any(char.isdigit() for char in search_item):
            print("\n### Please input letters not numbers ###\n")
        # elif any(not char.isalnum() for char in search_item):
        #     print("\n### Enter a valid input ###\n")
        #   continue
        elif search_item + '\n' in my_list:
            print(f"\n \"{search_item}\" is in your list\n")
            input("\nPress Enter to continue:\n")
            break
        elif not search_item:
            print("\n### Enter a valid input ###\n")
        else:
            print(f"\n \"{search_item}\" is not in your list\n")
            input("\nPress Enter to continue:\n")
            break


#  This particular function finds and delete a specific item from the list
def delete_item():
    while True:
        to_delete = (
            input("\nFind item to delete from list:\n")
            .title()
            .strip()
            )
        # checks to validate correct user input
        if any(char.isdigit() for char in to_delete):
            print("\n### Please input letters not numbers ###\n")
        # elif any(not char.isalnum() for char in to_delete):
        #     print("\n### Enter a valid input ###\n")
        #     continue
        elif not to_delete:
            print("\nEnter a valid input\n")
        elif to_delete + '\n' not in my_list:
            print(f"\n\"{to_delete}\" not deleted , it is NOT in your list")
            input("\nPress enter to continue:\n")
            break
        else:
            my_list.remove(to_delete + "\n")
            print(f"\n \"{to_delete}\" found and deleted from your list\n")
            save_data()
            input("\nPress Enter to continue:\n")
            break


# When this function is called, it empties the list
def empty_list():
    while True:
        if len(my_list) > 0:
            my_list.clear()
            print("\nYour  list is now empty\n")
            save_data()
            input("\nPress enter to return to Menu:\n")
            option_menu()
            break
        else:
            print("\nList is already empty, nothing to erase")
            input("\nPress enter to return to Menu:\n")
            option_menu()
            break


# This Exit function terminates  the program execution
def exit_program():
    exit_hour = int(datetime.now().strftime('%H'))
    choice = input("\nPress \"y\" to exit or \"n\" to re-start program\n")
    if choice == "y":
        if exit_hour < 12:
            print("\nThank you for your time =:)\n")
            print("\nEnjoy the rest of your morning\n")
            sys.exit(0)
        elif 12 <= exit_hour < 18:
            print("\nThank you for your time =:)\n")
            print("\nEnjoy the rest of your day\n")
            sys.exit(0)
        else:
            print("\nThank you for your time =:)\n")
            print("\nEnjoy the rest of your evening\n")
            sys.exit(0)
    elif choice == "n":
        greeting()
    else:
        option_menu()


# this funtion re-runs program
def main():
    greeting()
    get_cart_data()
    option_menu()


main()
