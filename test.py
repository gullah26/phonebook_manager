import sys


# An empty list that will contain user input
my_cart = []
new_cart = []


def greeting():
    # The program title
    print("                       %%%%%%%%%")
    print("                             %%%")
    print("         Shopping Cart  V1.0 %%%")
    print("                             %%%")
# welcome message that greets the user
    while True:
        name = (input("\nEnter your name:\n").title().strip())
        if any(char.isdigit() for char in name):
            print("\nInvalid input, letters only not numbers\n")
        elif not name:
            print("\nPlease enter a valid input\n")
        elif any(not char.isalnum() for char in name):
            print("\n** Please enter a valid input **\n")
            continue
        else:
            print(f"\nHello {name}, welcome to your shopping cart v1.0")
            print("=-----------------------------------------------=")
            print("\n    ")
            input("\n<<< Press Enter to access menu: >>>\n")
            break


# This is the main menu where user can pick a selection to execute a task
def option_menu():
    # user can select option between 1 to 6
    print("%%%%%% OPTION MENU %%%%%%")
    print("  ")
    print("Press 1 - 6 to select option")
    print("  ")
    print("1: Add item")
    print("2: View cart")
    print("3: Find item")
    print("4: Delete item")
    print("5: Empty cart  ")
    print("6: Exit app ""\n")
    # User input to select an option
    option = input("Select option: ")
    if option == "1":
        print("<<  Add item to Cart  >>")
        print("=========================""\n")
        add_item()
    elif option == "2":
        print("   <<  View cart  >>")
        print("=======================""\n")
        view_cart()
    elif option == "3":
        print("  <<  Find item >>")
        print("====================""\n")
        find_item()
    elif option == "4":
        print(" <<  Delete item  >>")
        print("======================""\n")
        delete_item()
    elif option == "5":
        print("   <<  Empty cart >>")
        print("======================""\n")
        empty_cart()
    elif option == "6":
        print("  <<  Exit program >>")
        print("=======================""\n")
        exit_app()
    elif not option:
        print("** Invalid input please enter 1-6 **")
        input("\nPress enter to return to Menu""\n")
    else:
        option_menu()


# Takes user input , add and save to text file
def add_item():
    while True:
        item_add = (
            input("\nAdd item to cart:\n")
            .title()
            .strip()
        )
        # checks to validate correct user input
        if any(char.isdigit() for char in item_add):
            print("\nPlease enter a word not numbers\n")
        elif any(not char.isalnum() for char in item_add):
            print("\nPlease enter a valid input\n")
            continue
        elif not item_add:
            print("\nPlease enter a valid input\n")
        elif item_add + "\n" in my_cart:
            print(f"\n{item_add} is already in cart""\n")
            input("\nPress enter to continue\n")
            break
        else:
            print(f"\n%%%%%% \"{item_add}\" added to cart %%%%%%""\n")
            input("\nPress enter to return to Menu\n")
            with open("cart_data.txt", "a", encoding='utf-8') as file:
                my_cart.append(item_add + "\n")
                file.write('\n'.join(my_cart))
            break


# The content of the shopping cart is displayed by calling this function
def view_cart():
    print("\n")
    print(f"   Total item(s) in your cart is : {len(my_cart)} ""\n")
    if len(my_cart) > 0:
        with open("cart_data.txt", "r", encoding='utf-8'):
            for i, item in enumerate(my_cart, 1):
                print(f"   item {i}: {item}", end="")
    else:
        print("\n%%%%%% Your shopping cart is empty %%%%%%""\n")
        input("\nPress enter to return to Menu ")
        option_menu()


# This function opens the file to read from the saved data
def get_cart_data():
    with open("cart_data.txt", "r+", encoding='utf-8') as my_list:
        for line in my_list:
            my_cart.append(line)


# Find item in the cart based on user input and return a message
def find_item():
    while True:
        search_item = (
            input("Find item in cart:\n")
            .title()
            .strip()
        )
        # checks to validate correct user input
        if any(char.isdigit() for char in search_item):
            print("\n### Please input letters not numbers ###\n")
        elif any(not char.isalnum() for char in search_item):
            print("\n### Enter a valid input ###\n")
            continue
        elif search_item + '\n' in my_cart:
            print(f"\n%%%%%% \"{search_item}\" is in your cart %%%%%%""\n")
            input("\nPress Enter to continue:\n")
            break
        elif not search_item:
            print("\n### Enter a valid input ###\n")
        else:
            print(f"\n%%%%%% \"{search_item}\" is not in your cart %%%%%%""\n")
            input("\nPress Enter to continue: ""\n")
            break


#  This particular function finds and delete a specific item from the cart
def delete_item():
    while True:
        to_delete = (
            input("Find item to delete from cart:\n")
            .title()
            .strip()
            )
        # checks to validate correct user input
        if any(char.isdigit() for char in to_delete):
            print("\n### Please input letters not numbers ###\n")
        elif any(not char.isalnum() for char in to_delete):
            print("\n### Enter a valid input ###\n")
            continue
        elif not to_delete:
            print("\n%%% Enter a valid input %%%\n")
        elif to_delete + '\n' not in my_cart:
            print(f"\n%%%!!!Oops, \"{to_delete}\" is NOT in your cart %%%")
            input("\nPress enter to continue:\n")
            break
        else:
            my_cart.remove(to_delete + "\n")
            print(f"\n%%%% \"{to_delete}\" deleted from your cart %%%%""\n")
            save_data()
            input("\nPress Enter to continue:\n""\n")
            break


# When this function is called, it empties the cart
def empty_cart():
    while True:
        if len(my_cart) > 0:
            my_cart.clear()
            print("\n%%%%%% Your shopping cart is now empty %%%%%%""\n")
            save_data()
            input("\nPress enter to return to Menu:\n")
            option_menu()
            break
        else:
            print("\n%%%%  Nothing  in cart to Erase in cart %%%%")
            input("\nPress enter to return to Menu:\n")
            option_menu()
            break


# Save data in "W" write mode overwrites and clear any existing data
def save_data():
    cart_list = new_cart + my_cart
    with open("cart_data.txt", "w", encoding='utf-8') as output_file:
        for x in cart_list:
            if x != "\n":
                output_file.write(x)

    new_cart.clear()
    my_cart.clear()
    get_cart_data()


# This Exit function terminates  the program execution
def exit_app():
    input("Press Enter to Exit")
    sys.exit(" --( Thank you for your time =:)--")


# main  will run the program again
option_menu()





