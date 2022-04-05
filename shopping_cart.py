# module exit the program when called
import sys


# The program title
def app_name():
    """
    This is the title of the program
    """
    print("""\n                           $$$$$$$$$$$$$""")
    print("""                                     $$$""")
    print("""               Shopping Cart  V1.0   $$$""")
    print("""                                     $$$""")
    print("""       $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")


# welcome message that greets the user
def greeting():
    while True:
        name = (input("\n      Enter your name: ").title().strip())
        if any(char.isdigit() for char in name):
            print("\nInvalid input, letters only not numbers\n")
        elif not name:
            print("\nPlease enter a valid input\n")
        elif any(not char.isalnum() for char in name):
            print("\n** Please enter a valid input **\n")
            continue
        else:
            print("\n    =-----------------------------------------------=")
            print(f"      Hello {name}, welcome to your shopping cart v1.0")
            print("      =-----------------------------------------------=")
            print("\n    ")
            input("\n       <<< Press Enter to access menu >>>    ")
            break


# An empty list that will contain user input
my_cart = []
new_cart = []


# This is the main menu where user can pick a selection to execute a task
def dash_board():
    while True:
        print("""   <<<<<<<< OPTION MENU >>>>>>>> """)
        print("""  """)
        print("""   Press 1 - 6 to select option""")
        print("""  """)
        print("        1: Add item")
        print("        2: View cart")
        print("        3: Find item")
        print("        4: Delete item")
        print("        5: Empty cart  ")
        print("        6: Exit app ""\n")
        option = input("Select option: ")
        if option == "1":
            print("\n    =========================")
            print("    <<  Add item to Cart  >>")
            print("    =========================""\n")
            add_item()
        elif option == "2":
            print("\n    =========================")
            print("    <<      View cart    >>  ")
            print("    =========================""\n")
            view_cart()
        elif option == "3":
            print("\n     =========================")
            print("     <<    Find item   >>")
            print("     =========================""\n")
            find_item()
        elif option == "4":
            print("\n     =========================")
            print("     <<       Delete item   >>")
            print("     =========================""\n")
            delete_item()
        elif option == "5":
            print("\n     =========================")
            print("     <<      Empty cart     >>")
            print("     =========================""\n")
            empty_cart()
        elif option == "6":
            print("\n     =========================")
            print("     <<     Exit program    >>")
            print("     =========================""\n")
            exit_app()
        elif not option:
            print("** Invalid input please enter 1-6 **")
            input("\nPress enter to return to Menu")
        else:
            print("Invalid option selected, RETRY!!!")
            input("\nPress enter to return to Menu")


# Takes user input , add and save to text file 
def add_item():
    while True:
        item_add = (
            input("\nAdd item to cart: ")
            .title()
            .strip()
        )
        if any(char.isdigit() for char in item_add):
            print("\nPlease enter a word not numbers\n")
        elif any(not char.isalnum() for char in item_add):
            print("\nPlease enter a valid input\n")
            continue
        elif not item_add:
            print("\nPlease enter a valid input\n")
        elif item_add + "\n" in my_cart:
            print(f"\n{item_add} is already in cart""\n")
            input("\nPress enter to continue")
            break
        else:
            print(f"\n## \"{item_add}\" added to cart ##""\n")
            input("\nPress enter to return to Menu")
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
        print("\n____!!!Your shopping cart is empty____""\n")
    input("\nPress enter to return to Menu")


# This function opens the file to read from the saved data
def get_cart_data():
    with open("cart_data.txt", "r+", encoding='utf-8') as my_list:
        for line in my_list:
            my_cart.append(line)


# Find item in the cart based on user input and return a message
def find_item():
    while True:
        search_item = (
            input("Find item in cart: ")
            .title()
            .strip()
        )
        if any(char.isdigit() for char in search_item):
            print("\n### Please input letters not numbers ###\n")
        elif any(not char.isalnum() for char in search_item):
            print("\n### Enter a valid input ###\n")
            continue
        elif search_item + '\n' in my_cart:
            print(f"\n$$$ \"{search_item}\" is in your cart $$$""\n")
            input("\nPress Enter to continue")
            break
        elif not search_item:
            print("\n### Enter a valid input ###\n")
        else:
            print(f"\n$$$ \"{search_item}\" is not in your cart $$$""\n")
            input("\nPress Enter to continue""\n")
            break


#  This particular function finds and delete a specific item from the cart
def delete_item():
    while True:
        to_delete = (
            input("Find item to delete from cart: ")
            .title()
            .strip()
            )
        if any(char.isdigit() for char in to_delete):
            print("\n### Please input letters not numbers ###\n")
        elif any(not char.isalnum() for char in to_delete):
            print("\n### Enter a valid input ###\n")
            continue
        elif not to_delete:
            print("\n### Enter a valid input ###\n")
        elif to_delete + '\n' not in my_cart:
            print(f"\n## !!!Oops, \"{to_delete}\" is not in your cart ##")
            input("\nPress enter to continue")
            break
        else:
            my_cart.remove(to_delete + '\n')
            print(f"\n### \"{to_delete}\" deleted from your cart ###""\n")
            save_data()
            input("\nPress Enter to continue""\n")
            break


# When this function is called, it empties the cart
def empty_cart():
    while True:
        erase_all = (
            input("\nEnter y to erase or n to return: ")
            .strip()
        )
        if any(char.isdigit() for char in erase_all):
            print("\nInvalid input, letters only not numbers\n")
        elif any(not char.isalnum() for char in erase_all):
            print("\n** Please enter a valid input **\n")
            continue
        elif not erase_all:
            print("\nPlease enter a valid input\n")
        elif len(my_cart) > 0:
            my_cart.clear()
            print("\n###   Your shopping cart is now empty   ###""\n")
            save_data()
            input("\nPress enter to return to Menu")
            dash_board()
            break
        else:
            print("\n###    Nothing to Erase in cart    ###")
            input("\nPress enter to return to Menu")
            dash_board()
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
def main():
    app_name()
    greeting()
    dash_board()


main()



